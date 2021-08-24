from gcsfs import GCSFileSystem
import apache_beam
import pandas as pd
import numpy as np
import ast
from augury_beam.io.feature_pool import ReadTimeRangeMachineFeatures
from augury_beam.options import AuguryPipelineOptions
from google.cloud import storage
from joblib import Parallel, delayed

from DoFn.detector_features_builder import DetectorFeaturesBuilder
from DoFn.flat_features import Flat_Features
from utils.helpers import DEFAULT_PIPELINE_OPTION_ARGS, map_time_range, convert_to_csv_format_with_header, \
    csv_to_dataframes


def fetch_features_to_csv(triggers_df: pd.DataFrame, gcs_output_path: str):
    beam_options = AuguryPipelineOptions(DEFAULT_PIPELINE_OPTION_ARGS)
    beam_pipeline = apache_beam.Pipeline(options=beam_options)

    sessions = []
    if 'session_ids' in triggers_df:
        try:
            sessions = list(np.concatenate(triggers_df['session_ids'].apply(lambda lst: np.array(ast.literal_eval(lst))).values))
        except ValueError:
            sessions = triggers_df['session_ids'].to_list()
        triggers_df = triggers_df.drop('session_ids', axis=1)

    triggers = list(triggers_df.T.to_dict().values())

    time_ranges = (
            beam_pipeline
            | "Create time ranges" >> apache_beam.Create(triggers)
            | "Map to MachineTimeRange" >> apache_beam.Map(map_time_range)
    )
    machine_features = (
            time_ranges
            | "Read all machine samples" >> ReadTimeRangeMachineFeatures()
    )
    detector_features = (
            machine_features
            | 'MachineFeatures to DetectorFeatures' >> apache_beam.ParDo(DetectorFeaturesBuilder(sessions))
    )

    flat_features = (
            detector_features
            | "Flat features" >> apache_beam.ParDo(Flat_Features())
            | "Drop irrelevant sessions" >> apache_beam.Filter(lambda df: df is not None))

    flat_features_csv_format = (
            flat_features
            | "Convert to csv format" >> apache_beam.FlatMap(convert_to_csv_format_with_header)
    )

    _ = (
            flat_features_csv_format
            | "Write to csv" >> apache_beam.io.textio.WriteToText(gcs_output_path, file_name_suffix='.csv')
    )

    beam_pipeline.run().wait_until_finish()


def output_to_one_file(gcs_output_path):
    storage_client = storage.Client()
    sub_path = gcs_output_path[5:]
    bucket_name = sub_path[:sub_path.index('/')]
    bucket = storage_client.get_bucket(bucket_name)
    prefix = gcs_output_path.replace(f'gs://{bucket_name}/', '')
    csv_paths = [f"gs://{bucket.name}/{csv_path.name}" for csv_path in
                 list(bucket.list_blobs(prefix=prefix)) if '-of-' in csv_path.name]

    def parallel_for(csv_path):
        return csv_to_dataframes(csv_path)

    df_list = Parallel(n_jobs=min(len(csv_paths), 8))(delayed(parallel_for)(csv_path) for csv_path in csv_paths)

    df_list = sum(df_list, [])  # flat list

    df = pd.concat(df_list, ignore_index=True)
    df = df.drop_duplicates()
    meta_columns = ['machine_id', 'trigger_time', 'session_id', 'component_id', 'bearing', 'plane']
    df = df[meta_columns + sorted([column for column in df.columns if column not in meta_columns])]
    df.to_csv(f'{gcs_output_path}output.csv', index=False)

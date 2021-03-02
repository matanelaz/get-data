import datetime
from collections import defaultdict

import apache_beam as beam
from augury_data_utilities.helpers.component_helper import ComponentType, ComponentHelper
from augury_data_utilities.helpers.machine_features import MachineFeaturesEnrichment
import pandas as pd
from augury_data_utilities.helpers.machine_helper import MachineHelper

from src.ptransformers.utils.detector_features import Detector_Features
from src.ptransformers.utils.parameters import rapid_cliff_enhancements_features_list


def convert_to_csv(df):
    rows = []
    for record in df.values.tolist():
        row = ",".join(record)
        rows.append(row)
    return rows


class _Flat_Features(beam.DoFn):
    def process(self, mfg, **kwargs):
        flatted_features = defaultdict(list)
        machine_id = mfg['machine_id']
        recorded_at = mfg['recorded_at']
        session_id = mfg['session_id']

        for unflatted_key in mfg['parsed_features'].keys():
            flatted_features['machine_id'].append(machine_id)
            flatted_features['recorded_at'].append(recorded_at)
            flatted_features['session_id'].append(session_id)
            flatted_features['component_id'].append(unflatted_key.component_id)
            flatted_features['bearing'].append(unflatted_key.bearing_num)
            flatted_features['plane'].append(unflatted_key.plane)
            for parsed_feature in rapid_cliff_enhancements_features_list:
                flatted_features[parsed_feature].append(mfg['parsed_features'][unflatted_key].get(parsed_feature))
        df = pd.DataFrame(flatted_features).fillna('').astype(str)
        df = df[df['vibration_session_machine_on'] == '1']
        yield df if len(df) else None


class Rapid_Cliff_Enhancements_PTransform(beam.PTransform):

    def __init__(self,
                 detector_name: str,
                 batch_mode: bool
                 ):
        super(Rapid_Cliff_Enhancements_PTransform, self).__init__()
        self.batch_mode = batch_mode
        self.detector_name = detector_name

    def expand(self, machine_features):
        detector_features = (machine_features | 'MachineFeatures to DetectorFeatures' >> beam.ParDo(Detector_Features()))
        flat_features = (detector_features | "Flat features to be " >> beam.ParDo(_Flat_Features()) | "filter off sessions" >> beam.Filter(lambda df: df is not None))
        csv_format = flat_features | "convert_to_csv_format" >> beam.FlatMap(convert_to_csv)
        return csv_format
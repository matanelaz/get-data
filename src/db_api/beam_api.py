import os
import pandas as pd
import apache_beam as beam
from apache_beam.options.pipeline_options import StandardOptions
from augury_beam.io.proto import ReadAllAuguryProto

from augury_beam.options import AuguryPipelineOptions
from augury_proto.ml import feature_pb2
from configuration.config import Config
from db_api.utils.detector_transform import DetectionTransform
from db_api.utils.parameters import feature_list


class Beam_API:

    def __init__(self):
        self.__beam_options = AuguryPipelineOptions(Config.BEAM_PIPELINE_ARGS)
        self.__beam_pipeline = beam.Pipeline(options=self.__beam_options)

        if Config.FEATURES_INPUT_PUBSUB is not None:
            machine_features = (self.__beam_pipeline
                                | beam.io.ReadFromPubSub(subscription=Config.FEATURES_INPUT_PUBSUB)
                                | beam.Map(feature_pb2.MachineFeatures.FromString)
                                )
            batch = False
        else:
            input_pattern = [Config.FEATURES_INPUT_DIR + '**' if Config.FEATURES_INPUT_DIR.endswith('/') else Config.FEATURES_INPUT_DIR]
            machine_features = (
                    self.__beam_pipeline
                    | "Input pattern" >> beam.Create(input_pattern)
                    | "Read features (All Augury Proto)" >> ReadAllAuguryProto(proto_class=feature_pb2.MachineFeatures)
            )
            batch = True

        detections = (
                machine_features
                | "Run inference (prediction on features)" >> DetectionTransform(detector_name="rapid_cliff",
                                                                                 batch_mode=batch)
        )
        detections | "Write to csv" >> beam.io.textio.WriteToText(Config.DETECTIONS_OUTPUT_DIR, file_name_suffix='.csv',
                                                                  header=",".join(feature_list))

    def run(self):
        if self.__beam_options.view_as(StandardOptions).runner == "direct":
            self.__beam_pipeline.run().wait_until_finish()
        else:
            self.__beam_pipeline.run()

    def get_machine_features(self):
        # TODO
        folder_prefix = f"beam-temp-{os.path.basename(Config.DETECTIONS_OUTPUT_DIR[:-1])}"
        df = pd.read_csv(f'C:/Users/koren/Documents/beam-temp-beam_output_files_2021-02-16-e4c2debd703011eb9e70fc4482b7ccde/88a9af05-f2d1-4d1a-9839-5d9fdac815e0..csv')
        return df
import logging
import os
import pandas as pd
import apache_beam as beam
from apache_beam.options.pipeline_options import StandardOptions
from augury_beam.io.proto import ReadAllAuguryProto

from augury_beam.options import AuguryPipelineOptions
from augury_proto.ml import feature_pb2
from src.configuration.config import Config
from src.db_api.utils.detector_transform import DetectionTransform
from src.db_api.utils.parameters import feature_list
from src.utils.argparser import init_parser


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


def run_example():
    Beam_API().run()


if __name__ == '__main__':
    parser = init_parser()
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    input_args, beam_pipeline_args = parser.parse_known_args()
    Config(
        pipeline_class='',
        input_args=input_args,
        beam_pipeline_args=beam_pipeline_args
    )
    run_example()

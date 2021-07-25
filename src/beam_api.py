import apache_beam as beam
import pandas as pd
from apache_beam.options.pipeline_options import StandardOptions
from augury_beam.io.proto import ReadAllAuguryProto
from augury_beam.options import AuguryPipelineOptions
from augury_proto.ml import feature_pb2

from src.configuration.config import Config
from src.ptransformers.miss_detector_ptransform import Miss_Detector_PTransform
from src.ptransformers.rapid_cliff_enhancements_ptransform import Rapid_Cliff_Enhancements_PTransform
from src.ptransformers.take_machine_features_ptransform import Take_Machine_Features_PTransform
from src.ptransformers.utils.features import all_features, rapid_cliff_enhancements_features_list


class Beam_API:

    def __init__(self):
        self.__beam_options = AuguryPipelineOptions(Config.BEAM_PIPELINE_ARGS)

    def run_take_machine_features(self):
        triggers = pd.read_csv(Config.MACHINE_FEATURES_TRIGGER_FILE_PATH, names=["machine_id", "start", "end"])
        beam_pipeline = beam.Pipeline(options=self.__beam_options)
        _ = (
                beam_pipeline
                | "Take machine samples subset" >> Take_Machine_Features_PTransform(
            list(triggers.T.to_dict().values()),
            Config.GCS_MACHINE_FEATURES_OUTPUT_PATH
        )

        )
        return self.__run(beam_pipeline)

    def run_machine_features_to_csv(self):
        beam_pipeline = beam.Pipeline(options=self.__beam_options)

        if Config.FEATURES_INPUT_PUBSUB is not None:
            machine_features = (self.__beam_pipeline
                                | beam.io.ReadFromPubSub(subscription=Config.FEATURES_INPUT_PUBSUB)
                                | beam.Map(feature_pb2.MachineFeatures.FromString)
                                )
            batch = False
        else:
            input_pattern = [Config.FEATURES_INPUT_DIR + '**' if Config.FEATURES_INPUT_DIR.endswith(
                '/') else Config.FEATURES_INPUT_DIR]
            machine_features = (
                    beam_pipeline
                    | "Input pattern" >> beam.Create(input_pattern)
                    | "Read features (All Augury Proto)" >> ReadAllAuguryProto(proto_class=feature_pb2.MachineFeatures)
            )
            batch = True

        detections = (
                machine_features
                | "Run inference (prediction on features)" >> Miss_Detector_PTransform(
            detector_name="miss_detector", batch_mode=batch)
        )
        detections | "Write to csv" >> beam.io.textio.WriteToText(Config.DETECTIONS_OUTPUT_DIR, file_name_suffix='.csv',
                                                                  header=",".join(all_features))
        return self.__run(beam_pipeline)

    def __run(self, beam_pipeline):
        if self.__beam_options.view_as(StandardOptions).runner == "direct":
            return beam_pipeline.run().wait_until_finish()
        else:
            return beam_pipeline.run()

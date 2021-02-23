import apache_beam as beam
from augury_beam.io.feature_pool import ReadTimeRangeMachineFeatures, MachineTimeRange
from augury_beam.io.proto import WriteAuguryProto


class Take_Machine_Features_PTransform(beam.PTransform):
    def __init__(self, triggers, output_path):
        super().__init__()
        self.triggers = triggers
        self.output_path = output_path

    def expand(self, pipeline):
        output_prefix = self.output_path.rstrip("/") + "/machine-features-"

        def map_time_range(x):
            import datetime
            return MachineTimeRange(start=datetime.datetime.utcfromtimestamp(x['start']),
                                    end=datetime.datetime.utcfromtimestamp(x['end']),
                                    machine_id=x['machine_id'])

        time_ranges = (
            pipeline
            | "Create time ranges" >> beam.Create(self.triggers)
            | "Map to MachineTimeRange" >> beam.Map(map_time_range)
        )

        machine_features = (
                time_ranges
                | "Read all machine samples" >> ReadTimeRangeMachineFeatures()
                | "Write filtered machine samples" >> WriteAuguryProto(file_path_prefix=output_prefix)
        )

        return machine_features


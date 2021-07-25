import apache_beam as beam

from src.ptransformers.utils.detector_features import Detector_Features
from src.ptransformers.utils.flat_features import Flat_Features
from src.ptransformers.utils.features import all_features
from src.ptransformers.utils.utils import convert_to_csv


class Miss_Detector_PTransform(beam.PTransform):

    def __init__(self,
                 detector_name: str,
                 batch_mode: bool
                 ):
        super(Miss_Detector_PTransform, self).__init__()
        self.batch_mode = batch_mode
        self.detector_name = detector_name

    def expand(self, machine_features):
        detector_features = (machine_features | 'MachineFeatures to DetectorFeatures' >> beam.ParDo(Detector_Features()))
        flat_features = (detector_features | "Flat features to be " >> beam.ParDo(Flat_Features(features_list=all_features)) | "filter off sessions" >> beam.Filter(lambda df: df is not None))
        csv_format = flat_features | "convert_to_csv_format" >> beam.FlatMap(convert_to_csv)
        return csv_format

from enum import Enum

from src.ptransformers.miss_detector_ptransform import Miss_Detector_PTransform
from src.ptransformers.rapid_cliff_enhancements_ptransform import Rapid_Cliff_Enhancements_PTransform
from src.ptransformers.utils.features import rapid_cliff_enhancements_features_list, all_features


class Preferences(Enum):
    RAPID_CLIFF_ENHANCEMENTS = (Rapid_Cliff_Enhancements_PTransform, rapid_cliff_enhancements_features_list)
    MISS_DETECTOR_DEV = (Miss_Detector_PTransform, all_features)

    def __init__(self, ptransform, features_list):
        self.ptransform = ptransform
        self.features_list = features_list

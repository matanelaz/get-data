import os
from calendar import calendar
from datetime import datetime
from pathlib import Path


from src.utils.date_functions import get_current_date

WORK_DIR = os.environ['WORK_DIR']
ROOT_DIR = Path(__file__).parent.parent


class Config:

    BEAM_PIPELINE_ARGS: dict
    FEATURES_INPUT_PUBSUB: str
    FEATURES_INPUT_DIR: str
    DETECTIONS_OUTPUT_DIR: str

    GCS_MACHINE_FEATURES_OUTPUT_PATH: str
    MACHINE_FEATURES_TRIGGER_FILE_PATH: str

    def __init__(self, input_args, beam_pipeline_args):

        self.__class__.BEAM_PIPELINE_ARGS = beam_pipeline_args
        self.__class__.FEATURES_INPUT_PUBSUB = input_args.machine_features_input_pubsub
        self.__class__.FEATURES_INPUT_DIR = input_args.machine_features_input_dir
        self.__class__.DETECTIONS_OUTPUT_DIR = f"{input_args.detections_output_dir[:-1]}_{get_current_date()}/"

        self.__class__.GCS_MACHINE_FEATURES_OUTPUT_PATH = f"gs://augury-datasets-research/rapid_cliff_enhancements/machine_features/{calendar.timegm(datetime.now().timetuple())}"
        self.__class__.MACHINE_FEATURES_TRIGGER_FILE_PATH = os.path.join(WORK_DIR , "rapid_cliff_machine_filter_2020-09-01_2021-02-15.csv")

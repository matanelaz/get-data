import os
import calendar
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
        self.__class__.FEATURES_INPUT_PUBSUB = getattr(input_args, 'machine_features_input_pubsub', None)
        self.__class__.FEATURES_INPUT_DIR = getattr(input_args, 'machine_features_input_dir', None)
        self.__class__.DETECTIONS_OUTPUT_DIR = f"{getattr(input_args, 'detections_output_dir', '')[:-1]}_{get_current_date()}/"

        self.__class__.GCS_MACHINE_FEATURES_OUTPUT_PATH = os.path.join(getattr(input_args, 'machine_features_output_dir_parent' ,''), str(calendar.timegm(datetime.now().timetuple())))
        self.__class__.MACHINE_FEATURES_TRIGGER_FILE_PATH = os.path.join(WORK_DIR, getattr(input_args, 'triggers_file_path', ''))

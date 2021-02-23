from pathlib import Path


from src.utils.date_functions import get_current_date

ROOT_DIR = Path(__file__).parent.parent


class Config:

    BEAM_PIPELINE_ARGS: dict
    FEATURES_INPUT_PUBSUB: str
    FEATURES_INPUT_DIR: str
    DETECTIONS_OUTPUT_DIR: str

    def __init__(self, input_args, beam_pipeline_args):

        self.__class__.BEAM_PIPELINE_ARGS = beam_pipeline_args
        self.__class__.FEATURES_INPUT_PUBSUB = input_args.machine_features_input_pubsub
        self.__class__.FEATURES_INPUT_DIR = input_args.machine_features_input_dir
        self.__class__.DETECTIONS_OUTPUT_DIR = f"{input_args.detections_output_dir[:-1]}_{get_current_date()}/"


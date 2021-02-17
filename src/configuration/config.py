import os
from pathlib import Path

import yaml

from utils.date_functions import get_current_date

ROOT_DIR = Path(__file__).parent.parent


class Config:
    PIPELINE_NAME: str
    PROJECT_PATH: str
    PIPELINE_PATH: str

    MONGODB_USERNAME: str
    MONGODB_PASS: str

    BEAM_PIPELINE_ARGS: dict
    FEATURES_INPUT_PUBSUB: str
    FEATURES_INPUT_DIR: str
    DETECTIONS_OUTPUT_DIR: str

    def __init__(self, pipeline_class, input_args, beam_pipeline_args):
        self.__class__.PIPELINE_NAME = f"{pipeline_class.__name__}.pkl"
        self.__class__.PROJECT_PATH = ROOT_DIR
        self.__class__.PIPELINE_PATH = os.path.join(ROOT_DIR, 'pipeline', self.__class__.PIPELINE_NAME)

        mongodb_credentials = self.__read_yaml('mongodb_credentials.yaml')
        self.__class__.MONGODB_USERNAME = mongodb_credentials['username']
        self.__class__.MONGODB_PASS = mongodb_credentials['password']

        self.__class__.BEAM_PIPELINE_ARGS = beam_pipeline_args
        self.__class__.FEATURES_INPUT_PUBSUB = input_args.machine_features_input_pubsub
        self.__class__.FEATURES_INPUT_DIR = input_args.machine_features_input_dir
        self.__class__.DETECTIONS_OUTPUT_DIR = f"{input_args.detections_output_dir[:-1]}_{get_current_date()}/"

    @staticmethod
    def __read_yaml(yaml_file_name):
        config_dir = os.path.dirname(__file__)
        with open(os.path.join(config_dir, yaml_file_name)) as fp:
            return yaml.safe_load(fp)
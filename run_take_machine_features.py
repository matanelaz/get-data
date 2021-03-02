import argparse
import logging

from src.beam_api import Beam_API
from src.configuration.config import Config

def init_parser():
    parser = argparse.ArgumentParser()
    inputs = parser.add_argument_group()
    inputs.add_argument('--triggers-file-path',
                        help='A path in GCS / local folder containing machine filter csv')
    inputs.add_argument('--machine-features-output-dir-parent',
                        help='A path in GCS / local folder to the parent of the output-path')
    return parser


if __name__ == '__main__':
    parser = init_parser()
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    input_args, beam_pipeline_args = parser.parse_known_args()
    Config(
        input_args=input_args,
        beam_pipeline_args=beam_pipeline_args
    )
    Beam_API().run_take_machine_features()
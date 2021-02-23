import logging

from src.configuration.config import Config
from src.db_api.beam_api import Beam_API
from src.utils.argparser import init_parser



if __name__ == '__main__':
    parser = init_parser()
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    input_args, beam_pipeline_args = parser.parse_known_args()
    Config(
        input_args=input_args,
        beam_pipeline_args=beam_pipeline_args
    )
    Beam_API().run()
import argparse


def init_parser():
    parser = argparse.ArgumentParser()

    inputs = parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument('--machine-features-input-dir',
                        help='A path in GCS / local folder containing machine features for inference')
    inputs.add_argument('--machine-features-input-pubsub',
                        help='A PubSub topic containing machine features for inference')

    outputs = parser.add_mutually_exclusive_group(required=True)
    outputs.add_argument('--detections-output-dir',
                         help='A path in GCS / local folder to store detections in')
    outputs.add_argument('--detections-output-pubsub',
                         help='A PubSub topic to post detections in')
    return parser

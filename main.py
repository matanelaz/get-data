import calendar
from datetime import datetime

import pandas as pd

from utils.pipeline import fetch_features_to_csv, output_to_one_file


GCS_BUCKET_PATH = 'gs://augury-datasets-research'
# GCS_OUTPUT_PATH = f'{GCS_BUCKET_PATH}/too-rapid-debug/logs_analysis/{str(calendar.timegm(datetime.now().timetuple()))}_between_70_100/'
GCS_OUTPUT_PATH = f'{GCS_BUCKET_PATH}/too-rapid-debug/machine_features_time_offset/{str(calendar.timegm(datetime.now().timetuple()))}/'
# TRIGGERS_LOCAL_PATH = 'C:/Users/koren/work_dir/too_rapid/machine_filter_between_70_100.csv'
# TRIGGERS_LOCAL_PATH = 'C:/Users/koren/work_dir/too_rapid/machine_filter_unittest.csv'
TRIGGERS_LOCAL_PATH = None
TRIGGERS_DF = pd.DataFrame([
    {'machine_id': '5eea68b3b0f53300018f55ce', 'start': 1630457801, 'end': 1630458201, 'session_ids': '["612edc40f23e77071b4f6255"]'},
    {'machine_id': '5d74efc2550b33000173c651', 'start': 1630457801, 'end': 1630458201, 'session_ids': '["612edca03a390652748e7cc4"]'},
    ])


"""
### Example ###
GCS_BUCKET_PATH = 'gs://augury-datasets-research'
GCS_OUTPUT_PATH = f'{GCS_BUCKET_PATH}/too-rapid-debug/logs_analysis/{str(calendar.timegm(datetime.now().timetuple()))}_between_70_100/'

TRIGGERS_LOCAL_PATH = 'C:/Users/koren/work_dir/too_rapid/machine_filter.csv'
    or
TRIGGERS_DF = pd.DataFrame([
    {'machine_id': '5d74f589550b33000173c7de', 'start': 1627146800, 'end': 1627156800},
    {'machine_id': '5d74f589550b33000173c7de', 'start': 1628146800, 'end': 1628156800},
    ])

"""


def main(gcs_output_path, triggers_local_path, triggers_df):
    if triggers_df is None:
        triggers_df = pd.read_csv(triggers_local_path)

    if not gcs_output_path.endswith('/'):
        gcs_output_path += '/'

    fetch_features_to_csv(triggers_df, gcs_output_path)

    output_to_one_file(gcs_output_path)


if __name__ == '__main__':
    main(
        gcs_output_path=GCS_OUTPUT_PATH,
        triggers_local_path=TRIGGERS_LOCAL_PATH,
        triggers_df=TRIGGERS_DF
    )

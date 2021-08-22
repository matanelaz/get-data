import calendar
from datetime import datetime

import pandas as pd

from utils.pipeline import fetch_features_to_csv, output_to_one_file


TRIGGERS_LOCAL_PATH = 'C:/Users/koren/work_dir/too_rapid/machine_filter.csv'
TRIGGERS_DF = None

GCS_OUTPUT_PATH = f'gs://augury-datasets-research/too-rapid-debug/logs_analysis/{str(calendar.timegm(datetime.now().timetuple()))}/'


def main():
    if TRIGGERS_DF is not None:
        triggers_df = TRIGGERS_DF
    else:
        triggers_df = pd.read_csv(TRIGGERS_LOCAL_PATH)
    fetch_features_to_csv(triggers_df, GCS_OUTPUT_PATH)
    output_to_one_file(GCS_OUTPUT_PATH)


if __name__ == '__main__':
    main()

import pandas as pd


DEFAULT_PIPELINE_OPTION_ARGS = [
    '--runner', 'dataflow',
    '--setup_file', './setup.py',
    '--worker_machine_type', 'n1-standard-32',
    '--max_num_workers', '100'
]


def map_time_range(x):
    import datetime
    from augury_beam.io.feature_pool import MachineTimeRange

    return MachineTimeRange(start=datetime.datetime.fromtimestamp(x['start']),
                            end=datetime.datetime.fromtimestamp(x['end']),
                            machine_id=x['machine_id'])


def convert_to_csv_format(df: pd.DataFrame):
    rows = []
    if df is not None:
        for record in df.values.tolist():
            row = ",".join(record)
            rows.append(row)
    return rows


def convert_to_csv_format_with_header(df: pd.DataFrame):
    df = df[sorted(df.columns)]
    rows = [",".join(list(df.columns))]
    return rows + convert_to_csv_format(df)

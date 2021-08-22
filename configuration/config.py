import pandas as pd


class Config:

    TRIGGERS_DF: pd.DataFrame
    OUTPUT_DIR: str

    def __init__(self, triggers_df, output_dir, features_list=None):

        self.__class__.TRIGGERS_DF = triggers_df
        self.__class__.FEATURES_LIST = features_list
        self.__class__.OUTPUT_DIR = output_dir

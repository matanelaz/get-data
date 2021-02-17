import datetime

import apache_beam as beam
from augury_data_utilities.helpers.machine_features import MachineFeaturesEnrichment
import pandas as pd

from db_api.utils.parameters import feature_list


def convert_to_csv(mfg):
    df = mfg['df']
    rows = []
    for record in df.values.tolist():
        row = ",".join(record)
        rows.append(row)
    return rows


class DetectorFeatures(beam.DoFn):
    def process(self, mfg, **kwargs):
        features = {}
        features['machine_id'] = mfg.machine.machine_id
        features['recorded_at'] = datetime.datetime.utcfromtimestamp(mfg.grouping_time.seconds)
        features['session_id'] = mfg.grouping_id
        features['parsed_features'] = MachineFeaturesEnrichment(mfg).parse_machine_features(filter_invalid=False)
        yield features


class FlatFeatures(beam.DoFn):
    def process(self, mfg, **kwargs):
        feature_vals = []
        m_id = mfg['machine_id']
        recorded_at = mfg['recorded_at']
        session_id = mfg['session_id']

        for k in mfg['parsed_features'].keys():
            c_id, bearing, plane = k.component_id, k.bearing_num, k.plane
            d = {"machine_id": m_id, "recorded_at": recorded_at, "session_id": session_id, "component_id": c_id,
                 "bearing": bearing, "plane": plane}
            vals = mfg['parsed_features'][k]
            for col in feature_list:
                if col not in d.keys():
                    d[col] = vals.get(col, None)
            feature_vals.append(d)
        df = pd.DataFrame(feature_vals)[feature_list].fillna('').astype(str)
        mfg['df'] = df[df['vibration_session_machine_on'] == '1']
        if mfg['df'].shape[0] == 0:
            mfg['df'] = None
        yield mfg


class DetectionTransform(beam.PTransform):

    def __init__(self,
                 detector_name: str,
                 batch_mode: bool
                 ):
        super(DetectionTransform, self).__init__()
        self.batch_mode = batch_mode
        self.detector_name = detector_name

    def expand(self, machine_features):
        detector_features = (machine_features |
                             'MachineFeatures to DetectorFeatures' >> beam.ParDo(DetectorFeatures()))
        flat_features = (detector_features | "Flat features to be " >> beam.ParDo(
            FlatFeatures()) | "filter off sessions" >> beam.Filter(lambda mfg: mfg['df'] is not None))
        csv_format = flat_features | "convert_to_csv_format" >> beam.FlatMap(convert_to_csv)
        return csv_format

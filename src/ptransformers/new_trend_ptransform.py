import apache_beam as beam
import pandas as pd

from src.ptransformers.utils.detector_features import Detector_Features
from src.ptransformers.utils.parameters import new_trand_feature_list


def convert_to_csv(mfg):
    df = mfg['df']
    rows = []
    for record in df.values.tolist():
        row = ",".join(record)
        rows.append(row)
    return rows


class _Flat_Features(beam.DoFn):
    def process(self, mfg, **kwargs):
        feature_vals = []
        m_id = mfg['machine_id']
        recorded_at = mfg['recorded_at']
        session_id = mfg['session_id']
        is_servo = mfg['is_servo']

        for k in mfg['parsed_features'].keys():
            c_id, bearing, plane = k.component_id, k.bearing_num, k.plane
            d = {"machine_id": m_id, "is_servo": is_servo, "recorded_at": recorded_at, "session_id": session_id, "component_id": c_id,
                 "bearing": bearing, "plane": plane}
            vals = mfg['parsed_features'][k]
            for col in new_trand_feature_list:
                if col not in d.keys():
                    d[col] = vals.get(col, None)
            feature_vals.append(d)
        df = pd.DataFrame(feature_vals)[new_trand_feature_list].fillna('').astype(str)
        mfg['df'] = df[df['vibration_session_machine_on'] == '1']
        if mfg['df'].shape[0] == 0:
            mfg['df'] = None
        yield mfg


class New_Trend_PTransform(beam.PTransform):

    def __init__(self,
                 detector_name: str,
                 batch_mode: bool
                 ):
        super(New_Trend_PTransform, self).__init__()
        self.batch_mode = batch_mode
        self.detector_name = detector_name

    def expand(self, machine_features):
        detector_features = (machine_features |
                             'MachineFeatures to DetectorFeatures' >> beam.ParDo(Detector_Features()))
        flat_features = (detector_features | "Flat features to be " >> beam.ParDo(
            _Flat_Features()) | "filter off sessions" >> beam.Filter(lambda mfg: mfg['df'] is not None))
        csv_format = flat_features | "convert_to_csv_format" >> beam.FlatMap(convert_to_csv)
        return csv_format

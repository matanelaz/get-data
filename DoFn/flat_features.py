from typing import Union

import apache_beam
import pandas as pd
from ad_pipeline.data_models.detector_features import DetectorFeatures


class Flat_Features(apache_beam.DoFn):

    def __init__(self):
        super().__init__()

    def process(self, detector_features: Union[DetectorFeatures, None], **kwargs):
        if detector_features is not None:
            flatted_features = []

            meta_data = {
                'machine_id': detector_features.machine_id,
                'trigger_time': detector_features.trigger_time,
                'session_id': detector_features.session_id,
            }

            for sampling_point in detector_features.features.keys():
                flatted_features_row = meta_data.copy()
                flatted_features_row.update({
                    'component_id': sampling_point.component_id,
                    'bearing': sampling_point.bearing_num,
                    'plane': sampling_point.plane,
                })

                for feature in detector_features.features[sampling_point]:
                    if feature not in flatted_features_row:
                        flatted_features_row[feature] = detector_features.features[sampling_point].get(feature)
                flatted_features.append(flatted_features_row)
            df = pd.DataFrame(flatted_features).fillna('').astype(str)
            df = df[df['vibration_session_machine_on'] == '1']
            yield df if len(df) else None
        else:
            yield None
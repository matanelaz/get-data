import pandas as pd
import apache_beam as beam


class Flat_Features(beam.DoFn):

    def __init__(self, features_list, *unused_args, **unused_kwargs):
        super().__init__(*unused_args, **unused_kwargs)
        self._features_list = features_list

    def process(self, mfg, **kwargs):
        flatted_features = []
        machine_id = mfg['machine_id']
        recorded_at = mfg['recorded_at']
        session_id = mfg['session_id']

        for unflatted_key in mfg['parsed_features'].keys():
            flatted_features_row = {
                'machine_id': machine_id,
                'component_id': unflatted_key.component_id,
                'is_component_motor': mfg['is_component_motor_map'][unflatted_key.component_id],
                'bearing': unflatted_key.bearing_num,
                'plane': unflatted_key.plane,
                'recorded_at': recorded_at,
                'session_id': session_id,
            }

            for parsed_feature in self._features_list:
                if parsed_feature not in flatted_features_row:
                    flatted_features_row[parsed_feature] = mfg['parsed_features'][unflatted_key].get(parsed_feature)
            flatted_features.append(flatted_features_row)
        df = pd.DataFrame(flatted_features, columns=self._features_list).fillna('').astype(str)
        df = df[df['vibration_session_machine_on'] == '1']
        yield df if len(df) else None
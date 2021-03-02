import datetime
import apache_beam
from augury_data_utilities.helpers.component_helper import ComponentType, ComponentHelper
from augury_data_utilities.helpers.machine_features import MachineFeaturesEnrichment
from augury_data_utilities.helpers.machine_helper import MachineHelper


class Detector_Features(apache_beam.DoFn):
    def process(self, mfg, **kwargs):
        features = {}
        features['machine_id'] = mfg.machine.machine_id
        features['recorded_at'] = datetime.datetime.utcfromtimestamp(mfg.grouping_time.seconds)
        features['session_id'] = mfg.grouping_id
        motor_component = MachineHelper.get_component_by_type(mfg.machine, ComponentType.MOTOR)
        features['is_servo'] = ComponentHelper.is_servo_motor(motor_component)
        features['parsed_features'] = MachineFeaturesEnrichment(mfg).parse_machine_features(filter_invalid=False)
        yield features
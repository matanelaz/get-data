import apache_beam
from ad_pipeline.data_models.detector_features import DetectorFeatures


class DetectorFeaturesBuilder(apache_beam.DoFn):

    def __init__(self, *unused_args, **unused_kwargs):
        super().__init__(*unused_args, **unused_kwargs)
        self.sessions = unused_args[0]

    def process(self, mfg, **kwargs):
        if not self.sessions:
            yield DetectorFeatures(mfg)
        elif mfg.grouping_id in self.sessions:
            yield DetectorFeatures(mfg)
        else:
            yield None

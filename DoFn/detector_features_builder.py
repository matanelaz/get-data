import apache_beam
from ad_pipeline.data_models.detector_features import DetectorFeatures


class DetectorFeaturesBuilder(apache_beam.DoFn):
    def process(self, mfg, **kwargs):
        yield DetectorFeatures(mfg)
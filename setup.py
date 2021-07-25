import setuptools
data_common_branch = "1.0.3"

setuptools.setup(
    name='get-data',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "apache-beam",
        "google-api-core",
        "google-cloud-pubsub",
        "python-dateutil",
        "numpy",
        "tensorflow",
        "scikit-learn",
        "shap",
        "cassandra-driver",
        "augury-beam @ git+https://github.com/augurysys/data-common.git@{}#egg=augury-beam-0.0.1#subdirectory=python/augury_beam".format(data_common_branch),
        "trend-storage @ git+https://github.com/augurysys/data-common.git@{}#egg=trend-storage-0.1.0#subdirectory=python/trend_storage".format(data_common_branch),
        # "augury-proto @ git+https://github.com/augurysys/data-common.git#subdirectory=python/augury_proto",
    ],
)

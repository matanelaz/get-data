import setuptools
data_common_branch = "master"

setuptools.setup(
    name='src',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "apache-beam==2.25.0",
        "google-api-core==1.22.2",
        "google-cloud-pubsub==1.7.0",
        "python-dateutil",
        "numpy==1.16.3",
        "tensorflow",
        "scikit-learn==0.23.1",
        "shap==0.35.0",
        "cassandra-driver==3.17.0",
        "augury-beam @ git+https://github.com/augurysys/data-common.git@{}#egg=augury-beam-0.0.1#subdirectory=python/augury_beam".format(data_common_branch),
        "trend-storage @ git+https://github.com/augurysys/data-common.git@{}#egg=trend-storage-0.1.0#subdirectory=python/trend_storage".format(data_common_branch),
        "augury-proto @ git+https://github.com/augurysys/data-common.git#subdirectory=python/augury_proto",
    ],
)

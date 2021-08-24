import setuptools
data_common_branch = "1.0.3"
ad_brain_tag = "1.2.0"

setuptools.setup(
    name='get-data',
    version='0.0.0',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        f"anomaly-detection-brain @ git+https://github.com/augurysys/anomaly-detection-brain.git@{ad_brain_tag}",
    ],
)

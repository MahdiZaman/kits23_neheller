from setuptools import find_namespace_packages
from setuptools import setup

setup(
    name='kits23',
    packages=find_namespace_packages(include=["kits23*"]),
    version='0.1.3',
    description='',
    zip_safe=False,
    install_requires=[
        'numpy',
        'scipy',
        'scikit-image',
        'opencv-python',
        'nibabel',
        'requests',
        'argparse',
        'tqdm',
        "pytest",
        # 'Surface-Distance-Based-Measures @ git+https://github.com/deepmind/surface-distance.git',    # Issues with surface-distance-based-measures. installing this manually
        # git clone https://github.com/deepmind/surface-distance.git
        # pip install surface-distance/
        'SimpleITK',
        "batchgenerators"
    ],
    entry_points={
        'console_scripts': [
            'kits23_download_data = kits23.entrypoints:download_data_entrypoint',
            'kits23_compute_metrics = kits23.evaluation.entry_point:main'
        ]
    },
)

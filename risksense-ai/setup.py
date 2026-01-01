# setup.py
# Python packaging and installation script for RiskSense AI
from setuptools import setup, find_packages

setup(
    name="risksense-ai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "pyyaml",
    ],
)
# --- IGNORE ---
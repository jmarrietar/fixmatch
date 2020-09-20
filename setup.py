from setuptools import setup, find_packages
from os import path

REQUIRED_PACKAGES = ["tensorflow-gpu==1.14.0"]

setup(
    name="fixmatch",
    version="1.2",
    license='Apache License 2.0',
    description="fixmatch",
    packages=find_packages(),
)
#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="rootlib",
    version="1.0",
    packages=find_packages() + ["submodules.mylib"],
    include_package_data=True,
)

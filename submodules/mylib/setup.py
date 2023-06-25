#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="mylib",
    version="1.0",
    packages=find_packages() + ["submodules"],
    include_package_data=True,
)

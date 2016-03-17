#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="py-ps-config",
    version="1.0",
    description="Management utilities for config files.",
    author="Jhonny Bravo",
    author_email="sanfranceshika5@gmail.com",
    url="https://github.com/JhonnyBravo/py-ps-config.git",
    packages=find_packages(),
    long_description=long_description,
    entry_points={
        "console_scripts": [
            "get_option=ps_config.bin.get_option:main",
            "get_section_list=ps_config.bin.get_section_list:main",
            "remove_option=ps_config.bin.remove_option:main",
            "remove_section=ps_config.bin.remove_section:main",
            "set_option=ps_config.bin.set_option:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)

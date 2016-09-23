#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except Exception:
    long_description = ""

setup(
    name="py-ps-config",
    version="1.1",
    description="Management utilities for config files.",
    author="Jhonny Bravo",
    author_email="sanfranceshika5@gmail.com",
    url="https://github.com/JhonnyBravo/py-ps-config.git",
    packages=find_packages(),
    long_description=long_description,
    entry_points={
        "console_scripts": [
            "get_config_option_list=ps_config.bin.get_config_option_list:main",
            "get_config_option_value=ps_config.bin.get_config_option_value:main",
            "get_config_section_list=ps_config.bin.get_config_section_list:main",
            "remove_config_option=ps_config.bin.remove_config_option:main",
            "remove_config_section=ps_config.bin.remove_config_section:main",
            "set_config_option=ps_config.bin.set_config_option:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)

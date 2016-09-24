#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except Exception:
    long_description = ""

setup(
    name="py-ps-json",
    version="1.0",
    description="Management utilities for json files.",
    author="Jhonny Bravo",
    author_email="sanfranceshika5@gmail.com",
    url="https://github.com/JhonnyBravo/py-ps-json.git",
    packages=find_packages(),
    long_description=long_description,
    entry_points={
        "console_scripts": [
            "get_json_key_list=ps_json.bin.get_json_key_list:main",
            "get_json_key_value=ps_json.bin.get_json_key_value:main",
            "remove_json_key=ps_json.bin.remove_json_key:main",
            "set_json_key=ps_json.bin.set_json_key:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)

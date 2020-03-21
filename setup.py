#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="napari-dv",
    version="0.2.3",
    author="Talley Lambert",
    author_email="talley.lambert@gmail.com",
    maintainer="Talley Lambert",
    maintainer_email="talley.lambert@gmail.com",
    license="MIT",
    url="https://github.com/tlambert03/napari-dv",
    description="Deltavision/MRC file reader for napari",
    long_description=read("README.rst"),
    py_modules=["napari_dv"],
    python_requires=">=3.6",
    install_requires=["napari>=0.2.11", "mrc>=0.1.5", "pluggy>=0.13.1"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"napari.plugin": ["dv_reader = napari_dv"]},
)

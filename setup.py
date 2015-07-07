#!/usr/bin/env python
# encoding: utf-8
from __future__ import absolute_import, print_function
import os

from setuptools import setup, find_packages


__version__ = '0.1alpha2'
__author__ = 'Dmitry Orlov <me@mosquito.su>'


setup(
    name='cm',
    version=__version__,
    author=__author__,
    author_email='me@mosquito.su',
    license="MIT",
    description="Commandline Magic",
    platforms="all",
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python',
    ],
    long_description=open('README.rst').read(),
    packages=find_packages(),
)

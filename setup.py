#!/usr/bin/env python

from setuptools import setup

setup(
  name                  = 'sdist_ignores_include_package_data',
  version               = '0.1',
  packages              = ['demonstrator'],
  include_package_data  = True,
)
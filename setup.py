#!/usr/bin/env python

from setuptools import setup

setup(
  name                  = 'sdist_ignores_include_package_data',
  version               = '0.1',
  packages              = ['demonstrator'],
  package_dir           = {'demonstrator': '.'},
  include_package_data  = True,
  zip_safe              = False,
)
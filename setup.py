#!/usr/bin/env python

from setuptools import setup

setup(
  name                  = 'sdist_ignores_include_package_data',
  version               = '0.1',
  namespace_packages    = ['Products'],
  packages              = ['Products.demonstrator'],
  package_dir           = {'Products.demonstrator': '.'},
  include_package_data  = True,
  zip_safe              = False,
)
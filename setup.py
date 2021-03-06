#!/usr/bin/env python
# encoding: utf-8

import setuptools
from setuptools import setup

setup(name='cowpy',
      description="A cowsay clone for python in one file.",
      author="Jeff Buttars",
      author_email="jeffbuttars@gmail.com",
      url="https://github.com/jeffbuttars/cowpy",
      version='1.0.1',
      packages=['cowpy'],
      scripts=['scripts/cowpy']
      )

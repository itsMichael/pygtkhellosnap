# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(
    name='pygtkhellosnap',
    version="1.0",
    packages=find_packages(),
    include_package_data=False,
    install_requires=[],
    entry_points = {
        'pygtkhellosnap': ['pygtkhellosnap=pygtkhellosnap:main'],
    }
)

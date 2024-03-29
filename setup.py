#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of easyNav-pi-main.
# https://github.com/easyNav/easyNav-pi-main.git

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Joel Tong me@joeltong.org


from setuptools import setup, find_packages
from easyNav_pi_main import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='easyNav-pi-main',
    version=__version__,
    description='Main execution function for easyNav',
    long_description='''
Main execution function for easyNav
''',
    keywords='easyNav navigation ',
    author='Joel Tong',
    author_email='me@joeltong.org',
    url='https://github.com/easyNav/easyNav-pi-main.git',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy",
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'easyNav-pi-main=easyNav_pi_main.cli:main',
        ],
    },
)

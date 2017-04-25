#!/usr/bin/env python

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='pdje',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    license='Apache License 2.0',
    description='A simple Django app to control an email system',
    long_description=README,
    url='https://0xdc.io/',
    author='Daniel Cordero',
    author_email='me@0xdc.io',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache License 2.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'passlib',
    ],
)

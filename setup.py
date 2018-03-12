#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='PythonKit',
    version='0.0.1',
    url='https://github.com/htwenning/python_kit',
    license='BSD',
    author='wenning',
    author_email='ht.wenning@foxmail.com',
    description='Write grpc application like Flask.',
    packages=['python_kit'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'enum34==1.1.6',
        'futures==3.2.0',
        'grpcio==1.10.0',
        'grpcio-tools==1.10.0',
        'protobuf==3.5.2',
        'six==1.11.0',
    ],
)

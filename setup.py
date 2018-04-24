#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Santosh Philip",
    author_email='santosh_philip@yahoo.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="""Implements the equations from Ashrae Fundamentals 2009""",
    entry_points={
        'console_scripts': [
            'pyclearsky=pyclearsky.cli:main',
        ],
    },
    install_requires=requirements,
    license="Mozilla Public License 2.0 (MPL 2.0)",
    long_description='\n\n' + readme, # + '\n\n' + history,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='pyclearsky',
    name='pyclearsky',
    packages=find_packages(include=['pyclearsky']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/santoshphilip/pyclearsky',
    version='version='0.2.13'',
    zip_safe=False,
)

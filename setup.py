#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from __future__ import absolute_import, print_function

import io
import re
from glob import glob
from os.path import basename, dirname, join, splitext

from setuptools import find_packages, setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name="marshmallow_configparser",
    version='0.3.3',
    license='MIT',
    description="ConfigParser meets marshmallow",
    long_description='%s\n%s' % (
        re.compile(
            '^' + re.escape('[//]: # (start-badges)') + '.*^'
            + re.escape('[//]: # (end-badges)'), re.M | re.S
        ).sub('', read('README.md')),
        # re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
        ''
    ),
    # In the future this will correctly render Markdown on PyPi:
    # long_description_content_type='text/markdown',
    author="Tomislav Adamic",
    author_email="tomislav.adamic@gmail.com",
    url="https://github.com/tadams42/marshmallow_configparser",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
        "congfiparser", "marshmallow"
    ],
    # List run-time dependencies HERE.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'marshmallow'
    ],
    # List additional groups of dependencies HERE (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev]
    extras_require={
        'docs': [
            'sphinx >= 1.4',
            'sphinx_rtd_theme',
            'm2r >= 0.1.14',
        ],
        'dev': [
            'pycodestyle',
            'yapf',
            'bumpversion',
            'isort',
            'check-manifest',
            'pylint',

            # IPython stuff
            'ipython',

            # Docs and viewers
            'sphinx',
            'sphinx_rtd_theme',
            'm2r',

            # py.test stuff
            'pytest >= 3.0.0',
            'pytest-sugar',
            'pytest-cov',
            'pytest-mock',

            'coverage',
            'factory-boy',
            'faker',
        ]
    }
)

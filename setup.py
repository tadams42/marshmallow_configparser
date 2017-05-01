#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
import sys
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

NEEDS_PYTEST = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
PYTEST_RUNNER = ['pytest-runner'] if NEEDS_PYTEST else []


SETUP_REQUIREMENTS = [
    # ... (other setup requirements)
] + PYTEST_RUNNER

INSTALL_REQUIREMENTS = [
    'marshmallow'
]

DEV_REQUIREMENTS = [
    'pycodestyle >= 2.0.0',  # (formerly called pep8)
    'mccabe >= 0.5.0',
    'pylint >= 1.6.0',
    'yapf >= 0.11.0',
    'bumpversion >= 0.5.3',

    # IPython stuff
    'ipython >= 5.0.0',
    'jupyter >= 1.0.0',
    'ipdb >= 0.10.0',

    # Docs and viewers
    'Sphinx >= 1.4.0',
    'sphinx_rtd_theme >= 0.1.9',
    'restview >= 2.6.0',

    # Profiling
    'snakeviz >= 0.4.0',
    'pyprof2calltree >= 1.4.0',

    # py.test things usefull only when manually running tests
    'pytest-colordots >= 0.1.0',
    'colored-traceback >= 0.2.0',
]

TEST_REQUIREMENTS = [
    'pytest >= 3.0.0',
    'pytest-spec >= 1.0.0',
    'pytest-cov >= 2.3.0',
    'check-manifest >= 0.33.0',
    'coverage >= 4.2.0',
]


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name="marshmallow_configparser",
    version='0.1.0',
    license='MIT',
    description="ConfigParser meets marshmallow",
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author="Tomislav Adamic",
    author_email="tomislav.adamic@gmail.com",
    url="https://github.com/tadamic/marshmallow_configparser",
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
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
        "congiparser", "marshmallow"
    ],
    setup_requires=SETUP_REQUIREMENTS,
    # List run-time dependencies HERE.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=INSTALL_REQUIREMENTS,
    # List additional groups of dependencies HERE (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev]
    extras_require={
        'dev': list(
            set(DEV_REQUIREMENTS).union(set(TEST_REQUIREMENTS))
        )
    },
    tests_require=TEST_REQUIREMENTS,
)

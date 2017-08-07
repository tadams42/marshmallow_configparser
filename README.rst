Overview
========

.. start-badges

|version| |license| |travis| |docs| |requirements| |codacy_grade| |codacy_coverage| |wheel| |python_versions|

.. |version| image:: https://img.shields.io/pypi/v/marshmallow-configparser.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/sokoenginepy/

.. |license| image:: https://img.shields.io/pypi/l/marshmallow-configparser.svg
    :alt: License
    :target: https://opensource.org/licenses/MIT

.. |wheel| image:: https://img.shields.io/pypi/wheel/marshmallow-configparser.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/sokoenginepy/

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/marshmallow-configparser.svg
    :alt: Supported versions
    :target: https://pypi.org/project/sokoenginepy/

.. |python_implementations| image:: https://img.shields.io/pypi/implementation/marshmallow-configparser.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/marshmallow-configparser/

.. |travis| image:: https://travis-ci.org/tadams42/marshmallow_configparser.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/tadams42/marshmallow_configparser

.. |docs| image:: https://readthedocs.org/projects/marshmallow-configparser/badge/?style=flat
    :alt: Documentation Status
    :target: http://marshmallow-configparser.readthedocs.io/en/latest/

.. |requirements| image:: https://requires.io/github/tadams42/marshmallow_configparser/requirements.svg?branch=master
     :alt: Requirements Status
     :target: https://requires.io/github/tadams42/marshmallow_configparser/requirements/?branch=master

.. |codacy_grade| image:: https://api.codacy.com/project/badge/Grade/ad3aa55e2fc74a37a1b1ac2fb59f6dc0
    :alt: Codacy grade
    :target: https://www.codacy.com/app/tadams42/marshmallow_configparser?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tadams42/marshmallow_configparser&amp;utm_campaign=Badge_Grade

.. |codacy_coverage| image:: https://api.codacy.com/project/badge/Coverage/ad3aa55e2fc74a37a1b1ac2fb59f6dc0
    :alt: Codacy coverage
    :target: https://www.codacy.com/app/tadams42/marshmallow_configparser?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tadams42/marshmallow_configparser&amp;utm_campaign=Badge_Coverage

.. end-badges

Ever wanted to load plain ``.ini`` config files and then validate loaded config?

Ever wanted to load config from multiple locations (``/etc/appconfig.conf``, ``~/.appconfig.conf``) into single object and then validate that?

Worry no more!

Python's `ConfigParser`_ met `marshmallow`_ and now they get along just fine - without any JSON in sight to spoil the fun.


Installation
============

::

    pip install marshmallow_configparser


Example
=======

Having config file ``/tmp/example_config.conf`` looking like this:

.. code-block:: ini

    [Section1]
    option1 = mandatory string
    option2 = optional string
    option3 = 42
    option4 = 24

    [Section2]
    option1 = mandatory string
    option2 = optional string
    option3 = 42
    option4 = 24

And wanting to load it into our config object:

.. code-block:: python

    class ConfigObject(object):
        MANDATORY_STRING1 = None
        OPTIONAL_STRING1 = None
        MANDATORY_INTEGER1 = None
        OPTIONAL_INTEGER1 = None
        MANDATORY_STRING2 = None
        OPTIONAL_STRING2 = None
        MANDATORY_INTEGER2 = None
        OPTIONAL_INTEGER2 = None


We can define `marshmallow`_ schema:

.. code-block:: python

    from marshmallow.validate import Range

    from marshmallow_configparser import (ConfigBoolean, ConfigInteger,
                                          ConfigParserSchema, ConfigString,
                                          IsNotBlank)

    class ConfigSchema(ConfigParserSchema):
        class Meta:
            model = ConfigObject

        MANDATORY_STRING1 = ConfigString(
            section='Section1', load_from='option1', dump_to='option1',
            validate=[IsNotBlank()]
        )
        OPTIONAL_STRING1 = ConfigString(
            section='Section1', load_from='option2', dump_to='option2',
        )
        MANDATORY_INTEGER1 = ConfigInteger(
            section='Section1', load_from='option3', dump_to='option3',
            validate=[Range(min=24, max=42)]
        )
        OPTIONAL_INTEGER1 = ConfigInteger(
            section='Section1', load_from='option4', dump_to='option4',
        )

        MANDATORY_STRING2 = ConfigString(
            section='Section2', load_from='option1', dump_to='option1',
            validate=[IsNotBlank()]
        )
        OPTIONAL_STRING2 = ConfigString(
            section='Section2', load_from='option2', dump_to='option2',
        )
        MANDATORY_INTEGER2 = ConfigInteger(
            section='Section2', load_from='option3', dump_to='option3',
            validate=[Range(min=24, max=42)]
        )
        OPTIONAL_INTEGER2 = ConfigInteger(
            section='Section2', load_from='option4', dump_to='option4',
        )


Which can then load and validate our config:

.. code-block:: python

    schema = ConfigSchema()
    obj, errors = schema.load(['/tmp/example_config.conf'])

In the end we have:

.. code-block:: python

    obj.__dict_

    {'MANDATORY_INTEGER1': 42,
     'MANDATORY_INTEGER2': 42,
     'MANDATORY_STRING1': 'mandatory string',
     'MANDATORY_STRING2': 'mandatory string',
     'OPTIONAL_INTEGER1': 24,
     'OPTIONAL_INTEGER2': 24,
     'OPTIONAL_STRING1': 'optional string',
     'OPTIONAL_STRING2': 'optional string'}

Instead of using convenience classes like ``ConfigString``, there are also
classes in ``marshmallow_configparser.fields`` module that expose full `marshmallow`_ API. Check the docs for details.

Documentation
=============

http://marshmallow-configparser.readthedocs.io/en/latest/index.html


.. _marshmallow: https://github.com/marshmallow-code/marshmallow
.. _ConfigParser: https://docs.python.org/3/library/configparser.html#configparser.ConfigParser

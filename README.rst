Overview
========

.. start-badges

|version| |license| |travis| |docs| |requirements| |codacy_grade| |codacy_coverage| |wheel| |python_versions|

.. |version| image:: https://img.shields.io/pypi/v/marshmallow_configparser.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/marshmallow_configparser

.. |license| image:: https://img.shields.io/pypi/l/marshmallow_configparser.svg
    :target: https://opensource.org/licenses/MIT
    :alt: License

.. |wheel| image:: https://img.shields.io/pypi/wheel/marshmallow_configparser.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/marshmallow_configparser

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/marshmallow_configparser.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/marshmallow_configparser

.. |python_implementations| image:: https://img.shields.io/pypi/implementation/marshmallow_configparser.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/marshmallow_configparser

.. |travis| image:: https://travis-ci.org/tadamic/marshmallow_configparser.svg
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/tadamic/marshmallow_configparser

.. |docs| image:: https://readthedocs.org/projects/marshmallow_configparser/badge/?style=flat
    :target: http://marshmallow_configparser.readthedocs.io/en/latest/
    :alt: Documentation Status

.. |requirements| image:: https://requires.io/github/tadamic/marshmallow_configparser/requirements.svg
     :target: https://requires.io/github/tadamic/marshmallow_configparser/requirements/
     :alt: Requirements Status

.. |codacy_grade| image:: https://api.codacy.com/project/badge/Grade/ad3aa55e2fc74a37a1b1ac2fb59f6dc0
    :target: https://www.codacy.com/app/tomislav-adamic/marshmallow_configparser
    :alt: Codacy code quality status

.. |codacy_coverage| image:: https://api.codacy.com/project/badge/Coverage/ad3aa55e2fc74a37a1b1ac2fb59f6dc0
    :target: https://www.codacy.com/app/tomislav-adamic/marshmallow_configparser
    :alt: Codacy code coverage

.. end-badges

Ever wanted to load plain ``.ini`` config files and then validate loaded config?

Ever wanted to load config from multiple locations (``/etc/appconfig.con``, ``~/.appconfig.conf``) into single object and then validate that?

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

Ann the end we have:

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

http://marshmallow_configparser.readthedocs.io/en/latest/index.html


.. _marshmallow: https://github.com/marshmallow-code/marshmallow
.. _ConfigParser: https://docs.python.org/3/library/configparser.html#configparser.ConfigParser

Overview
========

.. start-badges

.. end-badges

Ever wanted to load plain ``.ini`` config files and then validate loaded config?

Ever wanted to load config from multiple locations (``/etc/appconfig.con``, ``~/.appconfig.conf``) into single objcet and then validate that?

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

    from marshmallow_configparser import ConfigParserSchema, Integer, String
    from marshmallow_configparser import IsNotBlank

    class ConfigSchema(ConfigParserSchema):
        class Meta:
            model = ConfigObject

        MANDATORY_STRING1 = String(
            section='Section1',
            load_from='option1', dump_to='option1',
            allow_null=False, required=True, default='', missing='',
            validate=[IsNotBlank()]
        )
        OPTIONAL_STRING1 = String(
            section='Section1',
            load_from='option2', dump_to='option2',
            allow_null=False, required=False, default='', missing=''
        )
        MANDATORY_INTEGER1 = Integer(
            section='Section1',
            load_from='option3', dump_to='option3',
            allow_null=False, required=True, default=0, missing=0,
            validate=[Range(min=24, max=42)]
        )
        OPTIONAL_INTEGER1 = Integer(
            section='Section1',
            load_from='option4', dump_to='option4',
            allow_null=False, required=False, default=0, missing=0
        )

        MANDATORY_STRING2 = String(
            section='Section2',
            load_from='option1', dump_to='option1',
            allow_null=False, required=True, default='', missing='',
            validate=[IsNotBlank()]
        )
        OPTIONAL_STRING2 = String(
            section='Section2',
            load_from='option2', dump_to='option2',
            allow_null=False, required=False, default='', missing=''
        )
        MANDATORY_INTEGER2 = Integer(
            section='Section2',
            load_from='option3', dump_to='option3',
            allow_null=False, required=True, default=0, missing=0,
            validate=[Range(min=24, max=42)]
        )
        OPTIONAL_INTEGER2 = Integer(
            section='Section2',
            load_from='option4', dump_to='option4',
            allow_null=False, required=False, default=0, missing=0
        )

Which can then load and validate our config:

.. code-block:: python

    schema = ConfigSchema()
    obj, errors = schema.load(['/tmp/example_config.conf'])


Documentation
=============

TODO


.. _marshmallow: https://github.com/marshmallow-code/marshmallow
.. _ConfigParser: https://docs.python.org/3/library/configparser.html#configparser.ConfigParser

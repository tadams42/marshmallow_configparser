import os

import pytest
from marshmallow.validate import Range

from marshmallow_configparser import (ConfigInteger, ConfigParserSchema,
                                      ConfigString, Integer, IsNotBlank, String)

TESTS_ROOT_PATH = os.path.abspath(os.path.dirname(__file__))


class ConfigObject(object):
    pass


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


@pytest.fixture
def config_files():
    return [
        os.path.abspath(
            os.path.join(TESTS_ROOT_PATH, 'fixtures', 'complete.conf')
        )
    ]


@pytest.fixture
def config_schema():
    return ConfigSchema()


class ConfigStringConfigSchema(ConfigParserSchema):
    STRING_WITH_DEFAULT = ConfigString(
        section='Section1', default='default value',
        load_from='string_option_with_default',
        dump_to='string_option_with_default',
    )
    STRING_WITHOUT_DEFAULT = ConfigString(
        section='Section1',
        load_from='string_option_without_default',
        dump_to='string_option_without_default',
    )


@pytest.fixture
def config_string_config_schema():
    return ConfigStringConfigSchema()

@pytest.fixture
def string_option_doesnt_exist_file():
    return [
        os.path.abspath(
            os.path.join(TESTS_ROOT_PATH, 'fixtures',
                         'string_option_doesnt_exist.conf')
        )
    ]

@pytest.fixture
def string_option_is_blank_file():
    return [
        os.path.abspath(
            os.path.join(TESTS_ROOT_PATH, 'fixtures',
                         'string_option_is_blank.conf')
        )
    ]


class ConfigIntegerConfigSchema(ConfigParserSchema):
    INTEGER_WITH_DEFAULT = ConfigInteger(
        section='Section1', default=42,
        load_from='integer_option_with_default',
        dump_to='integer_option_with_default',
    )
    INTEGER_WITHOUT_DEFAULT = ConfigInteger(
        section='Section1',
        load_from='integer_option_without_default',
        dump_to='integer_option_without_default',
    )


@pytest.fixture
def config_integer_config_schema():
    return ConfigIntegerConfigSchema()

@pytest.fixture
def integer_option_doesnt_exist_file():
    return [
        os.path.abspath(
            os.path.join(TESTS_ROOT_PATH, 'fixtures',
                         'integer_option_doesnt_exist.conf')
        )
    ]

@pytest.fixture
def integer_option_is_blank_file():
    return [
        os.path.abspath(
            os.path.join(TESTS_ROOT_PATH, 'fixtures',
                         'integer_option_is_blank.conf')
        )
    ]

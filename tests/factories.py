import logging
import os

import pytest
from marshmallow.validate import Range

from marshmallow_configparser import Boolean
from marshmallow_configparser import ConfigParserSchema
from marshmallow_configparser import Integer
from marshmallow_configparser import IsNotBlank
from marshmallow_configparser import String

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

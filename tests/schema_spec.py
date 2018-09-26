import pytest
from marshmallow.exceptions import ValidationError

from marshmallow_configparser import is_marshmallow3


class DescribeConfigSchema:
    def it_loads_and_validates_config_file(self, config_files, config_schema):
        errors = None
        obj = None

        if is_marshmallow3():
            try:
                obj = config_schema.load(config_files)
            except ValidationError as e:
                errors = e.messages
        else:
            obj, errors = config_schema.load(config_files)

        assert not errors
        assert obj.MANDATORY_STRING1 == 'mandatory string'
        assert obj.OPTIONAL_STRING1 == 'optional string'
        assert obj.MANDATORY_INTEGER1 == 42
        assert obj.OPTIONAL_INTEGER1 == 24
        assert obj.MANDATORY_STRING2 == 'mandatory string'
        assert obj.OPTIONAL_STRING2 == 'optional string'
        assert obj.MANDATORY_INTEGER2 == 42
        assert obj.OPTIONAL_INTEGER2 == 24

    def it_dumps_config_object_to_ini_file(self, config_files, config_schema):
        errors = None
        obj = None

        if is_marshmallow3():
            try:
                obj = config_schema.load(config_files)
                data = config_schema.dumps(obj)
            except ValidationError as e:
                errors = e.messages
        else:
            obj, errors = config_schema.load(config_files)
            data, errors = config_schema.dumps(obj)

        assert not errors
        assert data == '[Section1]\noption1 = mandatory string\noption2 = optional string\noption3 = 42\noption4 = 24\n[Section2]\noption1 = mandatory string\noption2 = optional string\noption3 = 42\noption4 = 24'

    def it_validates_config_files_readability(
        self, non_readable_config_files, config_schema
    ):
        errors = None
        obj = None
        if is_marshmallow3():
            try:
                obj = config_schema.load(non_readable_config_files)
            except ValidationError as e:
                errors = e.messages
        else:
            obj, errors = config_schema.load(non_readable_config_files)

        assert not obj
        assert 'config_files' in errors
        assert 'No config files loaded!' in errors['config_files']

        if not is_marshmallow3():
            config_schema.strict = True

            with pytest.raises(ValidationError) as e:
                obj, errors = config_schema.load(non_readable_config_files)
                assert 'config_files' in e.errors
                assert 'No config files loaded!' in e.errors['config_files']

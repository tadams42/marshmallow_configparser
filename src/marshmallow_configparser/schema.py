from copy import deepcopy

from marshmallow import Schema, SchemaOpts, post_load
from marshmallow.exceptions import ValidationError

from .compatibility import is_marshmallow3

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import SafeConfigParser as ConfigParser

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class ModelOpts(SchemaOpts):
    def __init__(self, meta, **kwargs):
        SchemaOpts.__init__(self, meta, **kwargs)
        self.model = getattr(meta, 'model', None)
        self.model_args = getattr(meta, 'model_args', [])
        self.model_kwargs = getattr(meta, 'model_kwargs', {})


class ConfigParserSchema(Schema):
    OPTIONS_CLASS = ModelOpts

    @post_load
    def make_config_object(self, data):
        if self.opts.model:
            c = self.opts.model(*self.opts.model_args, **self.opts.model_kwargs)
            for k, v in data.items():
                setattr(c, k, v)
            return c

        return data

    def dump(self, obj):
        """
        Dump object to list of strings representing INI file.

        In marshmallow 2.x.x returns tuple of ``data, errors`` or raises
        depending on ``self.strict``

        In marshmallow 3.x.x always returns ``data`` or raises (schema is
        always strict in marshmallow 3.x.x)
        """

        if is_marshmallow3():
            errors = {}
            data = super(ConfigParserSchema, self).dump(obj)
        else:
            data, errors = super(ConfigParserSchema, self).dump(obj)
            if errors:
                return [], errors

        transformed_data = {}
        for key in data.keys():
            section, option = key.split('.')
            if section not in transformed_data:
                transformed_data[section] = {}
            transformed_data[section][option] = data[key]

        ini_data = []
        for section in sorted(transformed_data.keys()):
            options = transformed_data[section]
            ini_options = []
            for option, value in options.items():
                ini_options.append(option + ' = ' + str(value))
            ini_data = ini_data + ['[' + section + ']'] + sorted(ini_options)

        if is_marshmallow3():
            return ini_data
        else:
            return ini_data, errors

    def dumps(self, obj):
        """
        Dump object to string representing INI file.

        In marshmallow 2.x.x returns tuple of ``data, errors`` or raises
        depending on ``self.strict``

        In marshmallow 3.x.x always returns ``data`` or raises (schema is
        always strict in marshmallow 3.x.x)
        """

        if is_marshmallow3():
            ini_data = self.dump(obj)
            return "\n".join(ini_data)

        else:
            ini_data, errors = self.dump(obj)
            if not errors:
                return "\n".join(ini_data), errors
            return "", errors

    def load(self, config_files):
        """
        Load configuration from list of config file paths.

        In marshmallow 2.x.x returns tuple of ``data, errors`` or raises
        depending on ``self.strict``

        In marshmallow 3.x.x always returns ``data`` or raises (schema is
        always strict in marshmallow 3.x.x)
        """
        config_parser = ConfigParser()

        if not config_parser.read(config_files):
            msg = (
                "No config files loaded! Paths tried: {0}".format(config_files)
            )

            if is_marshmallow3():
                raise ValidationError({'config_files': msg})
            else:
                if self.strict:
                    raise ValidationError({'config_files': msg})
                else:
                    return dict(), {'config_files': msg}

        else:
            return self._load_from_config_parser(config_parser)

    def loads(self, ini_file_data):
        """
        Load configuration from string representing INI file.

        In marshmallow 2.x.x returns tuple of ``data, errors`` or raises
        depending on ``self.strict``

        In marshmallow 3.x.x always returns ``data`` or raises (schema is
        always strict in marshmallow 3.x.x)
        """
        str_io = StringIO(ini_file_data)
        config_parser = ConfigParser()

        try:
            config_parser.readfp(str_io, "mem")
        except AttributeError:
            config_parser.read_file(str_io, "mem")

        return self._load_from_config_parser(config_parser)

    def _load_from_config_parser(self, config_parser):
        self.config_parser_data = {}

        for section in config_parser.sections():
            for option in config_parser.options(section):
                self.config_parser_data[section + '.' + option] = (
                    config_parser.get(section, option)
                )

        return super(ConfigParserSchema, self).load(
            deepcopy(self.config_parser_data)
        )

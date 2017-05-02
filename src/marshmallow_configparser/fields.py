from marshmallow import fields


class ConfigParserFieldMixin(object):
    @property
    def load_from(self):
        return self._load_from

    @load_from.setter
    def load_from(self, value):
        if value:
            self._load_from = self._section + '.' + str(value)
        else:
            self._load_from = value

    @property
    def dump_to(self):
        return self._dump_to

    @dump_to.setter
    def dump_to(self, value):
        if value:
            self._dump_to = self._section + '.' + str(value)
        else:
            self._dump_to = value


class Dict(ConfigParserFieldMixin, fields.Dict):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(Dict, self).__init__(*args, **kwargs)


class List(ConfigParserFieldMixin, fields.List):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(List, self).__init__(*args, **kwargs)


class String(ConfigParserFieldMixin, fields.String):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(String, self).__init__(*args, **kwargs)


class UUID(ConfigParserFieldMixin, fields.UUID):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(UUID, self).__init__(*args, **kwargs)


class Number(ConfigParserFieldMixin, fields.Number):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(Number, self).__init__(*args, **kwargs)


class Integer(ConfigParserFieldMixin, fields.Integer):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(Integer, self).__init__(*args, **kwargs)


class Decimal(ConfigParserFieldMixin, fields.Decimal):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(Decimal, self).__init__(*args, **kwargs)


class Boolean(ConfigParserFieldMixin, fields.Boolean):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(Boolean, self).__init__(*args, **kwargs)


class FormattedString(ConfigParserFieldMixin, fields.FormattedString):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(FormattedString, self).__init__(*args, **kwargs)


class Float(ConfigParserFieldMixin, fields.Float):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(Float, self).__init__(*args, **kwargs)


class DateTime(ConfigParserFieldMixin, fields.DateTime):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(DateTime, self).__init__(*args, **kwargs)


class LocalDateTime(ConfigParserFieldMixin, fields.LocalDateTime):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(LocalDateTime, self).__init__(*args, **kwargs)


class Time(ConfigParserFieldMixin, fields.Time):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(Time, self).__init__(*args, **kwargs)


class Date(ConfigParserFieldMixin, fields.Date):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(Date, self).__init__(*args, **kwargs)


class TimeDelta(ConfigParserFieldMixin, fields.TimeDelta):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(TimeDelta, self).__init__(*args, **kwargs)


class Url(ConfigParserFieldMixin, fields.Url):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(Url, self).__init__(*args, **kwargs)


class Email(ConfigParserFieldMixin, fields.Email):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(Email, self).__init__(*args, **kwargs)


class Method(ConfigParserFieldMixin, fields.Method):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(Method, self).__init__(*args, **kwargs)


class Function(ConfigParserFieldMixin, fields.Function):
    def __init__(self, section, *args, **kwargs):
        self._section = section
        super(Function, self).__init__(*args, **kwargs)

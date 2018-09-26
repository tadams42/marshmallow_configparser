from .compatibility import is_marshmallow3
from .fields import Boolean, Integer, String
from .helpers import is_blank


class ConfigString(String):
    """
    :class:`marshmallow.fields.Field` that ensures:

    - option is always present in deserialized data
    - deserialized value is either the one read from config file or one
      declared in ``default``

    This is pretty similar to :class:`.String`, except this one assumes
    defaults for some of :class:`.String` attributes.
    """

    if is_marshmallow3():
        def __init__(
            self, section, default='', attribute=None, data_key=None,
            error=None, load_only=False, dump_only=False,
            error_messages=None, validate=None, **metadata
        ):
            super(ConfigString, self).__init__(
                section=section, attribute=attribute, data_key=data_key,
                error=error, error_messages=error_messages,
                default=default or '', missing=default or '', allow_null=False,
                required=False, validate=validate, **metadata
            )

    else:
        def __init__(
            self, section, default='', attribute=None, load_from=None,
            dump_to=None, error=None, load_only=False, dump_only=False,
            error_messages=None, validate=None, **metadata
        ):
            super(ConfigString, self).__init__(
                section=section, attribute=attribute, load_from=load_from,
                dump_to=dump_to, error=error, error_messages=error_messages,
                default=default or '', missing=default or '', allow_null=False,
                required=False, validate=validate, **metadata
            )

    def _deserialize(self, value, attr, data):
        retv = super(ConfigString, self)._deserialize(value, attr, data)
        if is_blank(retv):
            return self.default
        return retv


class ConfigInteger(Integer):
    """
    :class:`marshmallow.fields.Field` that ensures:

    - option is always present in deserialized data
    - deserialized value is either the one read from config file or one
      declared in ``default``
    - allows None as deserialized value (:class:`.Integer` raises
      ValidationError('Not a valid integer.'))

    This is pretty similar to :class:`.Integer`, except this one assumes
    defaults for some of :class:`.Integer` attributes and changes treating of
    None values.
    """

    if is_marshmallow3():
        def __init__(
            self, section, default=None, attribute=None, data_key=None,
            error=None, error_messages=None, as_string=False, validate=None,
            **metadata
        ):
            super(ConfigInteger, self).__init__(
                section=section, attribute=attribute,
                data_key=data_key, error=error, error_messages=error_messages,
                default=default, missing=default, allow_null=True,
                required=False, as_string=as_string, validate=validate,
                **metadata
            )
    else:
        def __init__(
            self, section, default=None, attribute=None, load_from=None,
            dump_to=None, error=None, error_messages=None, as_string=False,
            validate=None, **metadata
        ):
            super(ConfigInteger, self).__init__(
                section=section, attribute=attribute, load_from=load_from,
                dump_to=dump_to, error=error, error_messages=error_messages,
                default=default, missing=default, allow_null=True,
                required=False, as_string=as_string, validate=validate,
                **metadata
            )

    def _deserialize(self, value, attr, data):
        if is_blank(value):
            return self.default
        return super(ConfigInteger, self)._deserialize(value, attr, data)


class ConfigBoolean(Boolean):
    """
    :class:`marshmallow.fields.Field` that ensures:

    - option is always present in deserialized data

    This is pretty similar to :class:`.Boolean`, except this one assumes
    defaults for some of :class:`.Integer` attributes.
    """

    if is_marshmallow3():
        def __init__(
            self, section, default=None, attribute=None, data_key=None,
            error=None, error_messages=None, **metadata
        ):
            super(ConfigBoolean, self).__init__(
                section=section, attribute=attribute, data_key=data_key,
                error=error, error_messages=error_messages,
                default=default, missing=default, allow_null=True,
                required=False, **metadata
            )
    else:
        def __init__(
            self, section, default=None, attribute=None, load_from=None,
            dump_to=None, error=None, error_messages=None, **metadata
        ):
            super(ConfigBoolean, self).__init__(
                section=section, attribute=attribute, load_from=load_from,
                dump_to=dump_to, error=error, error_messages=error_messages,
                default=default, missing=default, allow_null=True,
                required=False, **metadata
            )

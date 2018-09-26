import marshmallow
from pkg_resources import parse_version


def is_marshmallow3():
    return parse_version(marshmallow.__version__) >= parse_version('3.0.0b1')

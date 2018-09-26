__version__ = '0.3.3'

import logging

from .compatibility import is_marshmallow3
from .convenience_fields import ConfigBoolean, ConfigInteger, ConfigString
from .fields import (UUID, Boolean, Date, DateTime, Decimal, Dict, Email,
                     Float, FormattedString, Function, Integer, List,
                     LocalDateTime, Method, Number, String, Time, TimeDelta,
                     Url)
from .schema import ConfigParserSchema
from .validators import IsNotBlank, IsNotNone

logging.getLogger(__name__).addHandler(logging.NullHandler())

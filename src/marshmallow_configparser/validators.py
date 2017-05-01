from marshmallow.validate import ValidationError
from marshmallow.validate import Validator

from .helpers import is_blank


class IsNotBlank(Validator):
    """Validator which succeeds if the value passed is not blank string."""

    def __call__(self, value):
        if is_blank(value):
            raise ValidationError("Can't be blank!")

        return value

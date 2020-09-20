import six
from apps.common.usecases import ValidatedEnum


class BaseEnumerate(ValidatedEnum):

    values = {}

    @classmethod
    def get_choices(cls):
        return list(cls.values.items())

    get_items = get_choices

    @classmethod
    def get_constant_value_by_name(cls, name):

        if not isinstance(name, six.string_types):
            raise TypeError("'name' must be a string")

        if not name:
            raise ValueError("'name' must not be empty")

        return cls.__dict__[name]

    @classmethod
    def get_keys(cls):
        return list(cls.values.keys())
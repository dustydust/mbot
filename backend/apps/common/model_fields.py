from django.db.models import CharField
from django.db.models import DecimalField


class ChoiceCharField(CharField):
    def __init__(self, *args, **kwargs):
        if 'max_length' not in kwargs:
            kwargs['max_length'] = 30

        super().__init__(*args, **kwargs)


class InchesField(DecimalField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('decimal_places', 6)
        kwargs.setdefault('max_digits', 20)
        kwargs.setdefault('null', False)
        kwargs.setdefault('blank', False)
        kwargs.setdefault('help_text', 'Value in inches.')

        super().__init__(*args, **kwargs)
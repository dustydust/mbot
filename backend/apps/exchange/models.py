from django.db import models
from apps.common.models import BaseUUIDModel


class Exchange(BaseUUIDModel):
    name = "Bittrex"

    def __str__(self):
        return ""

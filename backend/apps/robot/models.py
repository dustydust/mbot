from django.db import models
from apps.common.models import BaseUUIDModel


class Robot(BaseUUIDModel):
    is_active = models.BooleanField(default=False)
    cryptopair = "BTC-USD"
    strategy = ""
    exchange = "Bittrex"

    def __str__(self):
        return ""

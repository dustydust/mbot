from django.db import models
from apps.common.models import BaseUUIDModel


class Robot(BaseUUIDModel):
    is_active = models.BooleanField(default=False)
    use_socket = models.BooleanField(default=False)
    cryptopair = models.CharField(max_length=256, default="BTC-USD")
    strategy = models.CharField(max_length=256)
    exchange = models.CharField(max_length=256, default="Bittrex")

    def __str__(self):
        return ""

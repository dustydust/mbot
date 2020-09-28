from django.db import models
from apps.common.models import BaseUUIDModel
from apps.strategy.models import Strategy


class Robot(BaseUUIDModel):
    is_active = models.BooleanField(default=False)
    use_socket = models.BooleanField(default=False)
    cryptopair = models.CharField(max_length=256, default="BTC-USD")
    strategy = models.ForeignKey(Strategy, on_delete=models.DO_NOTHING, blank=True, null=True)
    exchange = models.CharField(max_length=256, default="Bittrex")

    def __str__(self):
        return f"{self.strategy}"

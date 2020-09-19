from django.db import models


class Robot(models.Model):
    is_active = models.BooleanField(default=False)
    cryptopair = "BTC-USD"
    strategy = ""
    exchange = "Bittrex"

    def __str__(self):
        return ""

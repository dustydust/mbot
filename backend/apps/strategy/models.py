from django.db import models
from apps.common.models import BaseUUIDModel


class Strategy(BaseUUIDModel):
    name = models.CharField(max_length=256)
    strategy_file = models.CharField(max_length=256)

    def __str__(self):
        return ""

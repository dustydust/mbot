from django.db import models
from apps.common.models import BaseUUIDModel
from apps.strategy.utils import get_local_strategies


class Strategy(BaseUUIDModel):
    name = models.CharField(max_length=256, default="1")
    directory = models.CharField(max_length=256, choices=get_local_strategies('tuple'), default=None)

    @staticmethod
    def get_strategies():
        return get_local_strategies()


    def __str__(self):
        return ""

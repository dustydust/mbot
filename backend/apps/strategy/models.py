from django.db import models
from apps.common.models import BaseUUIDModel
from apps.strategy.utils import get_local_strategies
from apps.strategy.utils import get_strategy_entity


class Strategy(BaseUUIDModel):
    name = models.CharField(max_length=256, default="1")
    directory = models.CharField(max_length=256, choices=get_local_strategies('tuple'), default=None)

    @staticmethod
    def get_strategies() -> enumerate:
        return get_local_strategies()

    def get_strategy(self):
        strategy_object = get_strategy_entity(self.directory)
        return strategy_object

    def __str__(self):
        return f"{self.name}"

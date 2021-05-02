from django.db import models
from apps.common.models import BaseUUIDModel
from apps.strategy.utils import get_local_strategies
from apps.strategy.utils import get_strategy_entity

import inspect
import json


class Strategy(BaseUUIDModel):
    name = models.CharField(max_length=256, default="1")
    directory = models.CharField(max_length=256, choices=get_local_strategies('tuple'), default=None)
    config = models.TextField(null=True, blank=True)

    @staticmethod
    def get_strategies() -> enumerate:
        return get_local_strategies()

    def get_strategy(self, context: models.Model):
        strategy_object = get_strategy_entity(self.directory, context)
        return strategy_object

    def __str__(self) -> str:
        return f"{self.name}"


class StrategyInterface():

    def load_strategy_state(self):
        attributes = inspect.getmembers(self, lambda a: not (inspect.isroutine(a)))
        filtered_attributes = {a[0]:a[1] for a in attributes
                               if not (a[0].startswith('__') and a[0].endswith('__'))}
        strategy = Strategy.objects.get(name=filtered_attributes["context"])
        if strategy.config:
            strategy_state = json.loads(strategy.config)

            for key in strategy_state.keys():
                if key not in ["context"]:
                    print(f"key {key}")
                    setattr(self, key, strategy_state[key])

            return json.loads(strategy.config)
        return False

    def save_strategy_state(self):
        attributes = inspect.getmembers(self, lambda a: not (inspect.isroutine(a)))
        filtered_attributes = {a[0]: a[1] for a in attributes
                               if not (a[0].startswith('__') and a[0].endswith('__'))}
        filtered_attributes["context"] = str(filtered_attributes["context"])
        strategy = Strategy.objects.get(name=filtered_attributes["context"])

        strategy.config = json.dumps(filtered_attributes)
        strategy.save()

        return filtered_attributes
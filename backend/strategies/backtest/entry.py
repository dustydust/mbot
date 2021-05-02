from apps.strategy.models import StrategyInterface
from apps.exchange.models import PairHistory
import datetime
from datetime import date
from datetime import timedelta

from decimal import *

getcontext().prec = 8

class StrategyMap(StrategyInterface):
    def __init__(self, context=None):
        self.context = context
        self.load_strategy_state()

    def go(self):
        tickers = PairHistory.objects.filter(starts_at__range=(date(2020,10,28), date(2020,10,29)))
        for tick in tickers:
            print(tick.open)

        return self.save_strategy_state()



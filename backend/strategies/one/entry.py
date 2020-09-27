from apps.exchange.models import Exchange
from apps.exchange.models import Order


class StrategyMap:
    def __init__(self, context=None):
        self.context = context

    def action_a(self):
        print("I'm the action of first strategy!")
        return True

    def go(self):
        # self.action_a()
        exch = Exchange.objects.get(name="btrx1")
        print(exch.get_ticker("ltc-btc"))
        print(exch.apikey)
        print(exch.testing)
        # print("I'm the go method!")


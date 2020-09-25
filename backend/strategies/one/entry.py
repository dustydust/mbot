from apps.exchange.models import ExchangeBittrex

class StrategyMap:
    def __init__(self, context=None):
        self.context = context

    def action_a(self):
        print("I'm the action of first strategy!")
        return True

    def go(self):
        self.action_a()
        r = ExchangeBittrex.get_ticker("btc-ltc")
        print(r.json())
        # print("I'm the go method!")


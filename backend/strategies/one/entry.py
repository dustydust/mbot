from apps.exchange.models import Exchange
from apps.exchange.models import Order
from apps.strategy.models import StrategyInterface
from decimal import *

getcontext().prec = 8

"""
    What is StrategyMap
    It is a class that implements number of instructions for
    robot with ability to save state and pass it throught iterations
    All inner state variables should be declared in __init__ with context.
    Context passes from view.
    load_strategy_state() and save_strategy_state() 
    must be called to save it state
"""

class StrategyMap(StrategyInterface):
    def __init__(self, context=None):
        self.context = context
        self.iteration = 0
        self.some_string = "string"
        self.load_strategy_state()

    @staticmethod
    def _process_tiker(bittrex_ticker: dict) -> dict:
        ticker = dict()
        ticker["last"] = Decimal(bittrex_ticker["lastTradeRate"])
        ticker["bid"] = Decimal(bittrex_ticker["bidRate"])
        ticker["ask"] = Decimal(bittrex_ticker["askRate"])

        return ticker

    def go(self):
        self.iteration += 1
        self.some_string = "yo!"

        pair = 'LTC-BTC'
        exch = Exchange.objects.get(name="btrx1")

        # GET TICKER
        ticker = self._process_tiker(exch.get_ticker(pair))

        # CHECK ORDERS
        orders = Order.objects.filter(
                                      exchange_type=exch.exchange_type,
                                      strategy__name=self.context.name,
                                      direction="Buy",
                                      status="Opened"
                                     )
        print(f"Ticker Last: {ticker['last']}, Count of Orders: {len(orders)}")

        for order in orders:
            if order.price_open < ticker["ask"]:
                print(f"Order price is: {order.price_open}, market price is {ticker['ask']}, selling/closing")
                order.price_close = ticker['ask']
                order.status = "Closed"
                order.save()

        if len(orders) < 5:
            new_order = Order(
                exchange_type=exch.exchange_type,
                strategy=self.context,
                quantity=Decimal(0.5),
                price_open=ticker["ask"],
                direction="Buy",
                pair=pair,
                uuid_outer="None"
            )
            new_order.save()
            print("Order is created")
            # exch.buy_limit()
        else:
            print("Waiting for closing orders...")
        print(f"Iteration is : {self.iteration}")

        return self.save_strategy_state()


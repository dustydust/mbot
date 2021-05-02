from apps.exchange.models import Exchange
from apps.exchange.models import Order
from django.db import models
from decimal import *

getcontext().prec = 8

class StrategyMap:
    def __init__(self, context=None):
        self.context = context

    def action_a(self):
        print("I'm the action of first strategy!")
        return True

    @staticmethod
    def _process_tiker(bittrex_ticker: dict) -> dict:
        ticker = dict()
        ticker["last"] = Decimal(bittrex_ticker["lastTradeRate"])
        ticker["bid"] = Decimal(bittrex_ticker["bidRate"])
        ticker["ask"] = Decimal(bittrex_ticker["askRate"])

        return ticker

    def go(self, context: models.Model):
        self.context = context


        # pair = 'LTC-BTC'
        # exch = Exchange.objects.get(name="btrx1")
        #
        # # GET TICKER
        # ticker = self._process_tiker(exch.get_ticker(pair))
        #
        # # CHECK ORDERS
        # orders = Order.objects.filter(
        #                               exchange_type=exch.exchange_type,
        #                               strategy__name=self.context.name,
        #                               direction="Buy",
        #                               status="Opened"
        #                              )
        # print(f"Ticker Last: {ticker['last']}, Count of Orders: {len(orders)}")
        #
        # for order in orders:
        #     if order.price_open < ticker["ask"]:
        #         print(f"Order price is: {order.price_open}, market price is {ticker['ask']}, selling/closing")
        #         order.price_close = ticker['ask']
        #         order.status = "Closed"
        #         order.save()
        #
        # if len(orders) < 5:
        #     new_order = Order(
        #         exchange_type=exch.exchange_type,
        #         strategy=self.context,
        #         quantity=Decimal(0.5),
        #         price_open=ticker["ask"],
        #         direction="Buy",
        #         pair=pair,
        #         uuid_outer="None"
        #     )
        #     new_order.save()
        #     print("Order is created")
        #     # exch.buy_limit()
        # else:
        #     print("Waiting for closing orders...")

        return True


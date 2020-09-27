from django.db import models
from apps.common.models import BaseUUIDModel
from apps.common.model_fields import ChoiceCharField
from apps.exchange.enums import ExchangeTypeEnum
from apps.common.requests import Request
from apps.strategy.models import Strategy
from decimal import *

BITTREX_BASE = "https://api.bittrex.com/v3/"
ORDER_DIRECTION_CHOICES = [
    ('BUY', 'Buy'),
    ('SELL', 'Sell'),
    ('DEBUG', 'Debug')
]


class Order(BaseUUIDModel):
    uuid_outer = models.CharField(max_length=256, default="")
    exchange_type = ChoiceCharField(choices=ExchangeTypeEnum.get_choices(),
                                    default=ExchangeTypeEnum.BITTREX)
    testing = models.BooleanField(default=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=11, blank=True, null=True)
    price = models.DecimalField(max_digits=18, decimal_places=11, blank=True, null=True)
    direction = ChoiceCharField(choices=ORDER_DIRECTION_CHOICES, blank=False, default="DEBUG")
    strategy = models.ForeignKey(Strategy, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.uuid}"


class ExchangeInterface(models.Model):
    name = models.CharField(max_length=256, default="robo")
    exchange_type = ChoiceCharField(choices=ExchangeTypeEnum.get_choices(),
                                    default=ExchangeTypeEnum.BITTREX)
    apikey = models.CharField(max_length=256, default="")
    testing = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def get_balance(self, wallet):
        """
        :argument: (string) (BTC-LTC)
        :return: (float) value of holding cryptowallet (100.00000)
        """
        pass

    def get_open_orders(self):
        pass

    @staticmethod
    def get_ticker(pair):
        """
        :param pair:
        :return:
        """
        pass

    def buy_limit(self):
        pass

    def sell_limit(self):
        pass


class Bittrex(ExchangeInterface):

    # https://bittrex.github.io/api/v3#topic-Authentication
    # Implement Headers

    class Meta:
        abstract = True

    @staticmethod
    def get_ticker(pair):
        print(f"Requesting {BITTREX_BASE}markets/{str(pair).upper()}/ticker")
        response = Request.get(f"{BITTREX_BASE}markets/{str(pair).upper()}/ticker").json()
        if response.get("code"):
            return print("ERROR: ", response.get("code"))
        return response

    def buy_limit(self, market: str = "", quantity: Decimal = 0.0, price: Decimal = 0.0):
        if self.testing:
            return {
                "exchange_type": self.exchange_type,
                "quantity": quantity,
                "price": price,
            }

        payload = {
            "marketSymbol": "value",
            "direction": "BUY",
            "type:": "LIMIT",
            "timeInForce": "GOOD_TIL_CANCELLED",
            "quantity": quantity,
            "limit": price
        }

        response = Request.post(f"{BITTREX_BASE}/orders", data=payload).json()

        if response.get("code"):
            return print("ERROR: ", response.get("code"))
        return response

    def sell_limit(self, market: str = "", quantity: Decimal = 0.0, price: Decimal = 0.0):
        if self.testing:
            return {
                "exchange_type": self.exchange_type,
                "quantity": quantity,
                "price": price,
            }

        payload = {
            "marketSymbol": "value",
            "direction": "SELL",
            "type:": "LIMIT",
            "timeInForce": "GOOD_TIL_CANCELLED",
            "quantity": quantity,
            "limit": price
        }

        response = Request.post(f"{BITTREX_BASE}/orders", data=payload).json()

        if response.get("code"):
            return print("ERROR: ", response.get("code"))
        return response

    def get_open_orders(self, marketsymbol: str = ""):
        # Return local exchange orders and remote
        response = Request.get(f"{BITTREX_BASE}orders/open")
        if response.get("code"):
            return print("ERROR: ", response.get("code"))
        return response


class Exchange(BaseUUIDModel, Bittrex):

    def __str__(self):
        return f"{self.name}"


class ExchangePoloniex(ExchangeInterface):

    class Meta:
        abstract = True

    @staticmethod
    def get_ticker(pair):
        pass
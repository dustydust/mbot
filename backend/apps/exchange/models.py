from django.db import models
from apps.common.models import BaseUUIDModel
from apps.common.model_fields import ChoiceCharField
from apps.exchange.enums import ExchangeTypeEnum
from apps.common.requests import Request
from decimal import *

BITTREX_BASE = "https://api.bittrex.com/v3/"
ORDER_DIRECTION_CHOICES = [
    ('BUY', 'Buy'),
    ('SELL', 'Sell'),
]


class Order(BaseUUIDModel):
    uuid_outer = models.CharField(max_length=256, default="")
    exchange_type = ChoiceCharField(choices=ExchangeTypeEnum.get_choices(),
                                    default=ExchangeTypeEnum.BITTREX)
    testing = models.BooleanField(default=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=11)
    price = models.DecimalField(max_digits=18, decimal_places=11)
    direction = ChoiceCharField(choices=ORDER_DIRECTION_CHOICES, blank=False)

    def __str__(self):
        return f"{self.uuid}"


class ExchangeActionInterface(models.Model):
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


class Exchange(BaseUUIDModel, ExchangeActionInterface):
    name = models.CharField(max_length=256, default="robo")
    exchange_type = ChoiceCharField(ExchangeTypeEnum.get_choices(),
                                    default=ExchangeTypeEnum.BITTREX)
    apikey = models.CharField(max_length=256)
    testing = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class ExchangeBittrex(Exchange, ExchangeActionInterface):

    # https://bittrex.github.io/api/v3#topic-Authentication
    # Implement Headers

    class Meta:
        abstract = True

    @staticmethod
    def get_ticker(pair):
        response = Request.get(f"{BITTREX_BASE}markets/{str(pair).upper()}/ticker")
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

        response = Request.post(f"{BITTREX_BASE}/orders", data=payload)

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

        response = Request.post(f"{BITTREX_BASE}/orders", data=payload)

        if response.get("code"):
            return print("ERROR: ", response.get("code"))
        return response

    def get_open_orders(self, marketsymbol: str = ""):
        # Return local exchange orders and remote
        response = Request.get(f"{BITTREX_BASE}orders/open")
        if response.get("code"):
            return print("ERROR: ", response.get("code"))
        return response


class ExchangePoloniex(ExchangeActionInterface):

    class Meta:
        abstract = True

    @staticmethod
    def get_ticker(pair):
        pass
from django.db import models
from apps.common.models import BaseUUIDModel
from apps.common.model_fields import ChoiceCharField
from apps.exchange.enums import ExchangeTypeEnum
from apps.exchange.enums import OrderDirectionEnum
from apps.exchange.enums import OrderStatusEnum
from apps.common.requests import Request
from apps.strategy.models import Strategy
from decimal import *

BITTREX_BASE = "https://api.bittrex.com/v3/"

# > datetime.fromisoformat('2018-12-11T00:56:00')
# datetime.datetime(2018, 12, 11, 0, 56)


class Order(BaseUUIDModel):
    uuid_outer = models.CharField(max_length=256, default="")
    exchange_type = ChoiceCharField(choices=ExchangeTypeEnum.get_choices(),
                                    default=ExchangeTypeEnum.BITTREX)
    testing = models.BooleanField(default=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=11, blank=True, null=True)
    price_open = models.DecimalField(max_digits=18, decimal_places=11, default=0.0)
    price_close = models.DecimalField(max_digits=18, decimal_places=11, default=0.0)
    direction = ChoiceCharField(choices=OrderDirectionEnum.get_choices(),
                                default=OrderDirectionEnum.BUY)
    strategy = models.ForeignKey(Strategy, on_delete=models.DO_NOTHING, blank=True, null=True)
    pair = models.CharField(max_length=256, default="")
    status = ChoiceCharField(choices=OrderStatusEnum.get_choices(),
                             default=OrderStatusEnum.OPENED)

    def __str__(self):
        return f"{self.uuid}"


class PairHistory(models.Model):
    pair = models.CharField(max_length=256, default="")
    exchange_type = ChoiceCharField(choices=ExchangeTypeEnum.get_choices(),
                                    default=ExchangeTypeEnum.BITTREX)
    starts_at = models.DateTimeField() # "2018-12-11T00:56:00Z"
    open = models.DecimalField(max_digits=18, decimal_places=11, default=0.0) # "0.00471835"
    high = models.DecimalField(max_digits=18, decimal_places=11, default=0.0) # "0.00471835"
    low = models.DecimalField(max_digits=18, decimal_places=11, default=0.0) # "0.00471835"
    close = models.DecimalField(max_digits=18, decimal_places=11, default=0.0) # "0.00471835"
    volume = models.DecimalField(max_digits=18, decimal_places=11, default=0.0) # "1.07286662"
    quote_volume = models.DecimalField(max_digits=18, decimal_places=11, default=0.0) # "0.00754226"

    def __repr__(self):
        return f"{pair} - {starts_at} - {self.pk}"


class ExchangeInterface(models.Model):
    name = models.CharField(max_length=256, default="robo")
    exchange_type = ChoiceCharField(choices=ExchangeTypeEnum.get_choices(),
                                    default=ExchangeTypeEnum.BITTREX)
    apikey = models.CharField(max_length=256, default="")
    testing = models.BooleanField(default=True)

    ###

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
            "marketSymbol": market,
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
            "marketSymbol": market,
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

    class Meta:
        app_label = "exchange"

    def __str__(self):
        return f"{self.name}"


class ExchangePoloniex(ExchangeInterface):

    class Meta:
        abstract = True

    @staticmethod
    def get_ticker(pair):
        pass
from django.db import models
from apps.common.models import BaseUUIDModel
from apps.common.model_fields import ChoiceCharField
from apps.exchange.enums import ExchangeTypeEnum
from apps.common.requests import Request
from decimal import *


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

    def __str__(self):
        return f"{self.name}"


class ExchangeBittrex(Exchange, ExchangeActionInterface):

    class Meta:
        abstract = True

    @staticmethod
    def get_ticker(pair):
        return Request.get("https://api.bittrex.com/api/v1.1/public/getticker?market=" + str(pair).upper())

    def buy_limit(self, market: str = "", quantity: Decimal = 0.0, rate: Decimal = 0.0):
        return Request.get(
            f"https://api.bittrex.com/api/v1.1/market/buylimit?"
            f"apikey={self.apikey}&market={market}&quantity={quantity}&rate={rate}"
        )

class ExchangePoloniex(ExchangeActionInterface):

    class Meta:
        abstract = True

    @staticmethod
    def get_ticker(pair):
        pass
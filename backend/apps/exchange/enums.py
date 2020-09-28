from apps.common.utils import BaseEnumerate


class ExchangeTypeEnum(BaseEnumerate):
    BITTREX = "bittrex"
    POLONIEX = "poloniex"

    values = {
        BITTREX: "Bittrex",
        POLONIEX: "Poloniex"
    }


class OrderDirectionEnum(BaseEnumerate):
    BUY = "Buy"
    SELL = "Sell"

    values = {
        BUY: "Buy",
        SELL: "Sell"
    }


class OrderStatusEnum(BaseEnumerate):
    OPENED = "Opened"
    CLOSED = "Closed"

    values = {
        OPENED: "Opened",
        CLOSED: "Closed"
    }
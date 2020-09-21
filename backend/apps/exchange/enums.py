from apps.common.utils import BaseEnumerate


class ExchangeTypeEnum(BaseEnumerate):
    BITTREX = 'bittrex'
    POLONIEX = 'poloniex'

    values = {
        BITTREX: 'Bittrex',
        POLONIEX: 'Poloniex'
    }
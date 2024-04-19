from bybit_api import ByBit
from models import Side, InstrumentInfo

import config


if __name__ == '__main__':
    bb = ByBit(config.bybit_credentials)
    # print(bb.get_balance(coin='USDT'))
    #
    # print(bb.get_orderbook(symbol='ETHUSDT'))

    # instruments: list[InstrumentInfo] = bb.get_instruments()
    # for instrument in instruments:
    #     print(instrument)
    # # print(instruments)
    # print(bb.get_instrument)
    # print(bb.get_best_price(symbol='SOLUSDT', liquidity=200, limit=20))
    # print(bb.create_order(
    #     coin='ARB',
    #     symbol='ARBUSDT',
    #     side=Side.buy,
    #     #instrument_info=instrument_info
    # ))
    #
    # bb.cancel_orders(symbol='ARBUSDT')

    # print(ByBit.round_to_accuracy(number=1.324324324, accuracy='0.01'))


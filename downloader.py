from datetime import datetime, timedelta

from tinkoff.invest import Client, RequestError, CandleInterval, HistoricCandle
from pandas import DataFrame

def get_data():

    TOKEN = ''
    try:
        with Client(TOKEN) as client:
            r = client.market_data.get_candles(
                figi='BBG004730RP0',
                from_=datetime.utcnow() - timedelta(days=3653),
                to=datetime.utcnow(),
                interval=CandleInterval.CANDLE_INTERVAL_MONTH  # см. utils.get_all_candles
            )
            # print(r)
            df = create_df(r.candles)
            #print(df.to_string())
            return df

    except RequestError as e:
        print(str(e))


def create_df(candles: [HistoricCandle]):
    df = DataFrame([{
        'time': c.time,
        'volume': c.volume,
        'open': cast_money(c.open),
        'close': cast_money(c.close),
        'high': cast_money(c.high),
        'low': cast_money(c.low),
    } for c in candles])

    return df


def cast_money(v):
    """
    https://tinkoff.github.io/investAPI/faq_custom_types/
    :param v:
    :return:
    """
    return v.units + v.nano / 1e9 # nano - 9 нулей


class Downloader:

    def __int__(self, delta_cap, volume):
        self.delta_cap = delta_cap
        self.volume = volume

    def big_cats_or_consensus(self, d_c, v):
        b_c_o_c = self.d_c / self.volume

        return b_c_o_c

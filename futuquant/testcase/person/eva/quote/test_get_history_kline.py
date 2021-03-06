#-*-coding:utf-8-*-

import futuquant
from futuquant.common.constant import *
import pandas

class GetHistoryKline(object):

    def __init__(self):
        pandas.set_option('max_columns',100)
        pandas.set_option('display.width',1000)

    def test1(self):
        quote_ctx = futuquant.OpenQuoteContext(host='127.0.0.1',port=11111)
        code = 'SH.000300'
        start = '2017-04-14'
        end = '2017-04-14'
        ktype = KLType.K_1M
        autype = AuType.QFQ
        fields = KL_FIELD.ALL_REAL

        ret_code , ret_data = quote_ctx.get_history_kline(code, start, end, ktype, autype, fields)

        print(ret_code)
        print(ret_data)
        quote_ctx.close()

if __name__ == '__main__':
    ghk = GetHistoryKline()
    # for i in range(10):
    ghk.test1()
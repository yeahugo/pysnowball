import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls
import time


def kline(symbol):
	time_stamp = int(round(time.time() * 1000))
	params = '&begin='+str(time_stamp)+'&period=day&count=-142&indicator=kline'
	url = api_ref.kline_url+symbol+params
	return utls.fetch(url)


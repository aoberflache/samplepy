# -*- coding: utf-8 -*-
import numpy
import matplotlib.pyplot as plt
import json
import requests
from six.moves.urllib.parse import urlparse
from six.moves.urllib.parse import urlencode

def ticker():
    URL={'bitFlyer':'https://api.bitflyer.jp/v1/getticker?product_code=BTC_JPY',
    'Zaif':'https://api.zaif.jp/api/1/ticker/btc_jpy',
    'Coincheck':'https://coincheck.com/api/ticker'}
    bf = requests.get(URL['Coincheck']).json()
    zf = requests.get(URL['Zaif']).json()
    cc = requests.get(URL['Coincheck']).json()
    return (bf,zf,cc)

### main ###
fig, ax = plt.subplots(1, 1)
x = numpy.arange(0,1000, 1)
tic = ticker()
y1 = plt.plot(x,tic[0]['last'])
y2 = plt.plot(x,tic[1]['last'])
y3 = plt.plot(x,tic[2]['last'])
lines, = ax.plot(x, y1)
while True:
    x += 1
    tic = ticker()
    y1 = plt.plot(x,tic[0]['last'])
    y2 = plt.plot(x,tic[1]['last'])
    y3 = plt.plot(x,tic[2]['last'])
    lines.set_data(x, y1)
    plt.pause(.01)

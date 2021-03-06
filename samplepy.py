import json
import requests
from six.moves.urllib.parse import urlparse
from six.moves.urllib.parse import urlencode

def ticker():
    URL={'bitFlyer':'https://api.bitflyer.jp/v1/getticker?product_code=BTC_JPY',
    'Quoine':'https://api.quoine.com/products/5',
    'Zaif':'https://api.zaif.jp/api/1/ticker/btc_jpy',
    'Coincheck':'https://coincheck.com/api/ticker'}
    
    bf = requests.get(URL['Coincheck']).json()
    qo = requests.get(URL['Quoine']).json()
    zf = requests.get(URL['Zaif']).json()
    cc = requests.get(URL['Coincheck']).json()
    return (bf,qo,zf,cc)


def lineAlert(message):
    LINE_ACCESS_TOKEN=""
    url = "https://notify-api.line.me/api/notify"
    msg = urlencode({"message":message})
    LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    a=session.post(url, headers=LINE_HEADERS, data=msg)


### main ###
tic = ticker()
exchanger = ["bifFlyer","Quoine","Zaif","Coincheck"]
for x in range(4):
    print ("#### " + exchanger[x] + " ####")
    print (tic[x])
    print()

###
if float(tic[3]['last']) > 700000:
    message = "Alert"
    lineAlert(message)

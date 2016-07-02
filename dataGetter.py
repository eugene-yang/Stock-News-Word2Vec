from datetime import date
from datetime import datetime
import math
import requests
from lxml import etree

priceDic = {}

def getNews(ticker):
    url = 'https://www.google.com/finance/company_news?q=' + ticker + '&start=0&num=1000'
    r = requests.get(url)
    dom = etree.HTML(r.content)
    nameList = dom.xpath("//div[@id='news-main']//span[@class='name']/a/text()")
    dateList = dom.xpath("//div[@id='news-main']//span[@class='date']/text()")

    rtn = []
    for i in range(len(nameList)):
        d = dateList[i]
        n = nameList[i].replace("\xa0", " ")
        if "ago" in d:
            d = date.today()
        else:
            d = datetime.strptime(d, "%b %d, %Y").date()
        rtn.append({'title': n, 'date': d})

    return rtn

def getHistoricalPrice(ticker):
    if ticker in priceDic:
        # print("using cache price series for " + ticker)
        return priceDic[ticker]

    print("fetching price series for " + ticker + "...")
    url = "http://www.google.com/finance/historical?q=" + ticker + "&startdate=Jan+1%2C+2014&output=csv"
    r = requests.get(url)
    print("fetching price series done")
    lines = r.content.decode('utf-8').split("\n")
    lines.pop(0)
    raw = [ l.split(",") for l in lines ]
    data = []
    for d in raw:
        if d[0] == '':
            continue
        data.append({
            'date': datetime.strptime(d[0], "%d-%b-%y").date(),
            'open': float( d[1] ),
            'high': float( d[2] ),
            'low': float( d[3] ),
            'close': float( d[4] ),
            'volume': int( d[5] )
        })
    data.sort(key=lambda i: i['date'], reverse = True)
    priceDic[ticker] = data
    return data

def getPriceByDate(ticker, date, offset):
    # offset is for choosing the price of date relative to
    # the specified date, 1 for future 1 date, -1 for past 1 date
    data = getHistoricalPrice(ticker)
    pos = None
    i = 0
    for d in data:
        if date == d['date']:
            pos = 0
            break
        elif date > d['date']:
            pos = -0.5
            break
        i = i + 1

    if pos == None or ( offset==0 and pos != 0 ):
        return None

    finalpos = int( i + pos - offset )
    if finalpos < 0 or finalpos >= len(data):
        return None

    return data[finalpos]
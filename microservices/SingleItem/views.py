from django.http import HttpResponse
from django.shortcuts import render
import json
import requests
# Create your views here.


def getItemSells(item: str, howMany: int, jsonLoaded: json):
    stringArray = []
    for k in jsonLoaded:
        if k == item.upper():
            sells = {k: v for k, v in sorted(jsonLoaded[k].items(), reverse=False, key=lambda item: len(item[1]))}
            sells = sells['sell_summary']
    for c, _object in enumerate(sells):
        passing_object = {'amount': _object['amount'],
                                  'pricePerUnit': _object['pricePerUnit'],
                                  'ordersNum': _object['orders'],
                                  'index': c + 1
                               }
        stringArray.append(passing_object)
    return stringArray


def getItemBuys(item: str, howMany: int, jsonLoaded: json):
    stringArray = []
    for k in jsonLoaded:
        if k == item.upper():
            buys = {k: v for k, v in sorted(jsonLoaded[k].items(), reverse=False, key=lambda item: len(item[1]))}
            buys = buys['buy_summary']
            # print('BUY ORDERS' + '\n' + str(buys))
    for c, _object in enumerate(buys):
        cnt = len(buys) - c - 1
        _object = buys[cnt]
        passing_object = {'amount': _object['amount'],
                                  'pricePerUnit': _object['pricePerUnit'],
                                  'ordersNum': _object['orders'],
                                  'index': cnt
                        }
        stringArray.append(passing_object)
    return stringArray


def index_sells(request, item):
    x = requests.get('https://api.slothpixel.me/api/skyblock/bazaar')
    parsed = json.dumps(x.json())
    jsonLoaded = json.loads(parsed)
    test = getItemSells(item, 100, jsonLoaded)
    return HttpResponse(json.dumps(test))


def index_buys(request, item):
    x = requests.get('https://api.slothpixel.me/api/skyblock/bazaar')
    parsed = json.dumps(x.json())
    jsonLoaded = json.loads(parsed)
    test = getItemBuys(item, 100, jsonLoaded)
    return HttpResponse(json.dumps(test))

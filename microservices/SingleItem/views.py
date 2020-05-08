import math

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
    weighted_avg = (get_weighted_average(test))
    std_deviation(test, weighted_avg)
    return HttpResponse(json.dumps(test))


def index_buys(request, item):
    x = requests.get('https://api.slothpixel.me/api/skyblock/bazaar')
    parsed = json.dumps(x.json())
    jsonLoaded = json.loads(parsed)
    test = getItemBuys(item, 100, jsonLoaded)
    weighted_avg = (get_weighted_average(test))
    print(std_deviation(test, weighted_avg))
    return HttpResponse(json.dumps(test))


def get_weighted_average(array: []):
    totalItems = 0
    totalPrice = 0
    totalJob = 0
    for item in array:
        totalItems = totalItems + (item['amount'] * item['ordersNum'])
        totalPrice = totalPrice + item['pricePerUnit'] * (item['amount'] * item['ordersNum'])
        totalJob += 1
    return totalPrice/totalItems


def std_deviation(array: [], weighted_avg):
    total_results = 0
    for item in array:
        result = weighted_avg - item['pricePerUnit']
        result = result * result
        total_orders = item['amount'] * item['ordersNum']
        # print(result, total_orders)
        total_results += result
    lower_range = weighted_avg - math.sqrt(total_results/total_orders) * 5
    upper_range = weighted_avg + math.sqrt(total_results/total_orders) * 5
    print('weighted_priced:', weighted_avg, '\n',
          'lower_range:', lower_range, '\n'
          'upper_range:', upper_range, '\n')

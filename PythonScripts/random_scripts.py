import json
import requests
import math
from _models.StdDeviationObject import StdDeviationObject


def get_data_from_external_api() -> json:
    x = requests.get('https://api.slothpixel.me/api/skyblock/bazaar')
    parsed = json.dumps(x.json())
    json_loaded = json.loads(parsed)
    return json_loaded


def get_item_sells(item: str, howMany: int, jsonLoaded: json) -> []:
    stringArray = []
    for k in jsonLoaded:
        if k == item.upper():
            sells = {k: v for k, v in sorted(jsonLoaded[k].items(), reverse=False, key=lambda item: len(item[1]))}
            sells = sells['sell_summary']
    for c, _object in enumerate(sells):
        passing_object = {'amount': _object['amount'],
                          'pricePerUnit': _object['pricePerUnit'],
                          'ordersNum': _object['orders'],
                          'index': c + 1,
                          'item_name': item
                          }
        stringArray.append(passing_object)
    return stringArray


def get_item_buys(item: str, howMany: int, jsonLoaded: json) -> []:
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

import math

from django.http import HttpResponse
import json
import requests

# Create your views here.
from microservices.queryAllItems.models import BazaarOrders


def get_data_from_external_api() -> json:
    x = requests.get('https://api.slothpixel.me/api/skyblock/bazaar')
    parsed = json.dumps(x.json())
    json_loaded = json.loads(parsed)
    generate_orders_object_array(json_loaded)
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


def index_buys_view(request, item) -> HttpResponse:
    json_loaded = get_data_from_external_api()
    test = get_item_sells(item, 100, jsonLoaded=json_loaded)
    weighted_avg = (get_weighted_average(test))
    std_deviation(test, weighted_avg, item)
    std_deviation_object = std_deviation(test, weighted_avg, item)
    # save_items_to_database(test, False, item)
    return HttpResponse(json.dumps(test))


def index_sells_view(request, item) -> HttpResponse:
    json_loaded = get_data_from_external_api()
    test = get_item_sells(item, 100, jsonLoaded=json_loaded)
    weighted_avg = (get_weighted_average(test))
    std_deviation_object = std_deviation(test, weighted_avg, item)
    # save_items_to_database(test, True, item)
    return HttpResponse(json.dumps(test))


def get_weighted_average(array: []) -> float:
    totalItems = 0
    totalPrice = 0
    totalJob = 0
    for item in array:
        totalItems = totalItems + (item['amount'] * item['ordersNum'])
        totalPrice = totalPrice + item['pricePerUnit'] * (item['amount'] * item['ordersNum'])
        totalJob += 1
    return totalPrice / totalItems


def std_deviation(array: [], weighted_avg, item_name: str) -> {}:
    total_results = 0
    for item in array:
        result = weighted_avg - item['pricePerUnit']
        result = result * result
        total_orders = item['amount'] * item['ordersNum']
        total_results += result
    lower_range = weighted_avg - math.sqrt(total_results / total_orders) * 1
    upper_range = weighted_avg + math.sqrt(total_results / total_orders) * 1
    passing_object = {'weighted_priced': weighted_avg,
                      'lower_range': lower_range,
                      'upper_range': upper_range,
                      'enchanted_item_price': weighted_avg * 160}
    return StdDeviationObject(std_deviation_dict=passing_object, item_name=item_name)


def generate_orders_object_array(response: json):
    final_object_array = []
    for item in response:
        print(item)


def save_items_to_database(array: [], sell_or_buy: bool, item_name: str) -> None:
    """
    :param item_name: str item name.
    :param array: array of all orders non-nested.
    :param sell_or_buy: sell = True. buy = False.
    :return: None
    """
    for item in array:
        BazaarOrders.objects.create(amount=item['amount'],
                                    pricePerUnit=item['pricePerUnit'],
                                    ordersNum=item['ordersNum'],
                                    sell_or_buy=sell_or_buy,
                                    item_name=item_name)


class StdDeviationObject:
    __slots__ = ('weighted_price', 'lower_range', 'upper_range', 'enchanted_item_price', 'item_name')

    def __init__(self, std_deviation_dict, item_name):
        self.weighted_price = std_deviation_dict['weighted_priced']
        self.upper_range = std_deviation_dict['lower_range']
        self.lower_range = std_deviation_dict['upper_range']
        self.enchanted_item_price = std_deviation_dict['enchanted_item_price']
        self.item_name = item_name


class OrderObject:
    __slots__ = ('amount', 'pricePerUnit', 'ordersNum', 'sell_or_buy', 'item_name')

    def __init__(self, amount: int, price_per_unit: float, orders_num: int, sell_or_buy: bool, item_name: str):
        self.amount = amount
        self.pricePerUnit = price_per_unit
        self.ordersNum = orders_num
        self.amount = sell_or_buy
        self.item_name = item_name


def getJsonRespone():
    x = requests.get('https://api.slothpixel.me/api/skyblock/bazaar')
    parsed = json.dumps(x.json())
    jsonLoaded = json.loads(parsed)
    final_sell_array = []
    final_buy_array = []

    for item in jsonLoaded:
        for item2 in jsonLoaded[item]:
            if item2 == 'sell_summary':
                type_of_order = 0
                sell_orders = jsonLoaded[item][item2]
                for item3 in sell_orders:
                    print(item3)
                    final_sell_array.append(OrderObject(amount=item3['amount'],
                                                        item_name=item,
                                                        price_per_unit=item3['pricePerUnit'],
                                                        sell_or_buy=type_of_order,
                                                        orders_num=item3['orders']))
            if item2 == 'buy_summary':
                type_of_order = 1
                buy_orders = jsonLoaded[item][item2]
                for item3 in buy_orders:
                    final_buy_array.append(OrderObject(amount=item3['amount'],
                                                       item_name=item,
                                                       price_per_unit=item3['pricePerUnit'],
                                                       sell_or_buy=type_of_order,
                                                       orders_num=item3['orders']))
    return jsonLoaded

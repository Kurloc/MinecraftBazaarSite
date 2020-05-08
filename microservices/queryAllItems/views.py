import json

import requests
from django.shortcuts import render

# Create your views here.
from _models.OrderObject import OrderObject
from microservices.queryAllItems.models import BazaarOrders


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
                if type_of_order == 0: type_of_order = False
                if type_of_order == 1: type_of_order = True
                sell_orders = jsonLoaded[item][item2]
                for item3 in sell_orders:
                    final_sell_array.append(OrderObject(amount=item3['amount'],
                                                        item_name=item,
                                                        price_per_unit=item3['pricePerUnit'],
                                                        sell_or_buy=type_of_order,
                                                        orders_num=item3['orders']))
            if item2 == 'buy_summary':
                type_of_order = 1
                if type_of_order == 0: type_of_order = False
                if type_of_order == 1: type_of_order = True
                buy_orders = jsonLoaded[item][item2]
                for item3 in buy_orders:
                    final_buy_array.append(OrderObject(amount=item3['amount'],
                                                       item_name=item,
                                                       price_per_unit=item3['pricePerUnit'],
                                                       sell_or_buy=type_of_order,
                                                       orders_num=item3['orders']))
    print(len(final_sell_array))
    print(len(final_buy_array))
    return jsonLoaded



from django.http import HttpResponse
import json

from PythonScripts.random_scripts import get_data_from_external_api, get_item_sells, get_item_buys
from PythonScripts.std_deviation import std_deviation
from PythonScripts.weighted_average import get_weighted_average
from microservices.queryAllItems.models import BazaarOrders

# Create your views here.
from microservices.queryAllItems.views import getJsonRespone


def index_buys_view(request, item) -> HttpResponse:
    json_loaded = get_data_from_external_api()
    test = get_item_buys(item, 100, jsonLoaded=json_loaded)
    weighted_avg = get_weighted_average(test)
    std_deviation(test, weighted_avg, item)
    std_deviation_object = std_deviation(test, weighted_avg, item)
    print(std_deviation_object.lower_range, std_deviation_object.upper_range,' - ', weighted_avg)
    return HttpResponse(json.dumps(test))


def index_sells_view(request, item) -> HttpResponse:
    json_loaded = get_data_from_external_api()
    test = get_item_sells(item, 100, jsonLoaded=json_loaded)
    weighted_avg = get_weighted_average(test)
    std_deviation_object = std_deviation(test, weighted_avg, item)
    print(std_deviation_object.lower_range, std_deviation_object.upper_range,' - ', weighted_avg)
    return HttpResponse(json.dumps(test))


getJsonRespone()

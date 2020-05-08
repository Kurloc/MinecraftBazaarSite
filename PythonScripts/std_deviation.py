import math

from _models.StdDeviationObject import StdDeviationObject


def std_deviation(array: [], weighted_avg, item_name: str) -> {}:
    total_results = 0
    total_orders = 0
    for item in array:
        result = weighted_avg - item['pricePerUnit']
        result = result * result
        total_orders = total_orders + item['amount'] * item['ordersNum']
        total_results += result
    lower_range = weighted_avg - math.sqrt(total_results / total_orders) * 1
    upper_range = weighted_avg + math.sqrt(total_results / total_orders) * 1
    passing_object = {'weighted_priced': weighted_avg,
                      'lower_range': upper_range,
                      'upper_range': lower_range,
                      'enchanted_item_price': weighted_avg * 160}
    return StdDeviationObject(std_deviation_dict=passing_object, item_name=item_name)

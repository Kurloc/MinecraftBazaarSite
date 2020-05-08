def get_weighted_average(array: []) -> float:
    totalItems = 0
    totalPrice = 0
    totalJob = 0
    for item in array:
        totalItems = totalItems + (item['amount'] * item['ordersNum'])
        totalPrice = totalPrice + item['pricePerUnit'] * (item['amount'] * item['ordersNum'])
        totalJob += 1
    return totalPrice / totalItems

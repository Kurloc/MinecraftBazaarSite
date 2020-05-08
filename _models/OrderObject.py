class OrderObject:
    __slots__ = ('amount', 'pricePerUnit', 'ordersNum', 'sell_or_buy', 'item_name')

    def __init__(self, amount: int, price_per_unit: float, orders_num: int, sell_or_buy: bool, item_name: str):
        self.amount = amount
        self.pricePerUnit = price_per_unit
        self.ordersNum = orders_num
        self.amount = sell_or_buy
        self.item_name = item_name
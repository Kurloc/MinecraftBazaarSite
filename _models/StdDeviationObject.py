class StdDeviationObject:
    __slots__ = ('weighted_price', 'lower_range', 'upper_range', 'enchanted_item_price', 'item_name')

    def __init__(self, std_deviation_dict, item_name):
        self.weighted_price = std_deviation_dict['weighted_priced']
        self.upper_range = std_deviation_dict['lower_range']
        self.lower_range = std_deviation_dict['upper_range']
        self.enchanted_item_price = std_deviation_dict['enchanted_item_price']
        self.item_name = item_name

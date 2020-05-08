from django.db import models


# Create your _models here.
class BazaarOrders(models.Model):
    amount = models.IntegerField()
    ordersNum = models.IntegerField()
    pricePerUnit = models.FloatField()
    sell_or_buy = models.BooleanField()
    item_id = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)

from django.db import models

# Create your models here.
class orders(models.Model):
    order_id = models.CharField(max_length=100)
    order_date = models.DateField()
    order_status = models.CharField(max_length=100)
    order_total = models.IntegerField()
    order_customer = models.CharField(max_length=100)
    order_product = models.CharField(max_length=100)
    order_quantity = models.IntegerField()
    order_price = models.IntegerField()

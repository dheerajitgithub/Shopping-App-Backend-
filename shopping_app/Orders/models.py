from django.db import models
from Product.models import ProductModel
from Customer.models import CustomerModel,AddressModel
from datetime import datetime

# Create your models here.
class OrderDetailsModel(models.Model):
    user_id = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE)
    placed_at = models.DateTimeField(auto_now_add=True)
    modifried_at = models.DateTimeField(auto_now=True, defualt=datetime.now)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Order Details"
        verbose_name_plural = "Order Details"
    

class OrderItemsModel(models.Model):
    order_id = models.OneToOneField(OrderDetailsModel, on_delete=models.CASCADE)
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    


    class Meta:
        verbose_name = "Order Items"
        verbose_name_plural = "Order Items"



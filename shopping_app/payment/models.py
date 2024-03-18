from django.db import models
from Orders.models import Order
from .utils import *

# Create your models here.
class PaymentDetailsModel(models.Model):
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=1, choices = PaymentStatusType.choices(), default="Pending")

    
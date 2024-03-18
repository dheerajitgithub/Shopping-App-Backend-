from django.db import models
from .utils import *


# Create your models here.
class CustomerModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100)
    membership_type = models.CharField(max_length=100, choices = MembershipType.choices(), default='Basic')

    class meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class AddressModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, related_name='customer_addresses')
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    
    
    class meta:
        verbose_name = 'Customer_Address'
        verbose_name_plural = 'Customers_Addresses'
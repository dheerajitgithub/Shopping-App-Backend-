from Customer.models import CustomerModel, AddressModel
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number','membership_type']

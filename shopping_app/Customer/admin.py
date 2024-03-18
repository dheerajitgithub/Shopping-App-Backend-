from django.contrib import admin
from .models import CustomerModel, AddressModel
# Register your models here.
@admin.register(CustomerModel)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone_number", "membership_type")
    search_fields = ("first_name", "last_name", "email", "phone_number")

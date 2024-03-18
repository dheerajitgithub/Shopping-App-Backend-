from django.contrib import admin
from .models import PaymentDetailsModel

# Register your models here.
@admin.register(PaymentDetailsModel)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'amount','status']
    search_fields = ['order_id']
from django.contrib import admin
from .models import ProductDiscountModel, ProductCategoryModel, ProductInventoryModel, ProductModel


# Register your models here.
@admin.register(ProductDiscountModel)
class ProductDiscountModelAdmin(admin.ModelAdmin):
    list_display = ('discount', 'created_at','modified_at', 'deleted_at')
    search_fields = ('discount','active')


@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at','modified_at', 'deleted_at')
    search_fields = ('name',)

@admin.register(ProductInventoryModel)
class ProductInventoryModelAdmin(admin.ModelAdmin):
    list_display = ('name','quantity', 'created_at','modified_at', 'deleted_at')
    search_fields = ('name',)

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_id', 'price', 'inventory_id', 'discount_id')
    search_fields = ('name','category_id', 'price', 'inventory_id', 'discount_id')
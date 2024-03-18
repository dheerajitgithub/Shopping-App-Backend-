from django.db import models

# Create your models here.
class ProductCategoryModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"  

class ProductInventoryModel(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class meta:
        verbose_name = "Product Inventory"
        verbose_name_plural = "Product Inventory"

class ProductDiscountModel(models.Model):
    discount = models.IntegerField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    class meta:
        verbose_name = "Product Discount"
        verbose_name_plural = "Product Discounts"


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    category_id = models.ForeignKey(ProductCategoryModel, on_delete=models.CASCADE)
    price = models.IntegerField()
    inventory_id = models.ForeignKey(ProductInventoryModel, on_delete=models.CASCADE)
    discount_id = models.ForeignKey(ProductDiscountModel, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"



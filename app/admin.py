from django.contrib import admin
from .models import Customer,Product,Cart,OrderPlaced
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin,):
    list_display = ['id','title','selling_price','discounted_price','brand','category']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display =['id', 'user', 'name','locality', 'city', 'state', 'zipcode']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']

admin.site.register(OrderPlaced)

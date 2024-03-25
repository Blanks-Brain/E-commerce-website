from django.contrib import admin
from .models import Customer,Product,Cart,OrderPlaced
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin,):
    list_display = ['id','title','selling_price','discounted_price','brand','category']

admin.site.register(Customer)

admin.site.register(Cart)
admin.site.register(OrderPlaced)

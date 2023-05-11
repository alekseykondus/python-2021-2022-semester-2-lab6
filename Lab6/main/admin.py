from django.contrib import admin
from .models import CategoryProduct
from .models import Product
# Register your models here.
admin.site.register(CategoryProduct)
admin.site.register(Product)
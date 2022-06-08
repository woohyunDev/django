from django.contrib import admin

from shop.models import Product
from .models import Product, Review 
# Register your models here.

admin.site.register(Product)
admin.site.register(Review)
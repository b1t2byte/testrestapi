from django.contrib import admin

from products.models import Product, Discount

admin.site.register(Product)
admin.site.register(Discount)

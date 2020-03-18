from django.contrib import admin
from .models import Warehouse, Product, WarehouseProduct, Unit

admin.site.register(Warehouse)
admin.site.register(Product)
admin.site.register(WarehouseProduct)
admin.site.register(Unit)

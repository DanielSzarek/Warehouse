from django.shortcuts import render, get_object_or_404
from .models import WarehouseProduct, Warehouse, Product


def warehouse_list(request):
    warehouses = Warehouse.objects.all().order_by('name')
    return render(request, 'warehouse/warehouse_list.html', {'warehouses': warehouses})


def warehouse_products(request, pk):
    products = WarehouseProduct.objects.filter(warehouse=pk).order_by('exp_date')
    warehouse = get_object_or_404(Warehouse, pk=pk)
    return render(request, 'warehouse/warehouse_products.html', {'warehouse_products': products, 'warehouse': warehouse})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'warehouse/product_detail.html', {'product': product})

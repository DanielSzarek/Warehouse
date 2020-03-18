from django.db import models
from django.utils import timezone


class Warehouse(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class WarehouseProduct(models.Model):
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    exp_date = models.DateField(default=timezone.now)

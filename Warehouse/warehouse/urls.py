from django.urls import path
from . import views

urlpatterns = [
    path('', views.warehouse_list, name='warehouse_list'),
    path('magazyn/<int:pk>/', views.warehouse_products, name='warehouse_products'),
    path('produkt/<int:pk>/', views.product_detail, name='product_detail')
]
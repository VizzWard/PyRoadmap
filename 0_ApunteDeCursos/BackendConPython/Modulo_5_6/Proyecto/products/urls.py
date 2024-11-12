from django.contrib import admin
from django.urls import path

# Importar las vistas creadas
from .views import index, get_product

urlpatterns = [
    path('', index, name='index'),
    path('/product/<int:id>', get_product, name='get_product')
]
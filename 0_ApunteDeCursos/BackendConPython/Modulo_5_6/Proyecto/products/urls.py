from django.contrib import admin
from django.urls import path

# Importar las vistas creadas
from .views import index, get_product, add_new_comment

urlpatterns = [
    path('', index, name='index'),
    path('/product/<int:id>', get_product, name='get_product'),
    path('product/<int:id>/add_new_comment', add_new_comment, name='add_new_comment')
]
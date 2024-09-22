from django.contrib import admin
from django.urls import path

# Importar las vistas creadas
from .views import index

urlpatterns = [
    path('', index),
]
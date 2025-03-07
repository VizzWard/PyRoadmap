from django.contrib import admin
from django.urls import path

# Importar las vistas creadas
from .views import login_view, logout_view, signup_view

urlpatterns = [
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('signup', signup_view, name='signup'),
]
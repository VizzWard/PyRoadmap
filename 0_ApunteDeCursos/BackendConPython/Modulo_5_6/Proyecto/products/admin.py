from django.contrib import admin
from .models import Products, Brand, Comment

# Register your models here.
admin.site.register(Products)
admin.site.register(Brand)
admin.site.register(Comment)
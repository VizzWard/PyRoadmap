from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

# Create your models here.

# Crearemos la primer tabla
# Aqui crearemos los parametros que tendra la tabla
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    sku = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        null=True
    )

    brand = models.ForeignKey(
        'products.Brand',
        on_delete=models.CASCADE,
        related_name='products'
    )

    image = models.ImageField(
        blank=True,
        null=True,
        upload_to='media/products'
    )

    discount = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    @property
    def final_price(self):
        if self.discount > 0:
            discount_amount = (self.price * Decimal(self.discount)) / Decimal(100)
            return self.price - discount_amount
        return self.price

    @property
    def has_discount(self):
        return self.discount > 0

    def __str__(self):
        return f'{self.name} | {self.brand}'


class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    logo = models.ImageField(
        blank=True,
        null=True,
        upload_to='media/brand'
    )

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(
        'products.Products',
        on_delete=models.CASCADE,
        related_name='comments'
    )

    author = models.CharField(max_length=200)

    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    aproved_comment = models.BooleanField(default=False)

    def approve(self):
        self.aproved_comment = True
        self.save()

    def __str__(self):
        return self.text
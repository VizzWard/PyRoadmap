from django.db import models
from django.utils import timezone

# Create your models here.

# Crearemos la primer tabla
# Aqui crearemos los parametros que tendra la tabla
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    sku = models.CharField(max_length=10)
    category = models.CharField(max_length=100)

    # Modificamos este parametro para referenciar de otra tabla
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

    discount = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # Con este metodo podremos modificar la forma de visualizar los datos en la DB
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
from django.shortcuts import render
from django.http import HttpResponse

from .models import Products

# Create your views here.

def index(request):
    # Devolver la lista de productos que esten en la base de datos
    products = Products.objects.all()
    return render(request,'list_of_products.html', {'products': products})

def get_product(request, id):
    product = Products.objects.get(id=id)
    return render(
        request,
        'show_product.html',
        {'product': product})
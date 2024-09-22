from django.shortcuts import render
from django.http import HttpResponse

from .models import Products

# Create your views here.

def index(request):
    # Devolver la lista de productos que esten en la base de datos
    products = Products.objects.all()
    return render(request,'list_of_products.html', {'products': products})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import (login_required, permission_required)
from django.http import HttpResponse

from .models import Products, Comment
from .forms import CommentsForm

# Create your views here.

def index(request):
    # Devolver la lista de productos que esten en la base de datos
    products = Products.objects.all()
    return render(
        request,
        'products/list_of_products.html',
        {'products': products}
    )

def get_product(request, id):
    product = Products.objects.get(id=id)

    comments = Comment.objects.filter(product=id)

    form = CommentsForm()
    return render(
        request,
        'products/show_product.html',
        {'product': product,
                'comments': comments,
                'form': form })


@login_required
@permission_required('products.add_comment', raise_exception=True)
def add_new_comment(request, id):
    if request.method == 'POST':

        form = CommentsForm(request.POST)

        if form.is_valid():
            user = request.user
            product = Products.objects.get(id=id)

            new_comment = form.save(commit=False)
            new_comment.author = user
            new_comment.product = product

            new_comment.save()

    return redirect('get_product', id)
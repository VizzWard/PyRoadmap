# Pasos seguidos

## 1. Navigation bar

Modificaremos la barra de navegacion, esta actualmente esta en nuestra base, y lo que haremos es pasarla a otro archivo y desde ese lo importaremos a nuestra base. Para esto creamos el archivo `nav.html` en el que copiaremos todo lo respectivo a la barra de navegacion:

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="{% url 'index' %}">Tienda de Barrio</a>
        <ul class="navbar-nav">
        {% if user.is_authenticated %}
                <li class="nav-item">
                    <a class="nav-link" href="/" tabindex="-1">{{ user.username }}</a>
                </li>
                <li class="nav-item">
                    <form action={% url 'logout' %} method="post">
                        {% csrf_token %}
                        <button class="btn btn-outline-light me-2" tabindex="-2" type="submit">Logout</button>
                    </form>
                </li>

        {% else %}

            <li class="nav-item">
                <a class="btn btn-outline-light me-2"
                    href="{% url 'login' %}"
                    tabindex="-1"
                    aria-disabled="true">Login</a>
            </li>
        {% endif %}
    </ul>
    </div>

</nav>
```

Y lo borraremos del archivo '`base.html`. Y lo que haremos sera importar este archivo en nuestra base, quedando de esta manera:

```html
{% load static %}
<html lang="es">
    <head>
        <title>Tienda de Barrio</title>
        <meta name="description" content="Mi primera tienda de barrio virtual">
        <meta name="keywords" content="ecomerce,market">
        {# Bootstrap - https://getbootstrap.com/#}
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
              rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        {# Fonts #}
        <link href="https://fonts.googleapis.com/css?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
        {# Styles #}
        <link rel="stylesheet" href="{% static 'styles1.css' %}">
    </head>
    <body>

        {% include 'base/nav.html' %}

        {% block content %}
        {% endblock %}
    </body>
</html>
```

## 2. Creacion de formularios - Comentarios

Para esto, hay que crear una nueva tabla en productos, donde van a estar los comentarios relacionados a un producto, en el archivo `models.py` de la aplicacion `products`:

```python
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
```

Y despues agregamos la tabla a `admin.py`:

```python
    admin.site.register(Comment)
```

Realizamos las migraciones y las aplicamos:

```commandline
python manage.py makemigrations --settings=settings.local
python manage.py migrate --settings=settings.local
```

Posteriormente, creamos un formulario para los comentarios, en el archivo `forms.py` de la aplicacion `products`:

```python
from django.forms import ModelForm, Textarea

from .models import Comment


class CommentsForm(ModelForm):
    class Meta:
        model = Comment

        fields = ('text',)

        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'aria-label': 'Comentarios',
                'placeholder': 'Deja tu comentario',
                'id': 'formComment'
            }),
        }
```

Y en el archivo `views.py` de la aplicacion `products`, importamos el formulario y lo agregamos a la vista de detalle de productos:

```python


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
```

Y en el archivo `urls.py` de la aplicacion `products`, agregamos la url para los comentarios:

```python
urlpatterns = [
    path('product/<int:id>/add_new_comment', add_new_comment, name='add_new_comment')
]
```

De igual manera modificaremos el metodo `get_product` para que muestre los comentarios:

```python
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
```

Temporalmente, en el archivo `show_product.html`, agregamos un formulario para los comentarios, Este ira en la parte de abajo de la pagina:

```html
    <form action="{%  url 'add_new_comment' id=product.id%}" method="post">
        {% csrf_token  %}
        {{ form }}

        <button type="submit" class="save btn btn-dark">Enviar</button>
    </form>

    <ul>
        {% for comment in comments %}
            <li>{{ comment }}</li>
        {% endfor %}
    </ul>
```

## 3. Creacion de formularios - Signup

Para esto, creamos la vista en el archivo `views.py` de la aplicacion `accounts`:

```python
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(
        request,
        'accounts/signup.html',
        {'form': form})
```

Igual se modifica el metodo `login_view`:

```python
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})
```

Añadimos la vista a las urls de la aplicacion `accounts`:

```python
urlpatterns = [
    path('signup', signup_view, name='signup'),
]
```

Y creamos el archivo `signup.html` en la carpeta `templates/accounts`:

```html
{% extends "base/base.html" %}
{% block content %}
<div class="login-container container">
    <div class="card">
        <div class="card-body">
            <h1 class="text-center mb-5">Signup</h1>

            <form action={% url 'signup' %} method="post">
                {% csrf_token %}
                {{ form }}
                <input class="btn submit-btn btn-tomato" type="submit" value="Sigup">
            </form>

            Ya tienes cuenta? <a href="{% url 'login' %}">Login</a>
        </div>
    </div>
</div>
{% endblock content %}
```
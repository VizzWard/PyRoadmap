# Pasos Seguidos

## 1. Modularizar el HTML

1. Moveremos las partes de los html que siempre estan presenten de la misma manera en todas nuestras vistas HTML. Que en este caso es:

```html
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
        <link rel="stylesheet" href="{% static 'styles.css' %}">
    </head>
    <body>
    </body>
</html>
```

2. Ahora dentro del `body` añadiremos esto:

```html
<body>
    {% block navigation_bar %}
    {% endblock %}
    {% block content %} 
    {% endblock %}
</body>
```

Que no sirve para que todo lo anterior se pueda usar en otros archivos.

3. Esta estructura la pasaremos a un nuevo archivo HTML, que nombraremos `base.html`. Este lo guardaremos en una carpeta, para saber que se trata de un archivo que se usa en varias vistas.
4. Ahora modificaremos las vistas que tenemos, que son `list_of_products.html` y `show_praduct.html`. En ambas borraremos todo a excepcion de lo que este dentro del body, para el caso del primero quedaria asi:

```html
{% extends 'base/base.html' %}
{% block content %}

    <div class="container">
        <div class="row">
            {% for product in products %}
            <div class="col-3">
                <div class="card">
                    <img src="{{product.image.url}}"
                         class="card-img-top float-start">
                    <div class="card-body">
                        <h5 class="card-title">{{product.name}}</h5>
                        <div class="price-container">
                            {% if product.has_discount %}
                                <div class="price-stack">
                                    <span class="original-price">
                                        <s>{{ product.price }} MXN</s>
                                    </span>
                                    <div class="price-discount-wrapper">
                                        <span class="final-price">{{ product.final_price }} MXN</span>
                                        <span class="discount-badge">-{{ product.discount }}%</span>
                                    </div>
                                </div>
                            {% else %}
                                <span class="single-price">{{ product.price }} MXN</span>
                            {% endif %}
                        </div>
                        <a class="btn btn-tomato" href="{% url 'get_product' id=product.id %}">Leer más</a>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>

{% endblock %}
```


## 2. Añadir estilos a las paginas

1. Mejoraremos el diseño de las paginas, añadiendo un archivo css. Para esto crearemos una nueva carpeta que la nombraremos staticfiles, en la que añadiremos archivos que no se modificaran comunmente o archivos con cierto tipos de datos.
2. En ella meteremos el archivo [styles.css](Proyecto/staticfiles/styles1.css).
3. Ahora tenemos que hacer que el proyecto sepa que existe ese archivo, en el archivo [base.py](Proyecto/settings/base.py), crearemos una nueva variable con los siguientes datos:

```python
STATICFILES_DIRS = [
    BASE_DIR / 'staticfiles',
]
```

Esta se pondrá después de `STATIC_URL`.

4. Como extra vamos a agregar una barra de navegacion. Esto agregandole al body del archivo `base.html` lo siguiente:

```html
<body>
    <nav class = "navbar navbar-expand-lg anvbar-dark bg-dark">
        <div class = "container">
            <a class = "navbar-brand" href = "{% url 'index' %}">Store</a>
        </div>
    </nav>
    {% block content %}
    {% endblock %}
</body>
```

## 3. Auth

1. Añadiremos la parte de autenticacion al proyecto, para esto usaremos las clases que ya incluye Django. Con esto lograremos hacer que ciertas paginas sean vistas solo por usuario o ciertos usuarios.
2. Como primer vistaso al apartado de users que ya trae Django, podemos ver el nombre de usuario que registramos para poder acceder a admin, esto lo vemos modificando el `list_of_products.html`, añadiendo al inicio del bloque lo siguiente:

```html
<h1>{{ user }}</h1>
```

3. Ahora crearemos otra aplicacion, como hicimos con products, esto lo haremos para que en esta manejemos el tema de login y cuentas.
4. Ejecutamos el comando:

```commandline
python manage.py startapp accounts
```

Esto nos creara una carpeta con los mismos archivos como lo hizo con products.

5. Ahora que se creo la aplicacion, esta la tenemos que añadir a los settings. Vamos al archivo `base.py`, y en la parte de `INSTALLED_APPS` lo agregamos:

```python
INSTALLED_APPS= [
    'products',
    'accounts',
]
```

6. Ahora en accounts, crearemos las vistas, usaremos para esto lo que ya nos incluye Django, agregamos en el archivo `views.py` de accounts esto:

```python
def login_view(request):
    if request.method == 'POST':
        pass

    return render(request, 'accounts/login.html', {'form': ''})
```

Por el momento usaremos esta estructura.

7. Ahora crearon un archivo html para el login, en templates creamos una carpeta llamada accounts, y dentro creamos un archivo `login.html`, y añadimos esto:

```html
{% extends "base/base.html" %}
{% block content %}
    <div class="login-container container">
        <h1>Login</h1>
    </div>
{% endblock content %}
```

8.  Ahora en la aplicacion `accounts` creamos un archivo `urls.py`, con esto:

```python
from django.contrib import admin
from django.urls import path

# Importar las vistas creadas
from .views import login_view

urlpatterns = [
    path('login', login_view(), name='login'),
]
```

9. Ahora registramos estas urls en la aplicacion base:

```python
urlpatterns = [
    path('', include('products.urls')), # Con este path incluiremos la ruta url creada en la carpeta products
    path('accounts/', include('accounts.urls'))
]
```

Con esto, si accedemos desde `accounts/login`, nos deberia aparecer la pagina.

10. Ahora crearemos la logica en `views.py` de accounts:

```python
def login_view(request):
    if request.method == 'POST':
        pass

    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
```

11. Y en el archivo `login.html`, añadimos esto:

```html
{% extends "base/base.html" %}
{% block content %}
    <div class="login-container container">
        <div class="card">
            <div class="card-body">
                <h1 class="text-center mb-5">Login</h1>

                <form action={% url 'login' %} method="post">
                    {% csrf_token %}
                    {{ form }}
                    <input class="btn submit-btn btn-tomato" type="submit" value="Login">
                </form>

            </div>
        </div>
    </div>
{% endblock content %}
```

12. Ahora le creamos la logica al metodo POST en el archivo `views.py`:

```python
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.get_user()
            login(request, username)
            return redirect('index')

    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
```

13. Ahora crearemos el metodo de logout:

```python
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')
```

14. Añadimos esta nueva url:

```python
from .views import login_view, logout_view

urlpatterns = [
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
]
```

15. Modificamos el apartado de `navigation-bar` del archivo `base.html`, para añadir las interacciones ya sea se este logeado o no:

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
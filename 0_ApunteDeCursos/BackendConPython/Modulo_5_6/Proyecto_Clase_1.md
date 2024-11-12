# Pasos seguidos

## Crear el proyecto y configuraciones iniciales

- Primero ir a la ruta de la carpeta deseada, en mi caso es:

```commandline
cd .\0_ApunteDeCursos\BackendConPython\Modulo5\Proyecto\
```

- En el directorio deseado, ejecutar el comando:

```commandline
django-admin startproject my_tienda .
```

- Para ejecutar el servidor:

```commandline
python manage.py runserver
```

- Para hacer las migraciones por defecto:

```commandline
python manage.py migrate
```

- Crear el usuario:

```commandline
python manage.py createsuperuser
```

```commandline
python manage.py startapp products
```

### 1.Views

Lo primero que haremos es crear algo visual, en el archivo [views](Proyecto/products/views.py). En este archivo estara nuestra logica.

- Crearemos un nuevo metodo:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello World</h1>")
```

- A diferencia de flask, que se usaba un decorador para especificar una url, en django la funcion que se crea la usaremos en el archivo [URL](Proyecto/my_tienda/urls.py)
- En este caso modularizaremos el proyecto, asi que crearemos un archivo [urls.py](Proyecto/products/urls.py) en la carpeta products.
- Ahi creamos el acceso a los metodos que creemos en [views.py](Proyecto/products/views.py).

```python
# Importar las vistas creadas
from .views import index

urlpatterns = [
    path('', index),
]
```

- Estas urls se las pasaremos al archivo [urls](Proyecto/my_tienda/urls.py), del proyecto. Agregando un nuevo path (incluir la libreria include de Django):

```python
from django.urls import path, include

urlpatterns = [
    path('', include('products.urls')), # Con este path incluiremos la ruta url creada en la carpeta products
]
```

### 2.Models

- En el archivo [models](Proyecto/products/models.py), crearemos el modelo, que es la estructura de la base de datos, que vamos a poder manejar y modificar.
- Creado el modelo de tabla `Products`, al estar esta en una aplicacion, debemos enlazarla a la carpeta del proyecto para poder hacer las migraciones. Vamos al archivo [settings](Proyecto/my_tienda/settings.py) y lo agregamos a `INSTALLED_APPS`. 
- Habiendo agregado `products`, para hacer las migraciones y se cree la tabla, vamos a la consola y ejecutamos el comando:

```commandline
python manage.py makemigrations
```

- Esto dara un error por no tener instalado la libreria `Pillow` (se usa para el manejo de imagenes), asi que instalaremos la libreria (en la raiz del [Proyecto](../../../../PythonRoadmap)):

```commandline
pip install Pillow
```

- Posteriormente actualizaremos el archivo `requirements.txt`:

```commandline
pip freeze > requirements.txt
```

- Despues de instalar Pillow, corremos el comando (en la raiz del [Proyecto](Proyecto)):

```commandline
python manage.py makemigrations
```

- Si no dio errores, esto nos tuvo que dar la salida:

```commandline
Migrations for 'products':
  products\migrations\0001_initial.py
    + Create model Products
```

- Y junto con ello, nos crea una carpeta [migration](Proyecto/products/migrations), en donde estaran las migraciones que hagamos. En el archivo [0001_initial.py](Proyecto/products/migrations/0001_initial.py), esta la migracion que acabos de hacer.
- Ahora nos falta aplicar las migraciones, esto se hace con el comando:

```commandline
python manage.py migrate
```

- Si no dio errores, esto nos tuvo que dar la salida:

```commandline
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, products, sessions
Running migrations:
  Applying products.0001_initial... OK
```

- Con esto ya tendremos una tabla en la base de datos.
- Ahora podremos desde el panel de administracion ver las tablas.
- Primero tendremos que configurarlo en el archivo [admin.py](Proyecto/products/admin.py), agregamos los siguiente:

```python
from django.contrib import admin
from .models import Products

admin.site.register(Products)
```

- Ahora podemos ver el el admin de Django la tabla que acabos de crear.
- Si quieres modificar la forma de visualizar los datos en admin, creamos un metodo integrado en Django para modificar esto, esto se agregar en el metodo Products del archivo [models.py](Proyecto/products/models.py)

```python
class Products(models.Model):
    # Con este metodo podremos modificar la forma de visualizar los datos en la DB
    def __str__(self):
        return f'{self.name} | {self.brand}'
```

### Templates

- Ahora crearos las direcciones en donde visualizaremos esos datos.
- Para esto crearemos una carpeta llamada [templates](Proyecto/templates), la ruta de la carpeta es dependiendo como se quiera manejar la estructura del proyecto (puede ir dentro de cada app, o una carpeta donde vayan todos los templates).
- Ahi guardaremos todos los archivos HTML, que usaremos para diferentes vistas.
- Lo que haremos es obtener los datos y mandarlos al frontend, para hacerlo modifcamos el archivo [views.py](Proyecto/products/views.py):

```python
from .models import Products

def index(request):
    # Devolver la lista de productos que esten en la base de datos
    products = Products.objects.all()
    return render(request,'list_of_products.html', {'products': products})
```

- Ahora agregamos la carpeta templates a los [settings](Proyecto/my_tienda/settings.py), modificamos el parametro `DIRS`:

```python
TEMPLATES = [
    {
        'DIRS': ['templates'],
    },
]
```

- Vamos al archivo [list_of_products](Proyecto/templates/products/list_of_products.html), y modificamos la parte de las listas de productos:

```html
<body>
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
                                <p class="card-title product-price">{{product.price}} USD</p>
                            </div>
                            <p class="card-text">
                                {{product.description}}
                            </p>
                            <a class="btn btn-tomato" href="/">Leer más</a>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </body>
```
__Creamos un bucle for, para que por cada producto en productos, se cree una tarjeta de presentacion, con sus respectivos valores.__

- Esto asi, funciona, pero las iamgenes no cargan, esto se debe a que en el apartado de <img>, le cargamos una url para que obtenga la imagen, pero en el archivo [urls](Proyecto/my_tienda/urls.py) de nuestro proyecto no estan configuradas esas urls, asi que tendremos que añadirlas (importamos las librerias correspondientes, y el parametro es despues del + en `urlpatterns`):

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```


## Resumen

- Creacion del proyecto `my_tiewnda`.
- Creacion de la aplicacion `products`.
    - Creacion del modelo `Products`.
    - Creacion de la vista `index`.
    - Creacion de la url `Home` del sitio.
    - Creacion del template `list_of_products.html`.
- Creacion del superuser para acceder a admin.
- Configuracion de las urls de las imagenes del sitio.
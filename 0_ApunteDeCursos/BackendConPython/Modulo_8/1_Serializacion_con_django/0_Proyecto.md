# Serializacion con Django

### Ruta del proyectp

```commandline
cd .\0_ApunteDeCursos\BackendConPython\Modulo_8\1_Serializacion_con_django\shopping_Cart\
```

## 1. Crear un proyecto de Django

```commandline
django-admin startproject shopping_Cart
```

## 2. Crear una aplicación

```commandline
python manage.py startapp api
```

Agregar la aplicación al archivo settings.py

```python
INSTALLED_APPS = [
    'api',
    ...
]
```

## 3. Crear un modelo

```python
from django.db import models

# Create your models here.
class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product_name} - ${self.product_price}"
```

Realizar las migraciones correspondientes.

```commandline
python manage.py makemigrations
python manage.py migrate
```

Agregar el modelo a admin.py, para visualizarla desde el panel de administración.

```python
from django.contrib import admin
from .models import CartItem

admin.site.register(CartItem)
```

## 4. Crear las vistas

Se crearan dos clases, para hacer un CRUD (Create, Read, Update, Delete), en una clase para POST y GET y en otra para PATH y DELETE

Clase POST y GET:

```python
import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import CartItem


# Create your views here.
# Agregamos este decorador para evitar problemas por Cross Site Request Forgery Attacks (CSRF)
@method_decorator(csrf_exempt, name='dispatch')
class ShoppingCart(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        p_name = data.get('product_name')
        p_price = data.get('product_price')
        p_quantity = data.get('product_quantity')
        
        product_data = {
            'product_name': p_name,
            'product_price': p_price,
            'product_quantity': p_quantity,
        }

        cart_item = CartItem.objects.create(**product_data)

        data = {
            "message": f"New item added to Cart with id: {cart_item.id}"
        }
        return JsonResponse(data, status=201)

    def get(self, request):
        items_count = CartItem.objects.count()
        items = CartItem.objects.all()
        items_data = []

        for item in items:
            items_data.append({
                'product_name': item.product_name,
                'product_price': item.product_price,
                'product_quantity': item.product_quantity,
            })

        data = {
            'items': items_data,
            'count': items_count,
        }

        return JsonResponse(data)
```

Clase PATH y DELETE:

```python
import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import CartItem

@method_decorator(csrf_exempt, name='dispatch')
class ShoppingCartUpdate(View):

    def patch(self, request, item_id):
        data = json.loads(request.body.decode("utf-8"))
        item = CartItem.objects.get(id=item_id)
        item.product_quantity = data['product_quantity']
        item.save()

        data = {
            'message': f'Item {item_id} has been updated'
        }

        return JsonResponse(data)

    def delete(self, request, item_id):
        item = CartItem.objects.get(id=item_id)
        item.delete()

        data = {
            'message': f'Item {item_id} has been deleted'
        }

        return JsonResponse(data)
```

## 5. Crear las rutas

En el archivo `urls.py` de la aplicación, se crearan las rutas para las vistas creadas, y en el archivo `urls.py` del proyecto, se incluira la ruta a la aplicación

urls.py de la aplicación:

```python
from django.urls import path
from .views import ShoppingCart, ShoppingCartUpdate

urlpatterns = [
    path('cart-items/', ShoppingCart.as_view()),
    path('update-item/<int:item_id>', ShoppingCartUpdate.as_view()),
]
```

urls.py del proyecto:

```python
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
```

## 6. Probar las peticiones a la api

Para probar las peticiones a la api, se puede usar la herramienta Postman, o se puede hacer desde la terminal con el comando `curl`.

### POST

```commandline
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/cart-items/ -d "{\"product_name\":\"name\",\"product_price\":\"41\",\"product_quantity\":\"1\"}"
```

### GET

```commandline
curl -X GET http://127.0.0.1:8000/cart-items/
```

### PATCH

```commandline
curl -X PATCH http://127.0.0.1:8000/update-item/1 -H "Content-Type: application/json" -d "{\"product_quantity\":\"3\"}"
```

### DELETE

```commandline
curl -X "DELETE" http://127.0.0.1:8000/update-item/1
```
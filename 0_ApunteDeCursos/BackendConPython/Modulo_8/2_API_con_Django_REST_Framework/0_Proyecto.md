# API con Django REST Framework

---

Ruta del proyecto:

```bash
cd 0_ApunteDeCursos\BackendConPython\Modulo_8\2_API_con_Django_REST_Framework\shopping_cart
```

Ejecutar aplicacion:

```bash
python manage.py runserver
```

---

## 1. Configuracion inicial


### Instalacion de Dependencias

```bash
pip install django
pip install djangorestframework
```

### Crear un Proyecto

```bash
django-admin startproject shopping_cart
```

### Crear una Aplicacion

```bash
python manage.py startapp api
```

### Agrega la aplicación de rest_framework y la que acabamos de crear en el archivo de `settings.py`

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',
]
```

---

## 2. Crear un Modelo

```python
from django.db import models

class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product_name} - ${self.product_price}"
```

### Registrar el modelo en el admin

```python
from django.contrib import admin
from .models import CartItem

admin.site.register(CartItem)
```

### Hacer las migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 3. Crear un superuser

```bash
python manage.py createsuperuser
```

---


## 4. Crear un Serializador

En la app `api`, crear un archivo `serializers.py`:

```python
from rest_framework import serializers
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = CartItem
        fields = ('__all__')
```

## 5. Crear las Vistas

### POST

```python
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CartItem
from .serializers import CartItemSerializer

class CartItemViews(APIView):
    serializer_class = CartItemSerializer

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
```

### GET

```python
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CartItem
from .serializers import CartItemSerializer

class CartItemViews(APIView):
    serializer_class = CartItemSerializer

    def get(self, request, id=None):
        if id:
            item = CartItem.objects.get(id=id)
            serializer = CartItemSerializer(item)
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK
            )

        items = CartItem.objects.all()
        serializer = CartItemSerializer(items, many=True)
        
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK
        )
```

### PATCH

```python
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CartItem
from .serializers import CartItemSerializer

class CartItemViews(APIView):
    serializer_class = CartItemSerializer

    def patch(self, request, id=None):
        item = CartItem.objects.get(id=id)
        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            })
        else:
            return Response({
                "status": "error",
                "data": serializer.errors
            })
```

### DELETE

```python
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CartItem
from .serializers import CartItemSerializer

class CartItemViews(APIView):
    serializer_class = CartItemSerializer
    
    def delete(self, request, id=None):
    item = get_object_or_404(CartItem, id=id)
    item.delete()
    return Response({"status": "success", "data": "Item Deleted"})
```

---

## 6. Configurar las URLs

En el archivo `urls.py` de la app `api`:

```python
from django.urls import path

from .views import CartItemViews

urlpatterns = [
    path('cart-items/', CartItemViews.as_view()),
    path('cart-items/<int:id>', CartItemViews.as_view())
]
```

En el archivo `urls.py` del proyecto:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

---

## 7. Probar la API

### POST

```bash
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api/cart-items/ -d "{\"product_name\":\"name\",\"product_price\":\"41\",\"product_quantity\":\"1\"}"
```

### GET

```bash
curl -X GET http://127.0.0.1:8000/api/cart-items/
```

### PATCH

```bash
curl -X PATCH http://127.0.0.1:8000/api/cart-items/1 -H 'Content-Type: application/json' -d '{"product_quantity":6}'
```

### DELETE

```bash
curl -X "DELETE" http://127.0.0.1:8000/api/cart-items/1
```

---

## 8. Paginacion

Podemos cambiar el metodo get, para que no nos de todos los items, sino que nos de una cantidad especifica. Esto se hace con la paginacion.

Primero, en el archivo `settings.py` del proyecto, agregar la configuracion de paginacion:

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
}
```

Luego, en el archivo `views.py` de la app `api`, modificar el metodo get, al igual que el serializer y la clase:

```python
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CartItem
from .serializers import CartItemSerializer

class CartItemViews(GenericAPIView):
    serializer_class = CartItemSerializer
    pagination_class = PageNumberPagination

    def get(self, request, id=None):
        if id:
            item = CartItem.objects.get(id=id)
            serializer = CartItemSerializer(item)
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK
            )

        items = CartItem.objects.all()
        serializer = CartItemSerializer(items, many=True)

        return self.get_paginated_response({"status": "success", "data": self.paginate_queryset(serializer.data)})
```
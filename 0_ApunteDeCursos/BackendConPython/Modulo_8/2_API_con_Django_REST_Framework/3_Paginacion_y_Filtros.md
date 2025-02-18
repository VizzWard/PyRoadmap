# Paginación y Filtros en Django Rest Framework (DRF)

## Paginación en DRF
La paginación en DRF permite dividir grandes conjuntos de datos en partes más manejables.

### Configuración de la Paginación
DRF proporciona varios estilos de paginación que pueden configurarse en `settings.py`.

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

### Tipos de Paginación

#### 1. `PageNumberPagination`
Permite paginación basada en número de página.

```python
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
```

#### 2. `LimitOffsetPagination`
Permite paginación basada en un límite y un desplazamiento.

```python
from rest_framework.pagination import LimitOffsetPagination

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100
```

#### 3. `CursorPagination`
Utiliza cursores para paginar grandes volúmenes de datos de manera eficiente.

```python
from rest_framework.pagination import CursorPagination

class CustomCursorPagination(CursorPagination):
    ordering = 'created_at'
    page_size = 5
```

---

## Filtrado en DRF
El filtrado permite recuperar datos específicos de un conjunto.

### Filtros Básicos
DRF soporta filtrado con `django-filter`. Instala la dependencia:

```sh
pip install django-filter
```

Luego, configúralo en `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
```

### Uso de `DjangoFilterBackend`

```python
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categoria', 'precio']
```

### Filtros Avanzados con `FilterSet`

```python
import django_filters
from .models import Producto

class ProductoFilter(django_filters.FilterSet):
    min_precio = django_filters.NumberFilter(field_name='precio', lookup_expr='gte')
    max_precio = django_filters.NumberFilter(field_name='precio', lookup_expr='lte')

    class Meta:
        model = Producto
        fields = ['categoria', 'min_precio', 'max_precio']
```

Luego, en la vista:

```python
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductoFilter
```

---
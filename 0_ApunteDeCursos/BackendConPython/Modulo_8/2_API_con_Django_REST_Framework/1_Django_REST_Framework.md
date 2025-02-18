# [Django Rest Framework](https://www.django-rest-framework.org/) (DRF)

## ¿Qué es Django Rest Framework?
Django Rest Framework (DRF) es una potente biblioteca para construir APIs REST en Django. Proporciona herramientas y clases reutilizables para facilitar la creación de APIs robustas y seguras.

## Características Principales de DRF
- Serialización flexible de datos.
- Autenticación y permisos avanzados.
- Navegación interactiva de la API.
- Soporte para vistas basadas en clases y en funciones.
- Paginación integrada.
- Integración con Django ORM y otros backends de datos.

---

## Instalación de DRF
```sh
pip install djangorestframework
```
Luego, añadir `'rest_framework'` a `INSTALLED_APPS` en `settings.py`.
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

---

## Serializadores en DRF
Los serializadores convierten los datos complejos (como modelos de Django) en formatos como JSON.

### Ejemplo de Serializador
```python
from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
```

---

## Vistas en DRF
DRF ofrece vistas basadas en clases y en funciones.

### Ejemplo de API con `APIView`
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioListView(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
```

### ViewSets y Routers
```python
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
```

---

## Autenticación y Permisos
DRF proporciona múltiples métodos de autenticación y permisos:

### Autenticación
- `SessionAuthentication`
- `TokenAuthentication`
- `JWTAuthentication` (requiere `djangorestframework-simplejwt`)

### Configuración en `settings.py`
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
```

---

## Paginación en DRF
La paginación permite controlar la cantidad de datos enviados en cada respuesta.

### Configuración de paginación en `settings.py`
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

---

## Protección y Seguridad en APIs REST
Para proteger las APIs en DRF se pueden aplicar:
- **Autenticación con tokens o JWT**.
- **Permisos personalizados** (`IsAuthenticated`, `IsAdminUser`, `AllowAny`).
- **Rate Limiting** con `throttling`.

Ejemplo de configuración de `throttling`:
```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}
```

---

## Testing en DRF
DRF proporciona herramientas para pruebas de APIs.

### Ejemplo de prueba con `APITestCase`
```python
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Usuario

class UsuarioAPITest(APITestCase):
    def test_obtener_lista_usuarios(self):
        response = self.client.get('/api/usuarios/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
```
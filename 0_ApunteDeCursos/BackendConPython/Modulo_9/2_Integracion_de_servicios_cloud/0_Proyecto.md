# Integracion S3 con Django

## 1. Crear un bucket en S3

1. Crear una cuenta en [aws](https://aws.amazon.com/es/free/)
2. Creacion del [bucket](https://s3.console.aws.amazon.com/s3)
    - Crear nuevo bucket.
      - Desmarcar Block all public access.
      - Aceptar cambios.
3. Crear un nuevo [grupo](https://us-east-1.console.aws.amazon.com/iamv2/home)
    - Crear nuevo Grupo.
      - Definir nombre del Grupo.
      - Definir como política AmazonS3FullAccess
4. Crear un nuevo [usuario](https://us-east-1.console.aws.amazon.com/iamv2/home)
    - Crear nuevo usuario.
      - Definir nombre del usuario.
      - Seleccionar grupo previamente creado.
      - Generar credenciales.
      - Local Code.

---

## 2. Configuracion inicial

1. Crear entorno virtual

```bash
python -m venv .venv
source env/bin/activate
```

2. Instalar dependencia

```bash
pip install django
pip install python-dotenv
pip install boto3
pip install django-storages
```

3. Crear el proyecto django

```bash
django-admin starproject
```

4. Agregar las credenciales de s3 en `settings.py`

```python
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''
AWS_S3_REGION_NAME = ''
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

---

## 3. Crear una vista

1. Crear un archivo `views.py` en el proyecto:

```python
from django.shortcuts import render
from storages.backends.s3boto3 import S3Boto3Storage

def index(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']

        storage = S3Boto3Storage()
        storage.save(
            f'image/{image.name}',
            image
        )

    return render(request, 'index.html', {
    })
```

2. Crear el template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subir Imagen</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
    <div class="container mx-auto mt-8 p-4 bg-white rounded-lg shadow-md">
        <h1 class="text-2x1 font-semibold mb-4">Subir Imagen</h1>
        <form method="POST" enctype="multipart/form-data" class="space-y-4">
            {% csrf_token %}
            <div class="flex items-center space-x-2">
                <label for="image" class="text-gray-600">Selecciona Imagen:</label>
                <input type="file" name="image" id="image" accept="image/*" class="py-2 px-4 border border-gray-300 rounded-md">
            </div>
            <button type="submit" class="bg-blue-500 hover:bg-blue600 text-white font-semibold py-2 px-4 rounded">Subir Imagen</button>
        </form>
        {% if image_url %}
        <h2 class="text-x1 mt-4">Imagen Cargada</h2>
        <img src="{{ image_url }}" alt="Imagen Cargada" class="mt-2 max-w-full">
        {% endif %}
    </div>
</body>
</html>
```

Con esto ya se pueden subir imagenes al s3

---

## 4. Crear un storage

1. Crear un archivo `storage.py`:

```python
from storages.backends.s3boto3 import S3Boto3Storage

class PublicMediaStorage(S3Boto3Storage):
    default_acl = 'public-read'
```

2. Modificar la vista:

```python
from django.shortcuts import render
from .storage import PublicMediaStorage

def index(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']

        storage = PublicMediaStorage()
        storage.save(
            f'image/{image.name}',
            image
        )

    return render(request, 'index.html', {
    })
```

---

## 5. Almacenar las rutas del archivo en la db

1. Crear una aplicacion `images`
2. Crear el modelo

```python
from django.db import models

from test_s3.storage import PublicMediaStorage

# Create your models here.
class ImageModel(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(storage=PublicMediaStorage(), upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
```

3. Modificar la vista:

```python
from django.shortcuts import render
from images.models import ImageModel

def index(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']

        aws_image = ImageModel.objects.create(
            name=image.name,
            image=image
        )

        print(f"Imagen subida a S3: {aws_image.image.url}")  # Imprimir la url


    return render(request, 'index.html', {
    })
```

4. Modificar `settings.py`

```python
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' <-- Parametro modificado
DEFAULT_FILE_STORAGE = 'test_s3.storage.PublicMediaStorage'
```

5. Realizar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```
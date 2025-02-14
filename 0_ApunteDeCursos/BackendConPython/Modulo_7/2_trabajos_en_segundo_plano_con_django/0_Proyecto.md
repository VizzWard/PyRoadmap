# Django para trabajos en segundo plano

---

### Ruta del proyectp

```commandline
cd .\0_ApunteDeCursos\BackendConPython\Modulo_7\2_trabajos_en_segundo_plano_con_django\live\
```

Comandos:

Inicializar el proyecto

```commandline
python manage.py runserver
```

Ejecutar celery (causa error en windows):

```commandline
celery -A live worker
```

Comando para windows:

```commandline
celery -A live worker --pool=solo --loglevel=info
```

Ejecutar flower:

```commandline
celery -A live flower --pool=solo --loglevel=info
```

---

### Comandos de vm

Iniciar redis:

```bash
redis-server
```

Comprobar conexion con redis:

```bash
redis-cli ping
```

Detener redis:

```bash
sudo /etc/init.d/redis-server stop
```

---

## Instalacion de dependencias

```commandline
pip install django
```

```commandline
pip install celery
```

```commandline
pip install redis
```

```commandline
pip install flower
```

---
## 0. Instalar Redis

https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/

## 1. Crear el proyecto de Django

```commandline
django-admin startproject live
```

## 2. Crear una app

```commandline
python manage.py startapp app1
```

Añadirla a settings.py

```python
INSTALLED_APPS = [
    'app1',
]
```

## 3. Crear la vista (vista basica para probar celery)

```python
from django.shortcuts import render

def index(request):

    mail_sent = False

    if request.method == 'POST':
        email = request.POST.get('email')

        mail_sent = True

    return render(request, 'index.html', {
        'mail_sent': mail_sent
    })
```

## 4. Crear la plantilla

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Landing Page</title>
        <!-- Agregar Estilos de Tailwind CSS -->
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    </head>
    <body class="bg-gray-100">
        <div class="min-h-screen flex items-center justify-center">
            <div class="w-3/4 bg-white p-8 rounded-lg shadow-lg">
                <h1 class="text-3x1 font-semibold mb-4">Bienvenido!</h1>
                <p class="text-gray-600 mb-8">Envia correos en segundo plano con Django</p>
                <form method="POST">
                    {% csrf_token %}
                    <div class="mb-4">
                        <label for="correo" class="block text-gray-600 text-sm font-semibold mb-2">Email:</label>
                        <input type="email" id="email" name="email" class="border rounded w-full py-2 px-3" required>
                    </div>
                    <button type="submit" class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded-full focus:outline-none">
                        Enviar Correo
                    </button>
                </form>
                {% if mail_sent %}
                <p class="mt-5 text-base text-slate-400">Correo Enviado Exitrosamente</p>
                {% endif %}
            </div>
        </div>
    </body>
</html>
```

- Redireccionar los templates a la carpeta templates en settings.py

```python
TEMPLATES = [
    {
        'DIRS': ['templates'],
    },
]
```

## 5. Configurar Celery

Crear un archivo llamado `celery.py` en la carpeta del proyecto (`live`)

```python
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'live.settings')

app = Celery('live')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
```

En el archivo `__init__.py` de la carpeta `live` añadir:

```python
from .celery import app as celery_app

__all__ = ('celery_app',)
```

En settings.py añadir (al final del archivo):

```python
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
```

## 6. Crear tareas

En la carpeta de la app crear un archivo llamado `tasks.py` - El decorador `@shared_task` es el que permite que la tarea sea reconocida por celery. 

```python
from celery import shared_task

@shared_task
def send_mail(to):
    print(f'Mail sent to {to}!')
    return to

@shared_task
def send_welcome_mail(to):
    print(f'Mail welcome sent to {to}!')
    return to

@shared_task
def send_subscription_mail(to):
    print(f'Mail subscription sent to {to}!')
    return to

@shared_task
def send_change_password_mail(*args):
    print(f'Mail change_password sent!')
```

---

## 7. Modificar la vista para pruebas de celery

### 1. Probar usa un proceso en segundo plano

1. En el archivo `views.py` importar la tarea, modificamos la vista, para que al usar el formulario de `index` se simule el envio de un correo en segundo plano. Esto con el uso de `send_mail.delay(email)`.

```python
from django.shortcuts import render
from .tasks import send_mail
def index(request):
    mail_sent = False

    if request.method == 'POST':
        email = request.POST.get('email')
        send_mail.delay(email)
        mail_sent = True

    return render(request, 'index.html', {
        'mail_sent': mail_sent
    })
```

2. Iniciar celery y redis:

```commandline
celery -A live worker --pool=solo --loglevel=info
```

```bash
redis-server
```

**Redis se ejecuta desde la terminal de la maquina virtual**

3. Inicar Django, y probar a mandar un correo, si no lanzo error los pasos se hicieron correctamente. Con esto usaremos un proceso en segundo plano, esto por medio de Celery, que a su vez se apoya de redis.

### 2. Uso de grupos de tareas

1. En el archivo `views.py` modificaremos la vista para que al enviar un correo, se ejecuten varios procesos.

```python
from django.shortcuts import render
rom .tasks import send_mail, send_welcome_mail, send_subscription_mail
from celery import group

def index(request):
    mail_sent = False

    if request.method == 'POST':
        email = request.POST.get('email')
        
        tasks = group(
            send_mail.s(email),  # s -> signature
            send_welcome_mail.s(email),
            send_subscription_mail.s(email)
        )
        
        tasks.apply_async()
        
        mail_sent = True

    return render(request, 'index.html', {
        'mail_sent': mail_sent
    })
```

Con esto, al mandar un correo, se ejecutaran todos los metodos que especificamos en el grupo de tareas.

### 3. Uso de cadena de tareas

1. En el archivo `views.py` modificaremos la vista para que al enviar un correo, se ejecuten varios procesos en cadena.

```python
from django.shortcuts import render
rom .tasks import send_mail, send_welcome_mail, send_subscription_mail
from celery import chain

def index(request):
    mail_sent = False

    if request.method == 'POST':
        email = request.POST.get('email')
        
        tasks = chain(
            send_mail.s(email),  # s -> signature
            send_welcome_mail.s(),
            send_subscription_mail.s()
        )
        
        tasks.apply_async()
        
        mail_sent = True

    return render(request, 'index.html', {
        'mail_sent': mail_sent
    })
```

Al igual que el grupo de tareas, se ejecutaran en cadena, pero en este caso, se ejecutaran uno tras otro. Con esto no nos hace falta pasarle arguntos a `send_welcome_mail` y `send_subscription_mail`. Ya que con retornar algun valor en `send_mail` se lo pasara a `send_welcome_mail`, y asi sucesivamente.

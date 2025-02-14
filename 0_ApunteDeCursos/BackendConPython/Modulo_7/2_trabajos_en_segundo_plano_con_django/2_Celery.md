# Celery y Redis en Django

## 1. ¿Qué es la Programación Asíncrona?
La programación asíncrona permite ejecutar tareas en segundo plano sin bloquear la ejecución del código principal. Esto mejora el rendimiento y la capacidad de respuesta de las aplicaciones.

En Python, se puede implementar programación asíncrona usando:
- Hilos (`threading`)
- Procesos (`multiprocessing`)
- AsyncIO (`asyncio`)
- Sistemas de colas de tareas como **Celery**

---
## 2. ¿Qué es Celery?
Celery es una biblioteca de Python que permite ejecutar tareas asíncronas en segundo plano, basándose en colas de tareas distribuidas. Es útil para:
- Enviar correos electrónicos en segundo plano
- Procesar archivos grandes sin bloquear la aplicación
- Realizar tareas programadas periódicamente

Celery usa un *message broker* para gestionar las colas de tareas. Uno de los más utilizados es **Redis**.

---
## 3. ¿Cómo funciona Celery?
1. **Productor:** La aplicación Django agrega tareas a la cola.
2. **Message Broker (Redis):** Almacena y gestiona las tareas en la cola.
3. **Trabajador (Worker):** Un proceso en segundo plano ejecuta las tareas.
4. **Resultados (Backend opcional):** Se pueden almacenar los resultados de las tareas en Redis, bases de datos o archivos.

---
## 4. ¿Qué es Redis y cómo funciona?
Redis es una base de datos en memoria utilizada como:
- **Almacenamiento en caché**
- **Sistema de colas de mensajes** (message broker para Celery)
- **Almacén de datos clave-valor**

Celery usa Redis para enviar y recibir mensajes entre la aplicación y los *workers*.

---
## 5. Primeros Pasos con Celery en Django
### Instalación
```bash
pip install celery redis
```

### Configuración en `settings.py`
```python
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
```

### Crear un archivo `celery.py` en tu aplicación Django
```python
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tu_proyecto.settings')

app = Celery('tu_proyecto')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```

### Definir una tarea en `tasks.py`
```python
from celery import shared_task

@shared_task
def suma(a, b):
    return a + b
```

### Ejecutar Celery Worker
```bash
celery -A tu_proyecto worker --loglevel=info
```

---
## 6. Decoradores y Utilidades de Celery
### Decorador `@shared_task`
Define tareas reutilizables.
```python
@shared_task
def my_task():
    return "Ejecutando tarea en segundo plano"
```

### Decorador `@task`
Ofrece más opciones de configuración.
```python
from celery import task

@task(bind=True, max_retries=3)
def retry_task(self):
    try:
        # Código que puede fallar
        pass
    except Exception as e:
        self.retry(exc=e, countdown=10)
```

### `apply_async`
Permite ejecutar tareas con opciones avanzadas.
```python
suma.apply_async(args=[4, 5], countdown=10)
```

---
## 7. Grupos, Cadenas y Chords en Celery
### Grupos (`group`)
Ejecuta varias tareas en paralelo y devuelve los resultados cuando todas terminan.
```python
from celery import group

group_tasks = group([suma.s(2, 2), suma.s(4, 4)])
result = group_tasks.apply_async()
print(result.get())
```

### Cadenas (`chain`)
Ejecuta tareas en secuencia, pasando el resultado de una a la siguiente.
```python
from celery import chain

chain_tasks = chain(suma.s(2, 2) | suma.s(4))
result = chain_tasks()
print(result.get())
```

### Chords (`chord`)
Ejecuta tareas en paralelo y luego una tarea final cuando todas terminen.
```python
from celery import chord

callback_task = suma.s(10)
chord_tasks = chord([suma.s(2, 2), suma.s(4, 4)], callback_task)
result = chord_tasks()
print(result.get())
```

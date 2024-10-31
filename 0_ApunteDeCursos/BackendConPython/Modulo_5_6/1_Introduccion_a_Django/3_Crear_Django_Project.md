# Django 

- Primero ir a la ruta de la carpeta deseada, en mi caso es:

```commandline
cd .\0_ApunteDeCursos\BackendConPython\Modulo5\1_Introduccion_a_Django\
```

- En el directorio deseado, ejecutar el comando:

```commandline
django-admin startproject myproject .
```

- Para ejecutar el servidor:

```commandline
python manage.py runserver
```

## Migrations

- Las migraciones son una manera incremental que tenemos para actualizar el esquema o como esta formada la base de datos.
- Django ya viene con una serie de migraciones listas para aplicar pero tu puedes crear las tuyas a medida que vas construyendo tu proyecto.

```commandline
python manage.py makemigrations
```

```commandline
python manage.py migrate
```

```commandline
python manage.py showmigrations
```


- Junto con el proyecto se crea un panel de administracion, para crear un usuario y acceder ejecutamos el comando:

```commandline
python manage.py createsuperuser
```
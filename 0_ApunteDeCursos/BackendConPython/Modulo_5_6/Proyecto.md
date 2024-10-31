Para los modulos 5 y 6, se va a crear un proyecto que se ira creando a lo largo de las clases:

- [Tienda](Proyecto)

Los pasos seguidos están en los archivos:

__Modulo 5:__

- [Clase_1](Proyecto_Clase_1.md)
- [Clase_2](Proyecto_Clase_2.md)

__Modulo 6:__

- [Clase_3](Proyecto_Clase_3.md)
- [Clase_4](Proyecto_Clase_1.md)

Ruta del proyecto:

```commandline
cd .\0_ApunteDeCursos\BackendConPython\Modulo5\Proyecto\
```

Iniciar el servidor (local):

```commandline
python manage.py runserver --settings=settings.local
```

Makemigrate:

```commandline
python manage.py makemigrations --settings=settings.local
```

Migrate:
```commandline
python manage.py migrate --settings=settings.local
```
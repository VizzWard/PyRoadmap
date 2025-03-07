# Proyecto

> Para los modulos 5 y 6, se va a crear un proyecto que sé irá creando a lo largo de las clases:


Carpeta del proyecto:

- [Tienda](Proyecto)

Los pasos seguidos están en los archivos respectivos a cada módulo:

__Modulo 5:__

- [Clase_1](Proyecto_Clase_1.md)
- [Clase_2](Proyecto_Clase_2.md)

__Modulo 6:__

- [Clase_3](Proyecto_Clase_3.md)
- [Clase_4](Proyecto_Clase_4.md)

## Comandos comunes

Ruta del proyecto:

```commandline
cd .\0_ApunteDeCursos\BackendConPython\Modulo_5_6\Proyecto\
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

Tests:
```commandline
python manage.py test --settings=settings.local
```

Test one:
```commandline
python manage.py test $(TEST_NAME) --settings=settings.local
```

Test app accounts:
```commandline
python manage.py test accounts --settings=settings.local -v 2
```

Test app products:
```commandline
python manage.py test products.tests --settings=settings.local -v 2
```

shellplus:
```commandline
python manage.py shell_plus --ipython --settings=settings.local
```
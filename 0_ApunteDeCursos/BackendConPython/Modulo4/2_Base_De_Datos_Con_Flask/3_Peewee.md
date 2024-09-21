# Peewee

Peewee es un ORM (Object-Relational Mapping) pequeño y expresivo para Python. Está diseñado para ser simple, intuitivo y flexible. Peewee soporta SQLite, MySQL y PostgreSQL, lo que lo hace versátil para diferentes proyectos.

Algunas características clave de Peewee incluyen:

1. Sintaxis pythónica para definir modelos y realizar consultas
2. Soporte para relaciones (uno a muchos, muchos a muchos)
3. Soporte para migraciones de base de datos
4. Capacidad de escribir consultas SQL personalizadas cuando sea necesario

## Tipos de campos comunes en Peewee

1. **CharField**: 
   - Para cadenas de texto cortas.
   - Ejemplo: `nombre = CharField(max_length=100)`

2. **TextField**: 
   - Para texto largo sin límite de longitud.
   - Ejemplo: `descripcion = TextField()`

3. **IntegerField**: 
   - Para números enteros.
   - Ejemplo: `edad = IntegerField()`

4. **FloatField**: 
   - Para números de punto flotante.
   - Ejemplo: `altura = FloatField()`

5. **DecimalField**: 
   - Para números decimales precisos (útil para dinero).
   - Ejemplo: `precio = DecimalField(max_digits=10, decimal_places=2)`

6. **BooleanField**: 
   - Para valores verdadero/falso.
   - Ejemplo: `activo = BooleanField(default=True)`

7. **DateTimeField**: 
   - Para fecha y hora.
   - Ejemplo: `creado_en = DateTimeField(default=datetime.datetime.now)`

8. **DateField**: 
   - Solo para fecha.
   - Ejemplo: `fecha_nacimiento = DateField()`

9. **TimeField**: 
   - Solo para hora.
   - Ejemplo: `hora_apertura = TimeField()`

10. **ForeignKeyField**: 
    - Para relaciones uno a muchos.
    - Ejemplo: `categoria = ForeignKeyField(Categoria, backref='productos')`

11. **ManyToManyField**: 
    - Para relaciones muchos a muchos.
    - Ejemplo: `tags = ManyToManyField(Tag, backref='productos')`

12. **BlobField**: 
    - Para datos binarios grandes.
    - Ejemplo: `imagen = BlobField()`

13. **UUIDField**: 
    - Para almacenar identificadores únicos universales (UUID).
    - Ejemplo: `id = UUIDField(primary_key=True)`

Nota: Algunos de estos campos pueden tener argumentos adicionales como `null`, `index`, `unique`, etc., para especificar más características del campo.

Estos son algunos de los tipos de campos más comunes en Peewee. Cada uno está diseñado para manejar diferentes tipos de datos y tiene sus propias características y opciones.

Al usar estos campos, puedes definir la estructura de tus modelos de manera que representen adecuadamente los datos que quieres almacenar en tu base de datos. Por ejemplo:

```python
from peewee import *

db = SqliteDatabase('mi_tienda.db')

class Producto(Model):
    nombre = CharField(max_length=100)
    descripcion = TextField()
    precio = DecimalField(max_digits=10, decimal_places=2)
    en_stock = BooleanField(default=True)
    creado_en = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
```
# DML (Data Manipulation Language)

## SELECTS

Queries que permiten leer todos los campos para cada una de la tablas creadas previamente.

- `SELECT *` Indica que se leerán todos los campos de la tabla.
- `FROM` Luego de este texto se especifica el nombre de la tabla (o tablas) a leer.

```sql
SELECT *
FROM Usuario;

SELECT *
FROM Historial_Conexion;

SELECT *
FROM Menu;

SELECT *
FROM Menu_Usuario;
```

- `SELECT Nombre, Apellido` para leer unicamente los campos Nombre y Apellido. Los campos se separan por comas.

```sql
SELECT Nombre, Apellido
FROM Usuario;
```

- `Nombre Primer_Nombre` _Nombre_ es el nombre del campo en la tabla, _Primer_Nombre es un alias para el campo, los alias es otra forma de referise al campo, son opcionales.
- `Usuario U` La letra _U_ es un alias para la tabla Usuario, los alias son muy comunes cuando en una misma consulta hay varias tablas.
- `WHERE` Aca se especifican los filtros, para solo obtener las filas que cumplan las condiciones especificadas.
- `Activo = 1` para filtrar solo las filas que en la columna Activo tengan valor igual a 1.
- `AND` para unir varios filtros dentro de la clausula `WHERE`.
- `Fecha_Nacimiento IS NULL` para filtrar solo las filas que en la columna Fecha_Nacimiento tengan valor igual a NULL.

```sql
SELECT Nombre Primer_Nombre, Apellido
FROM Usuario U
WHERE Activo = 1
AND Fecha_Nacimiento IS NULL;
```

- `ORDER BY` Luego de este texto se especifica el nombre del campo (o campos) para aplicar el ordenamiento. Se leer el hsitorial de conexion ordenados por dirección IP de forma ascendente.

```sql
SELECT *
FROM Historial_Conexion
ORDER BY IP;
```

- `DESC` Indica que el ordenamiento será descendente.
- `ASC` Indica que el ordenamiento será ascendente, si no se especifica ASC o DESC, por default el ordenamiento será ascendente. Se leer el hsitorial de conexion ordenados por Fecha y Hora de forma descendente.

```sql
SELECT *
FROM Historial_Conexion
ORDER BY Fecha_Hora DESC;
```

Podemos leer por ejemplo unicamente 3 filas de la tabla Menu por medio de la instrucción LIMIT.

```sql
SELECT *
FROM Menu
LIMIT 3;
```

- `CREATE VIEW` Para crear una vista, luego de AS se coloca el query de tipo SELECT que es lo que la vista mostrará.
- La vista se puede utilizar de la misma forma que cualquier tabla. Se le puede agregar mas filtros en el WHERE si asi se deseara.

```sql
CREATE VIEW Usuarios_Activos AS
    SELECT *
    FROM Usuario
    WHERE Activo = 1;

SELECT *
FROM Usuarios_Activos;****
```

## INSERTS

Distintos ejemplos de como usar la inserción de datos.

- `INSERT INTO` Luego de este texto debe de ir el nombre de la tabla.
- Entre los parentesis se incluye la lista de campos a insertar.
- `VALUES` Luego de este texto deben de ir los valores de los campos que se especificarón antes, en el mismo orden.
- El campo ID no se especifica, entonces la clausula AUTO_INCREMENT creará el valor correspondiente de form automatica.

```sql
INSERT INTO Menu 
(Titulo, Descripcion, URL, Activo)
VALUES ('Configuración', 'Menu de configuración', '/Configuración', 1);
```

- El campo `ID` si se especifica con un valor que ya existe, por lo que se generará un error.

```sql
INSERT INTO Menu 
(ID, Titulo, Descripcion, URL, Activo)
VALUES (1, 'Contraseña', 'Configuración de contraseña', '/Configuración/Contraseña', 1);
```

- El campo `ID` si se especifica, entonces la clausula se guardará con ese valor. No se tomará en cuenta el `AUTO_INCREMENT`.

```sql
INSERT INTO Menu 
(ID, Titulo, Descripcion, URL, Activo)
VALUES (5, 'Contraseña', 'Configuración de contraseña', '/Configuración/Contraseña', 1);
```

- Como se estan insertando valores para todas las columnas de la tabla, no es obligatorio especificar la lista de campos.
- Los valores deben de ir en el mismo orden en que se especificaron los campos en el `CREATE TABLE`.

```sql
INSERT INTO Menu 
VALUES (3, 'Tema', 'Configuración de tema oscuro o claro', '/Configuración/Tema', 1);
```

- Como se estan insertando un valor 5 en el campo Activo el cúal no es valido segun el `CHECK CONSTRAINT` que se creó, el query dará un error.

```sql
INSERT INTO Menu 
(Titulo, Descripcion, URL, Activo)
VALUES ('Tipo Cuenta', 'Configuración de tipo de cuenta', '/Configuración/TipoCuenta', 5);
```

- Luego de corregir el valor del campo Activo el query debera ejecutarse satisfactoriamente.

```sql
INSERT INTO Menu 
(Titulo, Descripcion, URL, Activo)
VALUES ('Tipo Cuenta', 'Configuración de tipo de cuenta', '/Configuración/TipoCuenta', 0);
```

Creación de una tabla temporal, la cual será una copia exacta de la tabla Menu, sobre la tabla temporal se puede hacer cualquier operación, podemos eliminar la tabla con DROP TABLE, o al finalizar la sesión, en automatico la tabla será eliminada.

- Inserción de 2 filas nuevas, sobre la tabla temporal `Menu_Copia`.

```sql
CREATE TEMPORARY TABLE Menu_Copia SELECT * FROM Menu;

INSERT INTO Menu_Copia 
(Titulo, Descripcion, URL, Activo)
VALUES ('Asociar Facebook', 'Asociar cuenta de Facebook', '/Configuración/Facebook', 1);

INSERT INTO Menu_Copia 
(Titulo, Descripcion, URL, Activo)
VALUES ('Asociar Google', 'Asociar cuenta de Google', '/Configuración/Google', 1);
```

- La tabla `Menu_Copia` contiene todos los valores de la tabla Menu y adicional las 2 filas recien insertadas.
- Se filtran las filas que el texto del campo Titulo comienza con el texto Asociar, para eso se usa la clasula `LIKE`.
- `%` Indica que alli puede ir cualquier texto.

```sql
SELECT Titulo, Descripcion, URL, Activo
FROM Menu_Copia
WHERE Titulo LIKE 'Asociar%'
```

- Ahora la clausula `INSERT` ya no contiene la instrucción `VALUES`, en lugar de eso, se insertarán todas filas que sean resultado de la clasula `SELECT`.

```sql
INSERT INTO Menu (Titulo, Descripcion, URL, Activo)
SELECT Titulo, Descripcion, URL, Activo
FROM Menu_Copia
WHERE Titulo LIKE 'Asociar%'
```

## UPDATES

Actualización de todos los registros de la tabla Menu, el campo Activo se le asigna el valor 1.

```sql
UPDATE Menu
SET Activo = 1;
```

Actualización de todos los registros de la tabla Menu, el campo Activo se le asigna el valor 0 y el campo URL se cambian todos sus caracteres a minusculas con la funcion `LOWER`.

```sql
UPDATE Menu
SET Activo = 0, URL = LOWER(URL);
```

Actualización de un único registro de la tabla Menu, el campo Activo se le asigna el valor 1 solo para la fila que tiene el campo ID igual a 1.

```sql
UPDATE Menu
SET Activo = 1
WHERE ID = 1;
```

Actualización de ningun registro de la tabla Menu, el campo Activo se trata de asignar el valor 1 solo para la fila que tiene el campo ID igual a 500, pero no hay ninguna fila con ese valor, el query se ejecuta satisfactoriamente dando como resultado ninguna fila actualizada.

```sql
UPDATE Menu
SET Activo = 1
WHERE ID = 500;
```

Actualización de varios registros de la tabla Menu, el campo Activo se le asigna el valor 1 solo para la fila que el campo ID esta contenido en la lista de valores (2, 3, 4).

```sql
UPDATE Menu
SET Activo = 1
WHERE ID IN (2, 3, 4)
```

Actualización de todos los registros de la tabla Menu, al campo Activo se le trata de asignar el valor 5, pero como la tabla tiene un `CHECK CONSTRAINT` que no permite esos valores, entonces se generará un error.

```sql
UPDATE Menu
SET Activo = 5;
```

## DELETES

Eliminación de todos los registros de la tabla Historial_Conexion. * Es muy importante ser cuidados al momento de ejecutar un query `DELETE` para no eliminar registros que no se debian eliminar.

```sql
DELETE 
FROM Historial_Conexion;
```

Eliminación de todos los registros de la tabla Historial_Conexion.

> Es muy importante ser cuidados al momento de ejecutar un query `DELETE` para no eliminar registros que no se debian eliminar. `WHERE 1 = 1` es equivalente a que no haya ninguna condición.

```sql
DELETE 
FROM Historial_Conexion;

DELETE 
FROM Historial_Conexion
WHERE 1 = 1;
```

`TRUNCATE TABLE` Borra todos los datos de una tabla, es parecido a ejecutar un `DROP TABLE` seguido de un `CREATE TABLE`.

- El `DELETE` borrar las filas una por una, `TRUNCATE TABLE` borra todas las filas de un solo, por lo que es mas rapido.

```sql
TRUNCATE TABLE Historial_Conexion;
```

Eliminación de varios registros de la tabla Menu.

```sql
DELETE 
FROM Menu
WHERE ID >= 7
AND ID <= 8;
```
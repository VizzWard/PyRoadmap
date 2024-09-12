# Categorización de comandos SQL

Los comandos SQL se pueden clasificar en cinco tipos principales, cada uno de los cuales tiene un propósito distinto en la gestión de bases de datos. Comprender estas categorías es esencial para operaciones de bases de datos eficientes y efectivas. Los comandos SQL se pueden clasificar en cinco tipos principales:

## Comandos del lenguaje de definición de datos (DDL)

DDL, o lenguaje de definición de datos, es un subconjunto de SQL que se utiliza para definir y administrar la estructura de los objetos de la base de datos. Los comandos DDL normalmente se ejecutan una vez para configurar el esquema de la base de datos.

Los comandos DDL se utilizan para definir, modificar y administrar la estructura de los objetos de la base de datos, como tablas, índices y restricciones. Algunos comandos DDL comunes incluyen:

- CREAR TABLA: Se utiliza para crear una nueva tabla.
- ALTER TABLE: Se utiliza para modificar la estructura de una tabla existente.
- DROP TABLE: Se utiliza para eliminar una tabla.
- CREAR ÍNDICE: Se utiliza para crear un índice en una tabla, mejorando el rendimiento de la consulta.

Los comandos DDL desempeñan un papel crucial en la definición del esquema de la base de datos.

## Comandos del lenguaje de manipulación de datos (DML)

Los comandos DML se utilizan para recuperar, insertar, actualizar y eliminar datos en la base de datos. Los comandos DML comunes incluyen:

- SELECCIONAR: Se utiliza para recuperar datos de una o más tablas.
- INSERTAR: Se utiliza para agregar nuevos registros a una tabla.
- ACTUALIZACIÓN: Se utiliza para modificar registros existentes en una tabla.
- ELIMINAR: Se utiliza para eliminar registros de una tabla.

Los comandos DML son esenciales para administrar los datos almacenados en una base de datos.

## Comandos del lenguaje de control de datos (DCL)

Los comandos DCL se utilizan para gestionar la seguridad de la base de datos y el control de acceso. Los dos comandos DCL principales son:

- GRANT: Se utiliza para otorgar privilegios específicos a usuarios o roles de la base de datos.
- REVOKE: Se utiliza para revocar privilegios otorgados previamente.

Los comandos DCL garantizan que solo los usuarios autorizados puedan acceder y modificar la base de datos.

## Comandos del lenguaje de control de transacciones (TCL)

Los comandos TCL se utilizan para gestionar transacciones de bases de datos, garantizando la integridad de los datos. Los comandos clave de TCL incluyen:

- COMMIT: confirma una transacción y guarda los cambios de forma permanente.\
- ROLLBACK: Deshace los cambios realizados durante una transacción.
- SAVEPOINT: establece un punto dentro de una transacción al que luego puede retroceder.

Los comandos TCL son vitales para mantener la coherencia de los datos en una base de datos.

## Comandos del lenguaje de consulta de datos (DQL)

Los comandos DQL se centran exclusivamente en recuperar datos de la base de datos. Mientras que la SELECT La declaración es el comando DQL más destacado y desempeña un papel fundamental en la extracción y presentación de datos de una o más tablas según criterios específicos. Los comandos DQL le permiten obtener información valiosa a partir de los datos almacenados.

## Comandos DDL comunes

### Crear mesa

El comando CREATE TABLE se utiliza para definir una nueva tabla en la base de datos. He aquí un ejemplo:

```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    ...
);
```

Este comando define una tabla llamada "Empleados" con columnas para ID de empleado, nombre, apellido y más.

### ALTERAR MESA

El comando ALTER TABLE le permite modificar una tabla existente. Por ejemplo, puede agregar una nueva columna o modificar el tipo de datos de una columna existente:

```sql
ALTER TABLE Employees
ADD Email VARCHAR(100);
```

Esto agrega una columna "Correo electrónico" a la tabla "Empleados".

### TABLA DE GOTA

El comando DROP TABLE elimina una tabla de la base de datos:

```sql
DROP TABLE Employees;
```

Esto elimina la tabla “Empleados” y todos sus datos.

### CREAR ÍNDICE

El comando CREATE INDEX se utiliza para crear un índice en una o más columnas de una tabla, mejorando el rendimiento de la consulta:

```sql
CREATE INDEX idx_LastName ON Employees(LastName);
```

Esto crea un índice en la columna "Apellido" de la tabla "Empleados".

## Comandos DML comunes

### SELECCIONAR

La declaración SELECT recupera datos de una o más tablas según criterios específicos:

```sql
SELECT FirstName, LastName FROM Employees WHERE Department = 'Sales';
```

Esta consulta selecciona los nombres y apellidos de los empleados del departamento de “Ventas”.

### INSERT

La declaración INSERT agrega nuevos registros a una tabla:

```sql
INSERT INTO Employees (FirstName, LastName, Department) VALUES ('John', 'Doe', 'HR');
```

Esto inserta un nuevo registro de empleado en la tabla "Empleados".

### ACTUALIZAR

La declaración UPDATE modifica los registros existentes en una tabla:

```sql
UPDATE Empleados SET Salario = Salario * 1.1 WHERE Departamento = 'Ingeniería';
```

Esto aumenta el salario de los empleados del departamento de “Ingeniería” en un 10%.

### BORRAR

La declaración DELETE elimina registros de una tabla:

```sql
DELETE FROM Employees WHERE Department = 'Finance';
```

Esto elimina empleados del departamento de "Finanzas".

## Comandos DCL comunes

### GRANT

El comando GRANT se utiliza para otorgar privilegios específicos a usuarios o roles de la base de datos:

```sql
GRANT SELECT, INSERT ON Employees TO HR_Manager;
```

Esto otorga al rol "HR_Manager" los privilegios para seleccionar e insertar datos en la tabla "Empleados".

### REVOCAR

El comando REVOKE se utiliza para revocar privilegios otorgados previamente:

```sql
REVOKE DELETE ON Customers FROM Sales_Team;
```

Esto revoca el privilegio de eliminar datos de la tabla "Clientes" del rol "Sales_Team".

## Comandos TCL comunes

### COMETER

El comando COMMIT se utiliza para guardar los cambios realizados durante una transacción en la base de datos de forma permanente:

```sql
BEGIN;
-- SQL statements
COMMIT;
```

Este ejemplo comienza una transacción, realiza declaraciones SQL y luego confirma los cambios en la base de datos.

### RETROCEDER

El comando ROLLBACK se utiliza para deshacer los cambios realizados durante una transacción:

```sql
BEGIN;
-- SQL statements
ROLLBACK;
```

Este ejemplo inicia una transacción, realiza declaraciones SQL y luego revierte los cambios, restaurando la base de datos a su estado anterior.

### PUNTO DE GUARDADO

El comando SAVEPOINT le permite establecer un punto dentro de una transacción al que luego puede retroceder:

```sql
BEGIN;
-- SQL statements
SAVEPOINT my_savepoint;
-- More SQL statements
ROLLBACK TO my_savepoint;
```

Este ejemplo crea un punto de guardado y luego regresa a ese punto, deshaciendo algunos de los cambios de la transacción.

## Comandos DQL comunes

### Sentencia SELECT

El SELECT La declaración es la piedra angular de DQL. Le permite recuperar datos de una o más tablas en una base de datos. Aquí está la sintaxis básica del SELECT declaración:

```sql
SELECT column1, column2, ...FROM table_nameWHERE condition;
```

- column1, column2,…: Las columnas que desea recuperar de la tabla.
- table_name: El nombre de la tabla de la que desea recuperar datos.
- condition (opcional): la condición que especifica qué filas recuperar. Si se omite, se recuperarán todas las filas.

### Palabra clave DISTINTA

El DISTINCT La palabra clave se utiliza junto con la SELECT declaración para eliminar filas duplicadas del conjunto de resultados. Garantiza que solo se devuelvan valores únicos.

```sql
SELECT DISTINCT CountryFROM Customers;
```

Esta consulta recupera una lista de países únicos de la tabla "Clientes", eliminando entradas duplicadas.

### ORDEN POR Cláusula

El ORDER BY La cláusula se utiliza para ordenar el conjunto de resultados en función de una o más columnas en orden ascendente o descendente.

```sql
SELECT ProductName, UnitPriceFROM ProductsORDER BY UnitPrice DESC;
```

Esta consulta recupera nombres de productos y precios unitarios de la tabla "Productos" y los clasifica en orden descendente de precio unitario.
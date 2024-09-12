# Tipos de Objetos en SQL

## Tablas

Las tablas son el objeto principal en una base de datos. Son donde se almacenan los datos en filas y columnas.

```sql
CREATE TABLE empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    salario DECIMAL(10, 2),
    fecha_contratacion DATE
);
```

## Constraints (Restricciones)

Las restricciones son reglas que aplican a las columnas de una tabla para garantizar la integridad de los datos.

- PRIMARY KEY: Identifica de manera única cada fila en la tabla.
- FOREIGN KEY: Asegura que los valores en una columna coincidan con valores en otra tabla.
- NOT NULL: Asegura que una columna no tenga valores nulos.
- UNIQUE: Garantiza que todos los valores en una columna sean únicos.
- CHECK: Impone una condición sobre los valores de una columna.

```sql
CREATE TABLE departamentos (
    id INT PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE,
    jefe_id INT,
    FOREIGN KEY (jefe_id) REFERENCES empleados(id),
    CHECK (nombre <> '')
);
```

## Vistas

Las vistas son tablas virtuales basadas en el resultado de una consulta SELECT. No almacenan datos por sí mismas, solo muestran datos.

```sql
CREATE VIEW empleados_con_alto_salario AS
SELECT nombre, salario
FROM empleados
WHERE salario > 5000;
```

## Triggers

Un trigger es un bloque de código SQL que se ejecuta automáticamente cuando ocurre un evento (INSERT, UPDATE, DELETE) en una tabla.

```sql
CREATE TRIGGER salario_actualizado
AFTER UPDATE ON empleados
FOR EACH ROW
WHEN (NEW.salario <> OLD.salario)
BEGIN
    INSERT INTO historial_salarios (empleado_id, salario_anterior, nuevo_salario, fecha)
    VALUES (NEW.id, OLD.salario, NEW.salario, CURRENT_DATE);
END;
```

## Funciones

Las funciones son bloques de código reutilizables que pueden recibir parámetros y devolver un valor. A diferencia de los procedimientos, las funciones siempre devuelven un valor.

```sql
CREATE FUNCTION obtener_salario(id_empleado INT)
RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE salario DECIMAL(10, 2);
    SELECT salario INTO salario FROM empleados WHERE id = id_empleado;
    RETURN salario;
END;
```

## Procedimientos

Los procedimientos almacenados son similares a las funciones, pero no están obligados a devolver un valor. Se pueden usar para realizar operaciones complejas en la base de datos.

```sql
CREATE PROCEDURE actualizar_salario(
    IN id_empleado INT,
    IN nuevo_salario DECIMAL(10, 2)
)
BEGIN
    UPDATE empleados
    SET salario = nuevo_salario
    WHERE id = id_empleado;
END;
```
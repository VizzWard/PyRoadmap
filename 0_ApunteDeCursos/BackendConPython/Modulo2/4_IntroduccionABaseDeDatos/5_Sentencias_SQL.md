# Sentencias SQL

## SELECT (para consultar datos)

La sentencia SELECT se usa para recuperar datos de una tabla.

```sql
SELECT nombre, salario FROM empleados WHERE salario > 3000;
```

## INSERT (para insertar datos)

La sentencia INSERT se usa para agregar nuevas filas a una tabla.

```sql
INSERT INTO empleados (id, nombre, salario, fecha_contratacion)
VALUES (1, 'Juan Pérez', 4500.50, '2023-09-01');
```

## UPDATE (para actualizar datos)

La sentencia UPDATE se usa para modificar los datos existentes en una tabla.

```sql
UPDATE empleados
SET salario = 5000
WHERE id = 1;
```

## DELETE (para eliminar datos)

La sentencia DELETE se usa para eliminar una o más filas de una tabla.

```sql
DELETE FROM empleados WHERE id = 1;
```
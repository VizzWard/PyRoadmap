# Funciones de Agregacion

Realizan operaciones sobre un grupo o un set de datos. Comúnmente son utilizadas con la cláusula `GROUP BY` para generar grupos y resultados sobre esos grupos.

## Algunas funciones comunes

- `AVG`: Para promediar valores.
- `COUNT`: Para contar registros.
- `COUNT(DISTINCT)`: Para contar registros unicos.
- `MAX`: Devuelve el valor máximo.
- `MIN`: Devuelve el valor mínimo.
- `SUM`: Para sumar valores.
- `STD`: Devuelve la desviación estándar.
- `JSON_ARRAYAGG()`: Agrupa un set de datos en un JSON array.
- `JSON_OBJECTAGG()`: Una fila de datos es retornada en formato JSON.

Ejemplos:

1. Seleccionamos el total de registros en la tabla customers, para obtener otra métrica, solo cambiamos el COUNT por la función que necesitemos.

```sql
SELECT COUNT(*)
FROM customers;
```

2. Seleccionamos el total de registros en la tabla customers, pero en lugar de un total general, es el total agrupado por el campo country.

```sql
SELECT country, COUNT(*)
FROM customers
GROUP BY country;
```

## GROUP BY

Es posible utilizar más de una función de agregación en un mismo query. Todos los campos individuales que están junto a la función de agregación en la clausula `SELECT` debe ir tambien en la clausula `GROUP BY`.

```sql
SELECT country, AVG(creditLimit), MIN(creditLimit), MAX(creditLimit)
FROM customers
GROUP BY country;

SELECT country, state, city, AVG(creditLimit), MIN(creditLimit), MAX(creditLimit)
FROM customers
GROUP BY country, state, city;
```

## Identificar duplicados con COUNT

La función `COUNT` puede ser utilizada para contar duplicados.

```sql
SELECT COUNT(firstName), COUNT(DISTINCT firstName)
FROM employees;

SELECT firstName, COUNT(firstName)
FROM employees
GROUP BY firstName
HAVING COUNT(firstName) > 1;
```

## Having

A diferencia de la cláusula `WHERE`, la cláusula `HAVING` se refiere a grupos, no a filas individuales. Se aplica a los resultados después de haberse agrupado (en la cláusula `GROUP BY`). Tiene la ventaja de permitir el uso de funciones establecidas tales como `AVG` o `SUM`, que no se pueden utilizar en la cláusula WHERE a menos que se coloquen dentro de una subconsulta.

```sql
SELECT country, state, city, AVG(creditLimit), MIN(creditLimit), MAX(creditLimit)
FROM customers
WHERE customerNumber BETWEEN 100 AND 500
AND creditLimit > 100000
GROUP BY country, state, city
HAVING MIN(creditLimit) >= 100000;
```

## ORDER BY

Toma la salida de la cláusula `SELECT` y ordena los resultados de la consulta de acuerdo con las especificaciones dentro de la cláusula `ORDER BY`. Se especifica una o más columnas y las palabras clave opcionales `ASC` o `DESC` (una por columna). Si no se especifica la palabra clave, setoma `ASC`.

- `ASC`: Orden ascendente.
- `DESC`: Orden descendente.

```sql
SELECT country, state, city, AVG(salesRepEmployeeNumber), MIN(creditLimit)
FROM customers
WHERE customerNumber BETWEEN 100 AND 500
AND creditLimit > 0
GROUP BY country, state, city
HAVING MIN(creditLimit) >= 100000
ORDER BY country, state DESC, city ASC, MIN(creditLimit);
```

## Objetos JSON

```sql
SELECT JSON_OBJECT('Name', customerName, 'Country', country, 'City', city) Json
FROM customers
ORDER BY customerName;

SELECT country, JSON_OBJECTAGG(customerName, city) Json
FROM customers
GROUP BY country
ORDER BY country;

SELECT JSON_ARRAYAGG(JSON_OBJECT('Name', customerName, 'Country', country, 'City', city)) Json
FROM customers;
```
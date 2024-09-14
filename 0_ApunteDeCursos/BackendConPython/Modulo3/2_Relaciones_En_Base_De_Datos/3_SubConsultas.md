# SubConsultas

Proporcionan una forma de acceder a datos en múltiples tablas con una sola consulta. Puede agregarse a una instrucción `SELECT`, `INSERT`, `UPDATE` o `DELETE` para permitir a esa instrucción utilizar los resultados de la consulta arrojados por la subconsulta. La subconsulta es esencialmente una instrucción SELECT incrustada que actúa como una puerta de entrada a los datos en una segunda tabla.

Se pueden en dos categorías generales:

- Las que pueden arrojar múltiples filas
- Las que pueden arrojar solamente un valor

Subconsulta que retorna múltiples filas:

```sql
SELECT * 
FROM customers
WHERE customerNumber BETWEEN 100 AND 500
AND (customerName LIKE 'A%'
    OR customerName LIKE '_A%')
AND addressLine1 IS NOT NULL
AND addressLine2 IS NULL
AND customerNumber IN (
	SELECT DISTINCT customerNumber
	FROM orders 
	WHERE orderDate >= '2005-01-01'
);
```

Subconsultas que retornan solamente un valor:

```sql
SELECT * 
FROM customers
WHERE creditLimit > (
	SELECT MAX(amount)
	FROM payments
);

SELECT *, (SELECT MAX(amount) FROM payments) MaxPayment
FROM customers;
```

El resultado de la subconsulta tambien puede ser utilizado como que fuera una tabla asignandole un alias y seleccionar datos de ese resultado:

```sql
SELECT *
FROM (
	SELECT customerNumber, CustomerName
	FROM customers
    WHERE customerNumber BETWEEN 100 AND 500
	AND (customerName LIKE 'A%'
		OR customerName LIKE '_A%')
	AND addressLine1 IS NOT NULL
	AND addressLine2 IS NULL
) Subquery;
```
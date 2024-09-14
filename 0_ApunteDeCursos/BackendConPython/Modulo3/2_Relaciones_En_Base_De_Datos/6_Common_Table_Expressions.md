# Commons Table Expressions

Es un conjunto de resultados con nombre temporal al que puede hacer referencia dentro de una instrucción SELECT, `INSERT`, `UPDATE` o `DELETE`. El CTE también se la puede usar en una vista.

## Syntax

`WITH` + alias + `AS` + (QUERY CTE) Query que hace referencia al CTE

```sql
WITH UK_Customers AS (
  SELECT customerNumber 
  FROM customers
  WHERE country = 'UK'
)
SELECT *
FROM orders O
INNER JOIN UK_Customers C ON C.customerNumber = O.customerNumber;

WITH CTE AS (
	SELECT CustomerNumber
	FROM customers
	WHERE customerNumber BETWEEN 121 AND 471
	AND (customerName LIKE 'A%'
		OR customerName LIKE '_A%')
	AND addressLine1 IS NOT NULL
	AND addressLine2 IS NULL
	AND creditLimit > 0
	AND postalCode IN ('4110', '51247')
)
UPDATE customers
INNER JOIN CTE C 
  ON C.CustomerNumber = customers.CustomerNumber
SET customers.creditLimit = 17.19;
```
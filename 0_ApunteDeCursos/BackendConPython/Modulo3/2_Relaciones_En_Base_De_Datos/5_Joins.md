# Joins

Un componente importante de cualquier base de datos relacional es la correlación que puede existir entre dos tablas cualesquiera. En SQL podemos unir las tablas en una instrucción. Una operación join es una operación que hace coincidir las filas en una tabla con las filas de manera tal que las columnas de ambas tablas puedan ser colocadas lado a lado en los resultados de la consulta como si éstos vinieran de una sola tabla.

## Tipos de joins

![](https://ingenieriadesoftware.es/wp-content/uploads/2018/07/sqljoin.jpeg)

- INNER JOIN: Devuelve registros que tienen valores coincidentes en ambas tablas.
- LEFT JOIN: Devuelve todos los registros de la tabla de la izquierda y los registros coincidentes de la tabla de la derecha.
- RIGHT JOIN: Devuelve todos los registros de la tabla de la derecha y los registros coincidentes de la tabla de la izquierda.
- CROSS JOIN (OUTER JOIN o FULL OUTER JOIN): Combina todas las filas de la tabla A con todas las filas de la tabla B.
- SELF JOIN: Aplica las reglas de los joins anteriores, solo que se realiza con la misma tabla.

### Ejemplo INNER JOIN

Leer los clientes que tienen ordenes, si un cliente no tiene ninguna orden, no estará en este resultado:

A: customers
B: orders

```sql
SELECT C.customerNumber, C.customerName, O.orderNumber, O.orderDate
FROM customers C
INNER JOIN orders O ON C.customerNumber = O.customerNumber;
```

Otra forma de escribirlo:

```sql
SELECT C.customerNumber, C.customerName, O.orderNumber, O.orderDate
FROM customers C
JOIN orders O ON C.customerNumber = O.customerNumber;

SELECT C.customerNumber, C.customerName, O.orderNumber, O.orderDate
FROM customers C, orders O
WHERE C.customerNumber = O.customerNumber;
```

A: customers
B: offices

```sql
SELECT C.customerNumber, C.customerName, O.officeCode, O.addressLine1
FROM customers C
INNER JOIN offices O ON C.country = O.country
	AND O.state = C.state
    AND O.city = C.city;
```

### Ejemplo LEFT JOIN

Leer todos los clientes, si los clientes tienen ordenes entonces aparecerán esos datos en el resultado, sino, apareceran como null:

A: customers
B: orders

```sql
SELECT C.customerNumber, C.customerName, O.orderNumber, O.orderDate
FROM customers C
LEFT JOIN orders O ON C.customerNumber = O.customerNumber;
```

Leer todos los clientes, que no tienen ordenes:

```sql
SELECT C.customerNumber, C.customerName, O.orderNumber, O.orderDate
FROM customers C
LEFT JOIN orders O ON C.customerNumber = O.customerNumber 
	AND O.orderNumber IS NULL;
```

### Ejemplo RIGTH JOIN

Leer todos los clientes, si los clientes tienen ordenes entonces aparecerán esos datos en el resultado, sino, apareceran como null:

A: orders
B: customers

```sql
SELECT C.customerNumber, C.customerName, O.orderNumber, O.orderDate
FROM orders O
RIGHT JOIN customers C ON C.customerNumber = O.customerNumber;
```

Leer todos los clientes, que no tienen ordenes:

```sql
SELECT C.customerNumber, C.customerName, O.orderNumber, O.orderDate
FROM orders O
RIGHT JOIN customers C ON C.customerNumber = O.customerNumber
	AND O.orderNumber IS NULL;
```

### Ejemplo CROSS JOIN

Leer todos los clientes y todas las ordenes:

A: orders
B: customers

```sql
SELECT C.customerNumber, C.customerName, O.orderNumber, O.orderDate
FROM customers C
CROSS JOIN orders O;

SELECT C.customerNumber, C.customerName, O.orderNumber, O.orderDate
FROM customers C, orders O;
```

La combinación anterior excepto la intersección de la tabla customers y orders:

```sql
SELECT C.customerNumber, C.customerName, O.orderNumber, O.orderDate
FROM customers C
CROSS JOIN orders O
WHERE C.customerNumber != O.customerNumber;
```

### Ejemplo SELF JOIN

Leer todas las ordenes y muestra el id de otra orden para para el mismo cliente y misma fecha:

A: orders
B: orders

```sql
SELECT A.customerNumber, A.orderNumber, A.orderDate, B.orderNumber
FROM orders A
LEFT JOIN orders B ON A.customerNumber = B.customerNumber
	AND A.orderDate = B.orderDate
	AND A.orderNumber != B.orderNumber;
```

## Joins con tablas intermediarias

Para obtener la lista de clientes y los productos que ha comprado cada cliente no existe una relación directa entre la tabla customers y products por lo que es necesario hacer los joins con tablas segun el diagrama ER muestra las llaves foraneas (como una cascada) hasta lograr llegar a la tabla de productos.

### joins

![](https://raw.githubusercontent.com/mayracmg/playground-sql-facilito/master/markdowns/JoinsCascada.png)

```sql
SELECT C.customerNumber, C.customerName, P.productCode, P.productName
FROM customers C
INNER JOIN orders O ON C.customerNumber = O.customerNumber
INNER JOIN orderdetails D ON D.orderNumber = O.orderNumber
INNER JOIN products P ON P.productCode = D.productCode;
```
# Window Functions

Una window function nos da visibilidad de información sobre un set de datos, desde cada fila podemos acceder a ese set de datos. A diferencia de las funciones de agregación que nos obliga a hacer agrupaciones, las window function no. Es posible usar las funciones de agregación con las window functions a fin de obtener calculos para cada fila sin realizar agrupaciones.

## Syntax

```sql
( [ ALL ] expression ) OVER ( [ PARTITION BY partition_list ] [ ORDER BY order_list] )
```

##  Algunas funciones comunes

- `FIRST_VALUE`: Para obtener el primer valor de un grupo.
- `LAST_VALUE`: Para obtener el ultimo valor de un grupo.
- `LAG`: Para obtener un valor de la fila anterior.
- `LEAD`: ara obtener un valor de la fila siguiente.
- `RANK`: Asigna un valor o un rank a cada fila segun la particion.
- `ROW_NUMBER`: Obtiene el numero de fila, puede ser una numeracion general o reiniciar la numeracion por grupos o particiones.

Query con una funcion de agregacion la cual devuelve el total de ordenes para cada cliente, pero no es posible listar los datos de esa orden:

```sql
SELECT C.customerNumber, C.customerName, COUNT(O.orderNumber) total_orders
FROM customers C
INNER JOIN orders O ON C.customerNumber = O.customerNumber
GROUP BY C.customerNumber, C.customerName;
```

Query con una window function la cual devuelve el total de ordenes para cada cliente, pero si es posible listar los datos de esa orden:

```sql
SELECT C.customerNumber, C.customerName, O.orderNumber, O.orderDate,
COUNT(O.orderNumber) OVER(PARTITION BY C.customerNumber) AS total_orders
FROM customers C
INNER JOIN orders O ON C.customerNumber = O.customerNumber;
```

Query con una window function para acceder a valores en otras filas. Adicional a los datos de la fila actual muestra la fecha de la primera orden que realizo el cliente:

```sql
SELECT C.customerNumber, C.customerName, O.orderNumber, O.orderDate,
FIRST_VALUE(O.orderDate) OVER(PARTITION BY C.customerNumber) AS firstOrderDate
FROM customers C
INNER JOIN orders O ON C.customerNumber = O.customerNumber
```
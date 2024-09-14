# Clausula Where

Define una condición (o varias) que debe cumplirse para que los datos sean devueltos. Los operadores utilizados en la cláusula `WHERE` (o cualquier condición definida en la cláusula) no tienen efecto en los datos almacenados en las tablas. Sólo afectan a los datos devueltos cuando se invoca la vista. Se puede incluir en una instrucción `SELECT`, `UPDATE` o `DELETE`.

## Datos

![](https://raw.githubusercontent.com/mayracmg/playground-sql-facilito/master/markdowns/EjemploDatos1.png)

## Aplicar un filtro

![](https://raw.githubusercontent.com/mayracmg/playground-sql-facilito/master/markdowns/EjemploDatos2.png)

## Aplicar otro filtro

![](https://raw.githubusercontent.com/mayracmg/playground-sql-facilito/master/markdowns/EjemploDatos3.png)

## Operadores de Comparación

- Típicos (`=,` !`=,` `<`, `<=,` `>`, `>=`)
- `AND`: Para unir dos condiciones, ambas deben ser verdaderas.
- `OR`: Para unir dos condiciones, una condición debe ser verdadera.
- `IS NULL`: Para obtener las filas donde X columna tiene valor null.
- `BETWEEN`: para identificar un rango de valores.
- `NOT`: Para negar una condición.
- `LIKE`: es posible especificar valores que son solamente similares a los valores almacenados.
- Signo de porcentaje (`%`): representa cero o más caracteres desconocidos.
- Guión bajo (`_`): representa exactamente un carácter desconocido.
- `IN`: permite determinar si los valores en la columna especificada de una tabla están contenidos en una lista definida o contenidos dentro de otra tabla.
- `EXISTS`: Está dedicado únicamente a determinar si la subconsulta arroja alguna fila o no.

```sql
SELECT CustomerNumber
FROM customers
WHERE customerNumber BETWEEN 121 AND 471
AND (customerName LIKE 'A%'
    OR customerName LIKE '_A%')
AND addressLine1 IS NOT NULL
AND addressLine2 IS NULL
AND creditLimit > 0
AND postalCode IN ('4110', '51247');
```
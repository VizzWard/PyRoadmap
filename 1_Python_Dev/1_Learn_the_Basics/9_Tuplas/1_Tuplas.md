# Tuplas en Python

## Definición
Las tuplas en Python son estructuras de datos inmutables y ordenadas que pueden contener elementos de diferentes tipos.

## Sintaxis
- Creación de una tupla vacía:
  ```python
  mi_tupla = ()
  ```
- Creación de una tupla con elementos:
  ```python
  mi_tupla = (1, 2, 3, 'a', 'b', 'c')
  ```
- Tupla de un solo elemento:
  ```python
  mi_tupla = (1,)  # La coma es necesaria
  ```

## Características principales
1. Inmutabilidad: No se pueden modificar después de ser creadas.
2. Indexación: Los elementos se acceden por su posición (índice), comenzando desde 0.
3. Admiten elementos duplicados.
4. Pueden contener elementos de diferentes tipos.

## Operaciones comunes
- Acceso a elementos: `mi_tupla[índice]`
- Slicing: `mi_tupla[inicio:fin:paso]`
- Longitud: `len(mi_tupla)`
- Concatenación: `tupla1 + tupla2`
- Repetición: `mi_tupla * n`

## Métodos útiles
- `count()`: Cuenta las ocurrencias de un elemento.
- `index()`: Encuentra el índice de un elemento.

## Ventajas
- Más eficientes en memoria que las listas.
- Inmutabilidad garantiza la integridad de los datos.
- Pueden usarse como claves en diccionarios.
- Ligeramente más rápidas que las listas para operaciones de lectura.

## Desventajas
- No se pueden modificar después de la creación.
- Menos flexibles que las listas para ciertas operaciones.

## Usos comunes
- Almacenar datos que no deben cambiar.
- Retornar múltiples valores de una función.
- Usar como claves en diccionarios (cuando contienen solo elementos inmutables).
- Representar registros o estructuras de datos fijas.

## Desempaquetado de tuplas
```python
x, y, z = (1, 2, 3)
```

## Conversión
- Lista a tupla: `tuple(mi_lista)`
- Tupla a lista: `list(mi_tupla)`

## Tuplas nombradas
Python ofrece `namedtuple` en el módulo `collections` para crear tuplas con campos nombrados:
```python
from collections import namedtuple
Punto = namedtuple('Punto', ['x', 'y'])
p = Punto(1, 2)
print(p.x, p.y)
```
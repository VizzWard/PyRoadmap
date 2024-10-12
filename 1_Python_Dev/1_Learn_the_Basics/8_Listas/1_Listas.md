# Listas en Python

## Definición
Las listas en Python son estructuras de datos mutables y ordenadas que pueden contener elementos de diferentes tipos.

## Sintaxis
- Creación de una lista vacía:
  ```python
  mi_lista = []
  ```
- Creación de una lista con elementos:
  ```python
  mi_lista = [1, 2, 3, 'a', 'b', 'c']
  ```

## Características principales
1. Mutabilidad: Se pueden modificar después de ser creadas.
2. Indexación: Los elementos se acceden por su posición (índice), comenzando desde 0.
3. Admiten elementos duplicados.
4. Pueden contener elementos de diferentes tipos.

## Operaciones comunes
- Acceso a elementos: `mi_lista[índice]`
- Slicing: `mi_lista[inicio:fin:paso]`
- Añadir elementos: 
  - Al final: `mi_lista.append(elemento)`
  - En una posición específica: `mi_lista.insert(índice, elemento)`
- Eliminar elementos:
  - Por valor: `mi_lista.remove(elemento)`
  - Por índice: `del mi_lista[índice]`
- Longitud: `len(mi_lista)`
- Ordenar: `mi_lista.sort()`
- Revertir: `mi_lista.reverse()`

## Métodos útiles
- `count()`: Cuenta las ocurrencias de un elemento.
- `index()`: Encuentra el índice de un elemento.
- `pop()`: Elimina y retorna el último elemento (o el especificado).
- `extend()`: Añade los elementos de un iterable al final de la lista.

## Ventajas
- Flexibles y fáciles de usar.
- Ideales para almacenar colecciones ordenadas de elementos.
- Permiten operaciones eficientes de inserción y eliminación.

## Desventajas
- Pueden consumir más memoria que otras estructuras de datos.
- Las operaciones de búsqueda pueden ser lentas en listas grandes.

## Usos comunes
- Almacenar colecciones de datos relacionados.
- Implementar pilas y colas.
- Manejar secuencias de elementos en algoritmos.
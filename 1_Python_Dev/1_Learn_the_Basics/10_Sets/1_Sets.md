# Sets en Python

## Definición
Los sets en Python son colecciones desordenadas de elementos únicos y mutables.

## Sintaxis
- Creación de un set vacío:
  ```python
  mi_set = set()
  ```
- Creación de un set con elementos:
  ```python
  mi_set = {1, 2, 3, 'a', 'b', 'c'}
  ```

## Características principales
1. No ordenados: Los elementos no tienen un orden específico.
2. Elementos únicos: No permiten duplicados.
3. Mutabilidad: El set en sí es mutable, pero sus elementos deben ser inmutables.
4. No soportan indexación.

## Operaciones comunes
- Añadir elementos: `mi_set.add(elemento)`
- Eliminar elementos:
  - `mi_set.remove(elemento)` (lanza error si no existe)
  - `mi_set.discard(elemento)` (no lanza error si no existe)
- Longitud: `len(mi_set)`
- Verificar pertenencia: `elemento in mi_set`

## Métodos útiles
- `union()`: Combina sets sin duplicados.
- `intersection()`: Encuentra elementos comunes entre sets.
- `difference()`: Encuentra elementos en un set pero no en otro.
- `symmetric_difference()`: Encuentra elementos que están en cualquiera de los sets, pero no en ambos.
- `issubset()`: Verifica si un set es subconjunto de otro.
- `issuperset()`: Verifica si un set es superconjunto de otro.

## Operaciones de conjunto
- Unión: `set1 | set2`
- Intersección: `set1 & set2`
- Diferencia: `set1 - set2`
- Diferencia simétrica: `set1 ^ set2`

## Ventajas
- Eliminación automática de duplicados.
- Operaciones de conjunto eficientes.
- Rápidos para verificar la pertenencia de elementos.

## Desventajas
- No mantienen un orden específico.
- No soportan indexación o slicing.
- Los elementos deben ser inmutables (no pueden contener listas o diccionarios).

## Usos comunes
- Eliminar duplicados de una secuencia.
- Realizar operaciones matemáticas de conjuntos.
- Verificar pertenencia de elementos de manera eficiente.
- Almacenar valores únicos sin importar el orden.

## Set comprehensions
Similar a las list comprehensions:
```python
mi_set = {x**2 for x in range(10)}
```

## Frozenset
Python también ofrece `frozenset`, una versión inmutable de set:
```python
mi_frozenset = frozenset([1, 2, 3])
```

## Conversión
- Lista a set: `set(mi_lista)`
- Set a lista: `list(mi_set)`
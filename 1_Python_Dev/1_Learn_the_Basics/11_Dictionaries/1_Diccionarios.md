# Diccionarios en Python

## 1. Introducción a los Diccionarios

Los diccionarios en Python son estructuras de datos que permiten almacenar pares clave-valor. Son colecciones ordenadas (a partir de Python 3.7), modificables y que no admiten duplicados en las claves.

Sintaxis básica:
```python
mi_diccionario = {
    "clave1": "valor1",
    "clave2": "valor2",
    "clave3": "valor3"
}
```

## 2. Características Principales

- **Ordenados**: Mantienen el orden de inserción (desde Python 3.7).
- **Modificables**: Se pueden cambiar, añadir o eliminar elementos después de la creación.
- **Sin Duplicados**: No pueden tener dos elementos con la misma clave.
- **Heterogéneos**: Las claves y valores pueden ser de diferentes tipos de datos.

## 3. Creación de Diccionarios

Existen varias formas de crear diccionarios:

```python
# Forma literal
dict1 = {"nombre": "Juan", "edad": 30}

# Usando el constructor dict()
dict2 = dict(nombre="María", edad=25)

# A partir de una lista de tuplas
dict3 = dict([("ciudad", "Madrid"), ("país", "España")])
```

## 4. Acceso y Manipulación de Elementos

### Acceso a valores
```python
mi_dict = {"nombre": "Ana", "edad": 28}
print(mi_dict["nombre"])  # Ana

# Usando el método get() (más seguro)
print(mi_dict.get("edad"))  # 28
print(mi_dict.get("altura", "No especificada"))  # No especificada
```

### Modificación de valores
```python
mi_dict["edad"] = 29
```

### Añadir nuevos pares clave-valor
```python
mi_dict["profesión"] = "Ingeniera"
```

## 5. Métodos de Diccionarios

- **keys()**: Devuelve una vista de las claves.
- **values()**: Devuelve una vista de los valores.
- **items()**: Devuelve una vista de los pares clave-valor.
- **get(key, default)**: Obtiene el valor de una clave, con un valor por defecto opcional.
- **update()**: Actualiza el diccionario con elementos de otro diccionario o de pares clave-valor.
- **pop(key, default)**: Elimina y devuelve el valor de una clave específica.
- **popitem()**: Elimina y devuelve el último par clave-valor insertado.
- **clear()**: Elimina todos los elementos del diccionario.

Ejemplo:
```python
mi_dict = {"a": 1, "b": 2}
mi_dict.update({"c": 3, "d": 4})
print(mi_dict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

valor = mi_dict.pop("b")
print(valor)  # 2
print(mi_dict)  # {'a': 1, 'c': 3, 'd': 4}
```

## 6. Eliminación de Elementos

```python
del mi_dict["a"]  # Elimina el par clave-valor con clave "a"
```

## 7. Iteración sobre Diccionarios

```python
for clave in mi_dict:
    print(clave, mi_dict[clave])

for clave, valor in mi_dict.items():
    print(clave, valor)
```

## 8. Diccionarios Anidados

Los diccionarios pueden contener otros diccionarios como valores:

```python
estudiantes = {
    "Juan": {"edad": 20, "carrera": "Informática"},
    "María": {"edad": 22, "carrera": "Matemáticas"}
}
print(estudiantes["Juan"]["carrera"])  # Informática
```

## 9. Comprensión de Diccionarios

Permite crear diccionarios de forma concisa:

```python
cuadrados = {x: x**2 for x in range(5)}
print(cuadrados)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## 10. Uso Práctico

Los diccionarios son útiles para:
- Almacenar datos estructurados (como registros de una base de datos).
- Implementar caches o memoización en algoritmos.
- Representar estructuras de datos complejas (como grafos).

Ejemplo de uso como caché:
```python
def factorial(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    result = n * factorial(n-1)
    cache[n] = result
    return result
```

## 11. Rendimiento

Los diccionarios en Python están implementados como tablas hash, lo que permite un acceso muy rápido a los elementos (complejidad O(1) en promedio).

## 12. Consideraciones de Inmutabilidad

Las claves de un diccionario deben ser inmutables (como strings, números o tuplas). Esto es necesario para garantizar la integridad de la estructura hash interna.

## 13. Métodos de Vista

Los métodos `keys()`, `values()`, e `items()` devuelven objetos de vista, que son dinámicos y reflejan los cambios en el diccionario:

```python
mi_dict = {"a": 1, "b": 2}
claves = mi_dict.keys()
print(claves)  # dict_keys(['a', 'b'])
mi_dict["c"] = 3
print(claves)  # dict_keys(['a', 'b', 'c'])
```

## 14. Ordenamiento

A partir de Python 3.7, los diccionarios mantienen el orden de inserción. Esto permite usarlos en situaciones donde el orden es importante:

```python
from collections import OrderedDict  # Ya no es necesario en Python 3.7+

mi_dict = {"c": 3, "a": 1, "b": 2}
print(list(mi_dict))  # ['c', 'a', 'b']
```

## 15. Comparación con Otros Tipos de Datos

- **Listas**: Ordenadas, permiten duplicados, acceso por índice.
- **Tuplas**: Como listas, pero inmutables.
- **Conjuntos**: No ordenados, sin duplicados, sin acceso por índice.
- **Diccionarios**: Ordenados, sin duplicados en claves, acceso por clave.

Elija diccionarios cuando necesite una asociación clave-valor eficiente y el orden de inserción sea importante.

## Conclusión

Los diccionarios en Python son estructuras de datos versátiles y potentes, ideales para muchas tareas de programación. Su eficiencia y flexibilidad los convierten en una herramienta esencial en el toolkit de cualquier programador de Python.
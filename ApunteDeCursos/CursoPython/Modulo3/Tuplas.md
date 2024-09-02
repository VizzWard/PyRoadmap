# Tuplas

En Python, una tupla es una estructura de datos que permite almacenar una secuencia ordenada de elementos. A diferencia de las listas, las tuplas son inmutables, lo que significa que una vez que se han creado, sus elementos no pueden ser modificados (no se pueden agregar, eliminar ni cambiar elementos).

## Características principales de las tuplas

- Ordenadas: Los elementos dentro de una tupla tienen un orden definido que no cambia.
- Inmutables: Después de crear una tupla, no se pueden modificar sus elementos.
- Permiten Elementos Duplicados: Una tupla puede contener elementos repetidos.
- Heterogéneas: Las tuplas pueden contener elementos de diferentes tipos de datos (enteros, cadenas, flotantes, etc.).
- Acceso por Índice: Puedes acceder a los elementos de una tupla utilizando índices.

## Creación de tuplas

Puedes crear una tupla simplemente separando los elementos por comas y encerrándolos entre paréntesis:

```python
mi_tupla = (1, 2, 3, "Hola", 4.5)
```

También puedes crear una tupla sin usar paréntesis, separando los elementos por comas:

```python
mi_tupla = 1, 2, 3, "Hola", 4.5
```

Para crear una tupla vacía, simplemente usa paréntesis vacíos:

```python
tupla_vacia = ()
```

## Acceso a elementos

Puedes acceder a elementos individuales de una tupla utilizando índices, de la misma manera que lo harías con una lista:

```python
mi_tupla = (1, 2, 3, "Hola", 4.5)
print(mi_tupla[0])  # Imprime: 1
print(mi_tupla[3])  # Imprime: Hola
```

También puedes usar índices negativos para acceder a elementos desde el final de la tupla:

```python
print(mi_tupla[-1])  # Imprime: 4.5
```

## Operaciones con tuplas

Aunque las tuplas son inmutables, aún puedes realizar varias operaciones:

- Concatenación: Puedes concatenar dos o más tuplas para crear una nueva tupla:

```python
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # Imprime: (1, 2, 3, 4, 5, 6)
```

- Repetición: Puedes repetir los elementos de una tupla:

```python
tupla_repetida = tupla1 * 3
print(tupla_repetida)  # Imprime: (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

- Slicing: Puedes obtener una subtupla usando el operador de slicing:

```python
sub_tupla = mi_tupla[1:4]
print(sub_tupla)  # Imprime: (2, 3, "Hola")
```

## Usos comunes de las tuplas

- Agrupación de datos: Las tuplas son útiles para agrupar datos relacionados que no necesitan cambiar, como coordenadas (x, y), fechas (año, mes, día), etc.
- Claves de diccionarios: Debido a su inmutabilidad, las tuplas se pueden usar como claves en diccionarios, algo que no se puede hacer con listas.
- Retorno de múltiples valores: Las funciones en Python pueden retornar múltiples valores empaquetándolos en una tupla.

```python
def coordenadas():
    return (10, 20)

x, y = coordenadas()
print(x, y)  # Imprime: 10 20
```
# Listas


En Python, una lista es una estructura de datos que permite almacenar una colección ordenada de elementos, los cuales pueden ser de diferentes tipos de datos. Las listas son mutables, lo que significa que puedes modificar sus elementos después de que la lista ha sido creada (añadir, eliminar o cambiar elementos).

## Características principales de las listas

1. Ordenadas: Los elementos en una lista tienen un orden definido que no cambia a menos que modifiques explícitamente la lista.
2. Mutable: Puedes cambiar los elementos de la lista, añadir nuevos elementos o eliminar existentes.
3. Elementos Heterogéneos: Una lista puede contener elementos de diferentes tipos de datos, como enteros, cadenas, flotantes, e incluso otras listas.
4. Indexación y Slicing: Puedes acceder a elementos individuales de la lista usando índices, y puedes obtener sublistas usando slicing.

## Sintaxis y usos basicos

### Crear una lista

```python
mi_lista = [1, 2, 3, "Hola", 4.5]
```

### Acceder a elementos:

- Por indice

```python
primer_elemento = mi_lista[0]  # 1
ultimo_elemento = mi_lista[-1]  # 4.5
```

- Sublistas

```python
sub_lista = mi_lista[1:4]  # [2, 3, "Hola"]
```

### Modificar elementos

```python
mi_lista[3] = "Adiós"
# Ahora mi_lista es [1, 2, 3, "Adiós", 4.5]
```

### Añadir elementos

- Al final

```python
mi_lista.append(6)
# Ahora mi_lista es [1, 2, 3, "Adiós", 4.5, 6]
```

- En una posicion especifica

```python
mi_lista.insert(1, "Nuevo")
# Ahora mi_lista es [1, "Nuevo", 2, 3, "Adiós", 4.5, 6]
```

### Eliminar elementos

- Por valor

```python
mi_lista.remove("Adiós")
# Ahora mi_lista es [1, "Nuevo", 2, 3, 4.5, 6]
```

- Por indice

```python
eliminado = mi_lista.pop(0)
# eliminado es 1 y ahora mi_lista es ["Nuevo", 2, 3, 4.5, 6]
```

### Iterar sobre una lista

```python
for elemento in mi_lista:
    print(elemento)
```

### Otras operaciones comunes

- Concatenar listas

```python
nueva_lista = mi_lista + [7, 8, 9]
```

- Repetir una lista

```python
repetida = mi_lista * 2
```
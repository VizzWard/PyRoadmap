# Diccionarios

Un diccionario es una estructura de datos que permite almacenar pares de clave-valor, donde cada clave está asociada con un valor específico. Los diccionarios son mutables, lo que significa que puedes modificar, agregar o eliminar elementos después de su creación. 

Además, son desordenados, lo que significa que no mantienen el orden de inserción de los elementos (aunque en versiones recientes de Python, el orden de inserción sí se conserva, pero no se debe depender de esto para operaciones críticas).

## Características

- Claves Únicas: Cada clave en un diccionario debe ser única. Si intentas usar una clave que ya existe, el valor asociado a esa clave será sobrescrito.
- Mutables: Puedes agregar, modificar o eliminar elementos en un diccionario.
- Acceso Rápido: Los diccionarios proporcionan un acceso rápido a los valores a través de sus claves.
- Clave-Valor: Cada elemento en un diccionario es un par formado por una clave y un valor asociado.

## Crear un diccionario

Puedes crear un diccionario utilizando llaves {} y separando las claves de sus valores con dos puntos :. Cada par clave-valor está separado por una coma.

```python
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
```

En este ejemplo, "nombre", "edad", y "ciudad" son las claves, mientras que "Juan", 30, y "Madrid" son los valores correspondientes.

## Acceder a elementos

Puedes acceder a los valores de un diccionario utilizando sus claves:

```python
print(mi_diccionario["nombre"])  # Imprime: Juan
```

Si intentas acceder a una clave que no existe, obtendrás un error KeyError. Para evitar esto, puedes usar el método get que retorna None si la clave no existe, o un valor predeterminado si se especifica.

```python
print(mi_diccionario.get("altura", "No disponible"))  # Imprime: No disponible
```

## Modificar elementos

Puedes modificar el valor asociado a una clave existente:

```python
mi_diccionario["edad"] = 31
print(mi_diccionario["edad"])  # Imprime: 31
```

## Agregar elementos

Puedes agregar nuevos pares clave-valor simplemente asignándolos:

```python
mi_diccionario["altura"] = 175
print(mi_diccionario)  # Imprime: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid', 'altura': 175}
```

## Eliminar elementos

Puedes eliminar un par clave-valor usando el método pop o el operador del:

```python
mi_diccionario.pop("ciudad")
del mi_diccionario["edad"]
print(mi_diccionario)  # Imprime: {'nombre': 'Juan', 'altura': 175}
```

## Métodos comunes de los diccionarios

### keys()

Retorna una vista de todas las claves en el diccionario.

```python
claves = mi_diccionario.keys()
print(claves)  # Imprime: dict_keys(['nombre', 'altura'])
```

### values()

Retorna una vista de todos los valores en el diccionario.

```python
valores = mi_diccionario.values()
print(valores)  # Imprime: dict_values(['Juan', 175])
```

### items()

Retorna una vista de todos los pares clave-valor como tuplas.

```python
items = mi_diccionario.items()
print(items)  # Imprime: dict_items([('nombre', 'Juan'), ('altura', 175)])
```

### update()

Actualiza el diccionario con otro diccionario o con pares clave-valor.

```python
otro_diccionario = {"peso": 70, "ciudad": "Barcelona"}
mi_diccionario.update(otro_diccionario)
print(mi_diccionario)  # Imprime: {'nombre': 'Juan', 'altura': 175, 'peso': 70, 'ciudad': 'Barcelona'}
```

### clear()

Elimina todos los elementos del diccionario.

```python
mi_diccionario.clear()
print(mi_diccionario)  # Imprime: {}
```
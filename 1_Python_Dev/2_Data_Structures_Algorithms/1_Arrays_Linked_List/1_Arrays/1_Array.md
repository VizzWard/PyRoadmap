# Arrays en Python

Un array es básicamente una estructura de datos que puede contener más de un valor a la vez. Es una colección o serie ordenada de elementos del mismo tipo.

```python
a = arr.array('d',[1.2,1.3,2.3])
```

Podemos hacer un bucle a través de los elementos del array fácilmente y obtener los valores requeridos con sólo especificar el número de índice. Las matrices son mutables (cambiable), así, por lo tanto, puede realizar diversas manipulaciones según sea necesario.

> ¿Es lo mismo una lista que un array en Python?
> 
> Los Arrays y las listas en Python almacenan valores de forma similar. Pero hay una diferencia clave entre ambos: los valores que almacenan. Una lista puede almacenar cualquier tipo de valores, como intergers, cadenas, etc. En cambio, las matrices almacenan valores de un solo tipo de datos. Por lo tanto, puedes tener un array de enteros, un array de cadenas, etc.

## Crear un Array

Las matrices en Python se pueden crear después de importar el módulo de matrices:

```python
import array as arr
```

La función array(tipo de datos, lista de valores) toma dos parámetros, el primero es el tipo de datos del valor que se va a almacenar y el segundo es la lista de valores. El tipo de datos puede ser int, float, double, etc. Ten en cuenta que `arr` es el nombre de alias y es para facilitar su uso. También puedes importar sin alias. Hay otra forma de importar el módulo array que es:

```python
from array import *
```

Esto significa que quieres importar todas las funciones del módulo array.

Para crear un array se utiliza la siguiente sintaxis:

```python
a = arr.array(data type, value list) 
```

o

```python
a = array(data type, value list)  # Cuando importas usando *
```

**Ejemplo**:

```python
a = arr.array( ‘d’ , [1.1 , 2.1 ,3.1] )
```

Aquí, el primer parámetro es 'd' que es un tipo de datos, es decir, float y los valores se especifican como el siguiente parámetro.

> Nota
> 
> Todos los valores especificados son del tipo float. No podemos especificar los valores de diferentes tipos de datos a una sola matriz.

La siguiente tabla muestra los distintos tipos de datos y sus códigos:

| Type code | Python Data Type | Byte Size |
|-----------|------------------|-----------|
| 'b'       | int (signed)     | 1         |
| 'B'       | int (unsigned)   | 1         |
| 'h'       | int (signed)     | 2         |
| 'H'       | int (unsigned)   | 2         |
| 'i'       | int (signed)     | 2         |
| 'I'       | int (unsigned)   | 2         |
| 'l'       | int (signed)     | 4         |
| 'L'       | int (unsigned)   | 4         |
| 'q'       | int (signed)     | 8         |
| 'Q'       | int (unsigned)   | 8         |
| 'f'       | float            | 4         |
| 'd'       | float            | 8         |
| 'u'       | Unicode character| 2         |
| 'c'       | char             | 1         |

### Acceso a elementos del array

Para acceder a los elementos de una matriz, es necesario especificar los valores del índice. La indexación comienza en 0 y no en 1. Por lo tanto, el número de índice es siempre 1 menos que la longitud de la matriz.

```python
a = arr.array( 'd', [1.1 , 2.1 ,3.1] )
a[1]
```

### Operaciones basicas

Hay muchas operaciones que se pueden realizar en matrices, que son las siguientes:

![basic_operations](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/04/OPERATIONS-NEW.png)

#### Determinar la longitud de una matriz

La longitud de una matriz es el número de elementos que están realmente presentes en una matriz. Usted puede hacer uso de la función len() para lograr esto. La función len() devuelve un valor entero que es igual al número de elementos presentes en esa matriz.

```python
a=arr.array('d', [1.1 , 2.1 ,3.1] )
len(a)
```

#### Añadir/modificar elementos de una matriz

Podemos añadir valor a un array utilizando las funciones append(), extend() e insert (i,x).

La función append() se utiliza cuando necesitamos añadir un único elemento al final del array.

```python
a=arr.array('d', [1.1 , 2.1 ,3.1] )
a.append(3.4)
```

El array resultante es el array actual con el nuevo valor añadido al final del mismo. Para añadir más de un elemento, puede utilizar la función extend(). Esta función toma como parámetro una lista de elementos. El contenido de esta lista son los elementos que se añadirán a la matriz.

```python
a=arr.array('d', [1.1 , 2.1 ,3.1] )
a.extend([4.5,6.3,6.8])
```

Sin embargo, cuando se necesita añadir un elemento específico en una posición concreta de la matriz, se puede utilizar la función insert(i,x). Esta función inserta el elemento en el índice correspondiente de la matriz. Toma 2 parámetros donde el primer parámetro es el índice donde el elemento necesita ser insertado y el segundo es el valor.

```python
a=arr.array('d', [1.1 , 2.1 ,3.1] )
a.insert(2,3.8)
```

#### Eliminar/borrar elementos de una matriz

Los elementos de una matriz pueden eliminarse mediante los métodos pop() o remove(). La diferencia entre estas dos funciones es que la primera devuelve el valor eliminado mientras que la segunda no.

La función pop() no toma ningún parámetro o toma el valor del índice como parámetro. Cuando no se proporciona ningún parámetro, la función pop() salta() el último elemento y lo devuelve. Cuando se proporciona explícitamente el valor del índice, la función pop() extrae los elementos necesarios y lo devuelve.

```python
a=arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6])
print(a.pop())
print(a.pop(3))
```
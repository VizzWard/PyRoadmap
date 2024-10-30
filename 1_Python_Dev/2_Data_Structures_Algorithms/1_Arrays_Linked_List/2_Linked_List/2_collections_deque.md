# Introducing collections.deque

En Python, hay un objeto específico en el módulo de colecciones que puedes utilizar para listas enlazadas llamado deque (pronunciado "deck"), que significa cola de doble extremo.

`collections.deque` utiliza una implementación de una lista enlazada en la que se puede acceder, insertar o eliminar elementos del principio o del final de una lista con un rendimiento O(1) constante.

## Como usar en Queues

Primero, necesitas crear una lista enlazada. Puedes utilizar el siguiente fragmento de código para hacerlo con deque:

```python
from collections import deque

deque()
```

El código anterior creará una lista enlazada vacía. Si desea rellenarla en la creación, entonces usted puede darle un iterable como entrada:

```commandline
>>> deque(['a','b','c'])
deque(['a', 'b', 'c'])

>>> deque('abc')
deque(['a', 'b', 'c'])

>>> deque([{'data': 'a'}, {'data': 'b'}])
deque([{'data': 'a'}, {'data': 'b'}])
```

Al inicializar un objeto deque, puede pasar cualquier iterable como entrada, como una cadena (también un iterable) o una lista de objetos.

Ahora que sabes cómo crear un objeto deque, puedes interactuar con él añadiendo o eliminando elementos. Puedes crear una lista enlazada abcde y añadir un nuevo elemento `f` así:

```commandline
>>> llist = deque("abcde")
>>> llist
deque(['a', 'b', 'c', 'd', 'e'])

>>> llist.append("f")
>>> llist
deque(['a', 'b', 'c', 'd', 'e', 'f'])

>>> llist.pop()
'f'

>>> llist
deque(['a', 'b', 'c', 'd', 'e'])
```

Tanto `append()` como `pop()` añaden o eliminan elementos de la parte derecha de la lista enlazada. Sin embargo, también puede utilizar deque para añadir o eliminar rápidamente elementos del lado izquierdo, o cabeza, de la lista:

## Como usar en Stacks

¿Y si quisieras crear una pila? Bueno, la idea es más o menos la misma que con la cola. La única diferencia es que la pila utiliza el enfoque LIFO, lo que significa que el último elemento que se inserta en la pila debe ser el primero en ser eliminado.

Imagina que estás creando la funcionalidad de historial de un navegador web en la que se almacenan todas las páginas que visita un usuario para que pueda volver atrás en el tiempo fácilmente. Supongamos que estas son las acciones que un usuario cualquiera realiza en su navegador:

1. Visita el sitio web de Real Python 
2. Navega hasta Pandas: Cómo leer y escribir archivos 
3. Hace clic en un enlace para Leer y escribir archivos CSV en Python

```commandline
>>> from collections import deque
>>> history = deque()

>>> history.appendleft("https://realpython.com/")
>>> history.appendleft("https://realpython.com/pandas-read-write-files/")
>>> history.appendleft("https://realpython.com/python-csv/")
>>> history
deque(['https://realpython.com/python-csv/',
       'https://realpython.com/pandas-read-write-files/',
       'https://realpython.com/'])
```

En este ejemplo, creó un objeto de historial vacío, y cada vez que el usuario visitaba un nuevo sitio, lo añadía a su variable de historial utilizando `appendleft()`. Haciendo esto se aseguraba de que cada nuevo elemento se añadía a la cabeza de la lista enlazada.

Ahora supongamos que después de que el usuario leyó ambos artículos, quiso volver a la página principal de Real Python para elegir un nuevo artículo para leer. Sabiendo que tiene una pila y que quiere eliminar elementos usando LIFO, podría hacer lo siguiente:

```commandline
>>> history.popleft()
'https://realpython.com/python-csv/'

>>> history.popleft()
'https://realpython.com/pandas-read-write-files/'

>>> history
deque(['https://realpython.com/'])
```


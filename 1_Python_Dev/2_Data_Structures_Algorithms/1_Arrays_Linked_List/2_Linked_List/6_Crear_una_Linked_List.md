# Cómo crear una lista enlazada

Lo primero es lo primero, crea una clase para representar tu lista enlazada:

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

La única información que necesitas almacenar para una lista enlazada es dónde empieza la lista (la cabeza de la lista). A continuación, crea otra clase para representar cada nodo de la lista enlazada:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

En la definición de clase anterior, puedes ver los dos elementos principales de cada nodo: `data` y `next`. También puedes añadir un `__repr__` a ambas clases para tener una representación más útil de los objetos:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
```

Echa un vistazo a un ejemplo de uso de las clases anteriores para crear rápidamente una lista enlazada con tres nodos:

```commandline
>>> llist = LinkedList()
>>> llist
None

>>> first_node = Node("a")
>>> llist.head = first_node
>>> llist
a -> None

>>> second_node = Node("b")
>>> third_node = Node("c")
>>> first_node.next = second_node
>>> second_node.next = third_node
>>> llist
a -> b -> c -> None
```

Definiendo los datos y los valores siguientes de un nodo, se puede crear una lista enlazada con bastante rapidez. Estas clases `LinkedList` y `Node` son los puntos de partida para nuestra implementación. A partir de ahora, se trata de aumentar su funcionalidad.

He aquí un ligero cambio en el `__init__()` de las listas enlazadas que permite crear rápidamente listas enlazadas con algunos datos:

```python
def __init__(self, nodes=None):
    self.head = None
    if nodes is not None:
        node = Node(data=nodes.pop(0))
        self.head = node
        for elem in nodes:
            node.next = Node(data=elem)
            node = node.next
```
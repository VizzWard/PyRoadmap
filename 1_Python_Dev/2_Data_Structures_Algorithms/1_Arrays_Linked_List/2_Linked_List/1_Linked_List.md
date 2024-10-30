# [Linked List](https://realpython.com/linked-lists-python/)

Las listas enlazadas son una colección ordenada de objetos. ¿Qué las diferencia de las listas normales? Las listas enlazadas se diferencian de las listas en la forma en que almacenan los elementos en memoria. Mientras que las listas utilizan un bloque de memoria contiguo para almacenar las referencias a sus datos, las listas enlazadas almacenan las referencias como parte de sus propios elementos.

## Conceptos principales

Cada elemento de una lista enlazada se denomina nodo, y cada nodo tiene dos campos diferentes:

1. **Data** contiene el valor a almacenar en el nodo.
2. **Next** contiene una referencia al siguiente nodo de la lista.

![node](https://realpython.com/cdn-cgi/image/width=350,format=auto/https://files.realpython.com/media/Group_12_2.0ded5fffe97a.png)

Una lista enlazada es una colección de nodos. El primer nodo se denomina **head**, y se utiliza como punto de partida para cualquier iteración a través de la lista. El último nodo debe tener su siguiente referencia apuntando a **None** para determinar el final de la lista. Así es como se ve:

![linked_list](https://realpython.com/cdn-cgi/image/width=1248,format=auto/https://files.realpython.com/media/Group_14.27f7c4c6ec02.png)

## Aplicaciones

Pueden utilizarse para implementar colas o pilas, así como graphs. También son útiles para tareas mucho más complejas, como la gestión del ciclo de vida de una aplicación del sistema operativo.

### Queues or Stacks

Las colas y las pilas sólo se diferencian en la forma de recuperar los elementos. En una cola, se utiliza el método **FIFO** (primero en entrar, primero en salir). Esto significa que el primer elemento insertado en la lista es el primero que se recupera:

![queue](https://files.realpython.com/media/Group_6_3.67b18836f065.png)

Puedes ver los elementos delanteros y traseros de la cola. Cuando añadas nuevos elementos a la cola, irán a la parte trasera. Cuando recuperes elementos, se tomarán de la parte delantera de la cola.

En el caso de una pila, se utiliza un enfoque **LIFO** (Last-In/First-Out), lo que significa que el último elemento insertado en la lista es el primero en ser recuperado:

![stack](https://files.realpython.com/media/Group_7_5.930e25fcf2a0.png)

Puedes ver que el primer elemento insertado en la pila (índice 0) está en la parte inferior, y el último elemento insertado está en la parte superior. Dado que las pilas utilizan el enfoque LIFO, el último elemento insertado (en la parte superior) será el primero en ser recuperado.

### Graphs

Los grafos pueden utilizarse para mostrar relaciones entre objetos o para representar distintos tipos de redes. Por ejemplo, una representación visual de un grafo -digamos un grafo acíclico dirigido (DAG)- podría tener este aspecto:

![graph](https://files.realpython.com/media/Group_20.32afe2d011b9.png)

Hay distintas formas de implementar grafos como el anterior, pero una de las más comunes es utilizar una lista de adyacencia. Una lista de adyacencia es, en esencia, una lista de listas enlazadas en la que cada vértice del grafo se almacena junto a una colección de vértices conectados:

| Vertex | Linked List of Vertices |
|--------|-------------------------|
| 1      | 2 -> 3 -> None          |
| 2      | 4 -> None               |
| 3      | None                    |
| 4      | 5 -> 6 -> None          |
| 5      | 6 -> None               |
| 6      | None                    |

En la tabla anterior, cada vértice del grafo aparece en la columna de la izquierda. La columna de la derecha contiene una serie de listas enlazadas que almacenan los demás vértices conectados con el vértice correspondiente de la columna de la izquierda. Esta lista de adyacencia también podría representarse en código mediante un dict:

```python
graph = {
    1 : [2, 3, None],
    2 : [4, None],
    3 : [None],
    4 : [5, 6, None],
    5 : [6, None],
    6 : [None]
}
```

Las claves de este diccionario son los vértices de origen, y el valor de cada clave es una lista. Esta lista suele implementarse como una lista enlazada.

> **Nota**: En el ejemplo anterior podría evitar almacenar los valores `None`, pero los hemos mantenido aquí por claridad y coherencia con ejemplos posteriores.

## Lists vs Linked Lists

Existen claras diferencias en la forma en que se almacenan en memoria las listas enlazadas y las matrices. En Python, sin embargo, las listas son arrays dinámicos. Eso significa que el uso de memoria tanto de las listas como de las listas enlazadas es muy similar.

Dado que la diferencia en el uso de memoria entre las listas y las listas enlazadas es tan insignificante, es mejor que te centres en sus diferencias de rendimiento en lo que respecta a la complejidad temporal.

### Insertion y Deletion de elementos

En Python, puedes insertar elementos en una lista usando `.insert()` o `.append()`. Para eliminar elementos de una lista, puedes utilizar sus equivalentes: `.remove()` y `.pop()`.

La principal diferencia entre estos métodos es que se utiliza `.insert()` y `.remove()` para insertar o eliminar elementos en una posición específica de una lista, pero se utiliza `.append()` y `.pop()` solo para insertar o eliminar elementos al final de una lista.

### Recuperación de elementos

Cuando se trata de buscar elementos, las listas funcionan mucho mejor que las listas enlazadas. Cuando se sabe a qué elemento se quiere acceder, las listas pueden realizar esta operación en tiempo __O(1)__. Intentar hacer lo mismo con una lista enlazada llevaría __O(n)__ porque es necesario recorrer toda la lista para encontrar el elemento.


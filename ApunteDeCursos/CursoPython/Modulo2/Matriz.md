# Matrices

Una matriz es una estructura de datos bidimensional en la que los elementos están organizados en filas y columnas. En Python, una matriz puede representarse usando una lista de listas, donde cada lista interna representa una fila de la matriz. Las matrices se utilizan comúnmente para realizar operaciones matemáticas y para almacenar datos estructurados en forma de tablas.

## Caracteristicas

- Bidimensional: Una matriz tiene dos dimensiones: filas y columnas.
- Indexación: Los elementos de una matriz se acceden utilizando dos índices: uno para la fila y otro para la columna.
- Operaciones: Puedes realizar operaciones como recorrer, modificar, y acceder a elementos individuales, filas, o columnas.

## Ejemplo

### Crear una Matriz

```python
matriz = [
    [1, 2, 3],   # Fila 0
    [4, 5, 6],   # Fila 1
    [7, 8, 9]    # Fila 2
]
```

Esta matriz tiene 3 filas y 3 columnas.

### Acceder a Elementos

Para acceder a un elemento específico, usa dos índices: uno para la fila y otro para la columna.

```python
elemento = matriz[1][2]  # Accede al elemento en la fila 1, columna 2 (valor 6)
print(elemento)  # Imprime: 6
```

### Modificar Elementos

Puedes modificar un elemento específico usando sus índices:

```python
matriz[2][1] = 10  # Cambia el valor en la fila 2, columna 1 a 10
print(matriz)
# Resultado: [[1, 2, 3], [4, 5, 6], [7, 10, 9]]
```

### Recorrer una Matriz

Puedes recorrer todos los elementos de la matriz utilizando bucles anidados:

```python
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Imprime una nueva línea después de cada fila
```

Este código imprime todos los elementos de la matriz fila por fila.

### Operaciones más avanzadas

Para realizar operaciones matemáticas más complejas, como la multiplicación de matrices o la transposición, es común usar bibliotecas como NumPy, que proporciona una implementación más eficiente y una amplia gama de operaciones específicas para matrices.

#### Ejemplo básico usando NumPy

```python
import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
transpuesta = matriz.T  # Transponer la matriz
print(transpuesta)
```

# Crear una matriz
matriz = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

# Acceder a un elemento
print(matriz[0][2])

# Modificar un elemento
matriz[0][0] = 1
print(matriz)

# Recorrer una matriz
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Imprime una nueva línea después de cada fila
# Ejemplo 1: Creación y manipulación básica de tuplas

# Creamos una tupla de números
numeros = (1, 2, 3, 4, 5)
print("Tupla original:", numeros)

# Creamos una tupla con diferentes tipos de datos
mixta = (1, "dos", 3.0, [4, 5], (6, 7))
print("Tupla mixta:", mixta)

# Accedemos a elementos por índice
print("Elemento en índice 2:", numeros[2])

# Usamos slicing para obtener una subtupla
subtupla = numeros[1:4]
print("Subtupla [1:4]:", subtupla)

# Intentamos modificar un elemento (esto causará un error)
try:
    numeros[0] = 10
except TypeError as e:
    print("Error al intentar modificar:", str(e))

# Contamos las ocurrencias de un elemento
conteo = numeros.count(3)
print("Número de veces que aparece 3:", conteo)

# Encontramos el índice de un elemento
indice = numeros.index(4)
print("Índice del elemento 4:", indice)

# Explicación:
# - Las tuplas se crean con paréntesis () y los elementos se separan por comas.
# - Pueden contener diferentes tipos de datos, incluyendo otras tuplas o listas.
# - Accedemos a los elementos usando índices, igual que con las listas.
# - El slicing funciona igual que con las listas.
# - Las tuplas son inmutables, por lo que no podemos modificar sus elementos.
# - count() y index() son los únicos métodos disponibles para tuplas.
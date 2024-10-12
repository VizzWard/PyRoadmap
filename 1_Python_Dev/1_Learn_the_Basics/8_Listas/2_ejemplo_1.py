# Ejemplo 1: Creación y manipulación básica de listas

# Creamos una lista de números
numeros = [1, 2, 3, 4, 5]
print("Lista original:", numeros)

# Añadimos un elemento al final de la lista
numeros.append(6)
print("Después de append(6):", numeros)

# Insertamos un elemento en una posición específica
numeros.insert(0, 0)
print("Después de insert(0, 0):", numeros)

# Eliminamos un elemento por su valor
numeros.remove(3)
print("Después de remove(3):", numeros)

# Eliminamos un elemento por su índice
del numeros[2]
print("Después de del numeros[2]:", numeros)

# Accedemos a elementos por índice
print("Elemento en índice 2:", numeros[2])

# Usamos slicing para obtener una sublista
sublista = numeros[1:4]
print("Sublista [1:4]:", sublista)

# Explicación:
# - Las listas se crean con corchetes [], y los elementos se separan por comas.
# - append() añade elementos al final de la lista.
# - insert() añade un elemento en una posición específica.
# - remove() elimina la primera ocurrencia de un valor.
# - del elimina un elemento por su índice.
# - Podemos acceder a elementos individuales usando su índice entre corchetes.
# - El slicing (lista[inicio:fin]) nos permite obtener una porción de la lista.
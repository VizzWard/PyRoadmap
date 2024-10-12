# Ejemplo 2: Operaciones avanzadas con listas

# Creamos dos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Concatenamos las listas
lista_concatenada = lista1 + lista2
print("Listas concatenadas:", lista_concatenada)

# Multiplicamos una lista
lista_multiplicada = lista1 * 3
print("Lista multiplicada por 3:", lista_multiplicada)

# Ordenamos una lista
numeros_desordenados = [3, 1, 4, 1, 5, 9, 2, 6, 5]
numeros_desordenados.sort()
print("Lista ordenada:", numeros_desordenados)

# Invertimos una lista
numeros_desordenados.reverse()
print("Lista invertida:", numeros_desordenados)

# Encontramos el índice de un elemento
indice = lista_concatenada.index(4)
print("Índice del elemento 4:", indice)

# Contamos las ocurrencias de un elemento
conteo = lista_multiplicada.count(2)
print("Número de veces que aparece 2:", conteo)

# Explicación:
# - Las listas se pueden concatenar con el operador +.
# - Podemos multiplicar una lista por un número para repetir sus elementos.
# - sort() ordena la lista in-place (modifica la lista original).
# - reverse() invierte el orden de los elementos in-place.
# - index() encuentra la posición de la primera ocurrencia de un elemento.
# - count() cuenta cuántas veces aparece un elemento en la lista.
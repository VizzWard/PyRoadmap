# Crear una lista
mi_lista = [1, 2, 3, 9, 4.5]
print(mi_lista)

# Acceder a un elemento
# Por indice
print(mi_lista[0])
print(mi_lista[-1])
# Por sublista
sublista = mi_lista[2:4]
print(sublista)


# Modificar listas:

# Actualizar elemento
mi_lista[3] = 8
print(mi_lista)

# Añadir elementos
# Al final
mi_lista.append(0)
print(mi_lista)
# En una posicion
mi_lista.insert(1, 5)
print(mi_lista)


# Ordenar una lista
mi_lista.sort()
print(mi_lista)

# Conocer el numero menor
print(min(mi_lista))

# Conocer el numero mayor
print(max(mi_lista))

# Conocer si un elemento existe en la lista
print(10 in mi_lista)
# Negacion
print(5 not in mi_lista)

# Conocer el indice de un elemento
print(mi_lista.index(8))
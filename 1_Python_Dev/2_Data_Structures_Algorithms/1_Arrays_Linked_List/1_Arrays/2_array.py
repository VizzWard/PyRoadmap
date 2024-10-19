import array as arr

# Creacion de una array
a = arr.array('i', [1,2,3,4,5])

# Recorrer la lista y imprimir cada elemento
for i in a:
    print(i, end=' ')
print('')

# Acceder a un elemento:
print('Elemnto 0:' , a[0])

# Longitud del array
print('Longitud:' , len(a))

# Anadir un elemento

a.append(6)
print('Añadir al final:', *a)

a.extend([7,8,9])
print('Añadir varios elementos:', *a)

a.insert(0,0)
print('Insertar en una posicion:', *a)

# Eliminar el ultimo elemento
a.pop()
print('Eliminar ultimo elemento:', *a)

a.pop(0)
print('Eliminar primer elemento:', *a)

#
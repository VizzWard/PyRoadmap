''' Clase 1 '''

# Crear un diccionario
mi_diccionario = {}

''' Clase 2 '''

# Añadir elementos
mi_diccionario['nombre'] = 'Vicente'
mi_diccionario['edad'] = 22
mi_diccionario['nacionalidad'] = 'Mexicano'
print(mi_diccionario)

# Acceder a elementos
print(mi_diccionario['nombre'])

# Modificar elementos
mi_diccionario['edad'] = 23
print(mi_diccionario)

# Conocer la longitud del diccionario
print(len(mi_diccionario)) # Devuelve la cantidad de llaves almacenadas


''' Clase 3 '''

diccionario = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}

# Obtener el valor
valor = diccionario['a'] # Solamente se obtendra el valor si existe, si no existe lanza un error (keyerror)
print(valor)
# Para eviter el error podemos usar:
print('b' in diccionario) # Comprobar si existe
# Obtener el valor de forma segura:
valor = diccionario.get('c') # Si existe devuelve el valor, si no existe devuelve 'none'
print(valor)

# Obtener el valor, si no existe lo crea
valor = diccionario.setdefault('e', 5)
print(valor)
print(diccionario)


''' Clase 4 '''

# keys
# Obtener las llaves en un diccionario
llaves = tuple(diccionario.keys()) # Usamos tuple para convertir la lista obtenida a tupla
print(llaves)

# values
# Obtener los valores en un diccionario
valores = tuple(diccionario.values())
print(valores)

# items
# Obtener los elementos en un diccionario
elementos = tuple(diccionario.items())
print(elementos)


''' Clase 5 '''

dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
print(dict)

# Eliminar elementos
del dict['a']
print(dict)

# Otra forma de eliminar
valor = dict.pop('b') # Retorna el valor de la llave y lo elimina
print(valor)
print(dict)
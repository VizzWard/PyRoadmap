''' Clase 1'''
# Crear un string
lenguajes = 'Python-Ruby-Java-Go-C+' # Al no tener espacios se toma como una sola cadena de texto
print(lenguajes)

# Separar string y almacenar en una lista
lista_lenguajes = lenguajes.split('-') # Le indicamos que el caracter para separar la cadena sera '-'
print(lista_lenguajes)

# Generar un string a partir de una lista
lenguajes2 = ', '.join(lista_lenguajes)
print(lenguajes2)
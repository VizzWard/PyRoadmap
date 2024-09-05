''' Clase 2 '''

# Los strings son inmutables
# Cuando modificamos un string, lo que hace el lenguaje es generar un nuevo string

nombre = 'Vicente'
apellido = 'Rodriguez'

# Concatenar strings
nombre_completo = nombre + ' ' + apellido
print(nombre_completo)

# Otra forma de concatenar
nombre_completo2 = 'Hola, %s %s' %(nombre, apellido)
print(nombre_completo2)


''' Clase 3 '''

# Metodo format para concatenar
nombre_completo3 = 'Hola, {} {} {}.'.format(nombre, apellido, 'Hidalgo')
print(nombre_completo3)

nombre_completo4 = 'Hola, {nombre} {primer_apellido} {segundo_apellido}.'.format(
    nombre = nombre,
    primer_apellido = apellido,
    segundo_apellido = 'Hidalgo'
)
print(nombre_completo4)


''' Clase 4 '''

#Uso de FSting
nombre_completo5 = f'Hola, {nombre} {apellido}.'
print(nombre_completo5)


''' Clase 5 '''

# Concatenar directamente en print
print(nombre + ' ' + apellido + '.')

print(nombre, apellido, sep=' ')
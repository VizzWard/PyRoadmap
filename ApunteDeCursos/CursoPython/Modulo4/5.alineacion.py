''' Clase 7 '''

mensaje = 'Hola mundo!'

# Justificar texto usando ljust (justificar a la izquierda)
mensaje2 = mensaje.ljust(20) # El argumento es la cantidad de espacios que va a agregar
print(mensaje2, '.')

# Justificar texto usando rjust (justificar a la derecha)
mensaje3 = mensaje.rjust(20)
print(mensaje3, '.')

# Justificar texto usando center (justificar al centro)
mensaje4 = mensaje.center(20)
print(mensaje4)
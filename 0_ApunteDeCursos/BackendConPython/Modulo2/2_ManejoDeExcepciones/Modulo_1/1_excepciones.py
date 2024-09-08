''' Clase 1 '''

''' Clase 2 '''


''' Clase 3 '''


''' Clase 4 '''

# Lanzar una excepcion

num1 = 10
num2 = 0

# try - except
# Lo usaremos para ejecutar la parte del codigo que creamos que lanzara alguna excepcion
try:
    # Al intentar dividir entre 0, lanzará una excepcion 'ZeroDivisionError'
    result = num1 / num2
    print(result)

except ZeroDivisionError: # Except es para ejecutar un bloque si se da algun error
    print('No se puede dividir entre 0')
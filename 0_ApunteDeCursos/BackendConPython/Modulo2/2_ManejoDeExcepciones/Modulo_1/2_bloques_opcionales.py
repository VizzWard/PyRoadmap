''' Clase 5 '''

# Bloques opcionales: else y finally
# else se ejecuta si y solo si, lo que esta en el bloque try no lanza ningun error
# finally se ejecuta independientemente halla o no un error
num1 = 10
num2 = 0
try:
    # Al intentar dividir entre 0, lanzará una excepcion 'ZeroDivisionError'
    result = num1 / num2
except ZeroDivisionError as error: # Except es para ejecutar un bloque si se da algun error
    print('No se puede dividir entre 0')
    print(error)
else:
    print('El resultado es:', result)
finally:
    print('El programa finalizo')
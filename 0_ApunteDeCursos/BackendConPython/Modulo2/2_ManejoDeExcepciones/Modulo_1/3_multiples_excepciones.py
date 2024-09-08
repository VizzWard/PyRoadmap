''' Clase 6 '''

# Multiples errores
# No hay limite de bloques except que se puedan utilizar en un try
num1 = 10
num2 = 0

try:
    number = [1, 2, 3]
    num1 = number[3]
    result = num1 / num2
    result = num1 / num3
except ZeroDivisionError as error:
    print('No se puede dividir entre 0')
except NameError as error:
    print('Variable no encontrada,', error)
except IndexError as error:
    print('No se puede acceder al indice', error)

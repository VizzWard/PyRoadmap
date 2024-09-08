''' Clase 7 '''

# Las excepciones como 'ZeroDivisionError' son heredadas de Exception.
# Por ende podemos utilizar Exception como parte del bloque except, para manejar cualquier tipo de error.
num1 = 10
num2 = 0

try:
    number = [1, 2, 3]
    num1 = number[3]
    result = num1 / num2
    result = num1 / num3
except Exception as error:
    print('No fue posible realizar la tarea,', error)
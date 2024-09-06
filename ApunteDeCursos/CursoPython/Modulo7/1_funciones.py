''' Clase 1 '''

# Crear una funcion
def suma():
    numero_uno = int(input('Ingrese un numero: '))
    numero_dos = int(input('Ingrese un numero: '))

    resultado = numero_uno + numero_dos
    print(resultado)

suma() # Llamar a la funcion

''' Clase 2 '''

# Incluir parametros en las funciones
def resta(num1, num2):
    resultado = num1 - num2
    print(resultado)

numero_uno = 10
numero_dos = 2

# Agregar los argumentos al llamar a la funcion
resta(numero_uno, numero_dos)


''' Clase 3 '''

# Retornar valores
def multiplicacion(num1, num2):
    return num1 * num2

numero_uno = 20
numero_dos = 15

resultado = multiplicacion(numero_uno, numero_dos)
print(resultado)
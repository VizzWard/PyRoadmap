''' Clase 4 '''

# Al asignarle a una variable un valor, el lenguaje lo toma como parametro opcional
# Los parametros con valores, se deben poner al final.
def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2) # Al usar ** se indica que se quiere elevar un numero a la potencia indicada

resultado = area_circulo(10) # Podemos usar la funcion sin todos los parametros
print(resultado)

resultado = area_circulo(12, 3.141592) # O asignarle un valor al parametro opcional
print(resultado)

# Podemos ignorar el orden de los parametros, idicando el nombre del parametro
resultado = area_circulo(pi=3.141592, radio=15)
print(resultado)
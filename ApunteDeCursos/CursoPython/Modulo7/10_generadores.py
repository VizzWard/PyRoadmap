''' Clase 18 '''

# Un generador es un tipo de funcion que retorna objetos que podemos iterar
# esto sin que la funcion finalice
def pares():
    for numero in range(0, 100, 2):
        yield numero # Generador -> lazy iterator
        # A diferencia de return, que finaliza la funcion una vez retorne un valor
        # yield suspende momentaneamente la ejecucion, una vez el objeto es retornado,
        # la funcion se sigue ejecutando en el punto que se quedo.

'''
for par in pares(): # Creamos un for para iterar la funcion.
    print(par)
'''


''' Clase 19 '''

# Generaremos los valores bajo demanda, es decir conforme los vayamos necesitando
generador = pares() # almacenamos los valores de la funcion

print(next(generador)) # Cada que lo llamamos retorna un valor y se pausa, hasta que se vuelve a llamar
print(next(generador)) # reanuda su ejecución y continua donde se quedó.
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
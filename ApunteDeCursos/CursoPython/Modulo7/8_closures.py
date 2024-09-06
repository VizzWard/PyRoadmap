''' Clase 13 '''

# Comportamiento de las variables dentro y fuera de la funciones

def funcion_principal():
    a = 'a'
    b = 'b'

    def funcion_anidada():
        c = 'c' # Variable local de la funcion: funcion_anidada

        nonlocal b # Para modificar la variable de un scope superior usamos nonlocal
        b = 'a' # Variable distinta de b, por estar en diferentes scopes

        print(a)
        print(b)

    funcion_anidada()
    # print(c) # No tiene el alcance para imprimir 'c'

funcion_principal()


''' Clase 14 '''

def saludar():

    def mostrar_mensaje():
        print('Hola')

    return mostrar_mensaje # Asi retornaremos una funcion

respuesta = saludar()
print(respuesta)
print(type(respuesta))

respuesta() # Uso de la funcion por medio de la variable


''' Clase 15 '''

# Closure: es una funcion que genera de forma dinamica a otra funcion
def saludo(username):
    mensaje = f'Hola {username}' # Variable local

    def mostrar_mensaje(): # Funcion anidada
        print(mensaje)

    return mostrar_mensaje

username = 'Vicente'
respuesta = saludo(username)

# Al momento de llamar a la funcion mostrar_mensaje,
# esta aun puede acceder a las variables locales que tenga a su alcance (scope)
respuesta()
# Este es un ejemplo de closure
# Ya que la funcion aun puede acceder a las variables locales que
# fueron creadas durante la ejecucion de la funcion.
# En otras palabras aun puede seguir accediendo a los valores de
# las variables que fueron creadas al momento de la ejecucion.
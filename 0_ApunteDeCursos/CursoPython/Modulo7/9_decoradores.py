''' Clase 16 '''

# Un decorador es una funcion que toma como valor de entrada
# una funcion y retorna otra funcion.

# a -> Funcion principal (decorador)
# b -> Funcion a decorar
# c -> Funcion decorada
# a(b) -> c

# Ejemplo de funcion decorada:
def funcion_a(funcion_b):

    def funcion_c():
        print('Antes del llamado')
        funcion_b() # Llamado de la funcion.
        print('Despues del llamado')

    return funcion_c

@funcion_a # Especificar que esta es la funcion que va a recibir funcion_a.
def saludar(): # Funcion a decorar
    print('Hola')


saludar() # Al llamar a la funcion no estaremos ejecutando al funcion principal, si no que ejecutamos la funcion decorada.
# Con esto extenderemos funcionalidades.
# Agregando funcionalidades antes o despues del llamado de la funcion.

''' Clase 17 '''

# Cuando la funcion a decorar recibe argumentos y retorna algun valor
# tendremos que adaptar el decorador

def decorador(funcion_b): # Decorador

    def funcion_c(*args, **kwargs): # Funcion decorada
        print('Antes del llamado')
        resultado = funcion_b(*args, **kwargs) # Almacenamos el resultado en una variable
        print('Despues del llamado')

        return resultado # Retornamos el resultado

    return funcion_c

@decorador
def suma(num1, num2): # Funcion a decorar
    return num1 + num2

resultado = suma(10, 20)
print(resultado)
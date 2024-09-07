''' Clase 10 '''

def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32

# podemos almacenar una funcion en una variable
mi_funcion = centigrados_a_farhenheit # Poner unicamente el nombre de la funcion, sin los `()`
print(type(mi_funcion))

# Podemos hacer uso de la funcion a traves de la variable
print(mi_funcion(10))


''' Clase 11 '''

# Funciones lambda (funcion anonima), es decir una funcion sin nombre
# Syntax: nombre_variable = lambda parametros : cuerpo de la funcion
funcion_grados = lambda grados : grados * 1.8 + 32
print(funcion_grados(10))
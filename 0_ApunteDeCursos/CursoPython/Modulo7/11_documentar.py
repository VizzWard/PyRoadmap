''' Clase 20 '''

# Docstring -> para documentar una funcion
# Es un comentario que se coloca en la primera lines de la funcion
# Por convencion la documentacion se hara con comillas dobles (""")

def suma(num1, num2):
    """
    La funcion suma dos numeros enteros.

    Argumentos:
    :param num1:
    :param num2:
    :return: Suma de los parametros

    >>> suma(10, 20)
    30

    >>> suma(100, 200)
    300
    """
    return num1 + num2

# Al hacer esto, la documentacion queda guardada en un atributo llamado: __doc__
# Objetos documentable: modulos, clase, objetos, metodos y funciones


# Podemos imprimir este atributo:
print(suma.__doc__)

# Igual podemos obtener la documentacion de la sig manera:
# print(help(suma))



''' Clase 21 '''

# Podemos testear nuestra funcion usando docstring:
# Simulamos en la documentacion el llamado a la funcion en consola
# y debajo ponemos lo que deberia retornar.
# Para ejecutar el test usamos el comando: python -m doctest 11_documentar.py

# Si los test se ejecutan y dan como resultado el valor que hayamos puesto debajo de cada test,
# este se ejecutara sin problemas. En caso contrario, nos dara un error.
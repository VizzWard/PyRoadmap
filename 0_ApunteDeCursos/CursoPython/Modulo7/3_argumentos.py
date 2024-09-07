''' Clase 5 '''

# print es una funcion, ya integrada en el lenguaje
print('String', 10) # Esta no tiene limite de argumentos

# Crearemos una funcion que no tenga limite de argumentos
def promedio(*args): # Al usar * al inicio del parametro, este creara una tupla con los argumentos que se le den.
    # Por convenio al poner * el parametro se llamara args
    return sum(args) / len(args)

resultado = promedio(10, 9, 10, 6, 7, 9)
print(resultado)


''' Clase 6 '''

def combinacion(p1, p2, *args):
    print(p1)
    print(p2)
    print(args)

combinacion(1, 2, 3, 4, 5, 6, 7, 8) # Los argumentos se asignan respecto a su posicion.


''' Clase 7 '''

def usuario(**kwargs): # Al tener ** este se convierte en un diccionario
    # Por convenio al poner ** el parametro se llamara kwargs
    print(kwargs)

usuario(eduardo=[10,9,8,8,10], luis=[10,10,9,9,10]) # Los argumentos deben darse en forma de diccionario.


# Podemos combinar tango *args y **kwargs
def combinaciones(*args, **kwargs):
    print(args)
    print(kwargs)

combinaciones(1, 2, 3, 4, 5, curso=True, lenguaje='Python')
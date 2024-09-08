''' Clase 10 '''

# Podemos lanzar excepciones por grupo

# Crearemos un par de excepciones:
class CustomError(Exception):
    def __init__(self):
        self.msg = 'Error 1'
        super().__init__(self.msg)

class CustomError2(Exception):
    def __init__(self):
        self.msg = 'Error 2'
        super().__init__(self.msg)

class CustomError3(Exception):
    def __init__(self):
        self.msg = 'Error 3'
        super().__init__(self.msg)

try:
    # Para lanzar multiples errores usamos 'ExceptionGroup'
    raise ExceptionGroup('Grupo de excepciones propias:',[CustomError(),CustomError2(),CustomError3()])
# Podemos desempaquetar estos errores:
except *CustomError as e:
    print('CustomError 1')
except *CustomError2 as e:
    print('CustomError 2')
except *CustomError3 as e:
    print('CustomError 3')
# O manejar el grupo completo en una sola excepcion
#except ExceptionGroup as e:
#    print(e)
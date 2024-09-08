''' Clase 9 '''

# Crear excepciones propias
# Se crean a traves de POO
class UsernameException(Exception): # Para que sean consideradas excepciones, deben heredar la clase Exception
    def __init__(self):
        self.message = 'El user debe ser mayor a 6 caracteres' # Le añadimos al error un mensaje
        super().__init__(self.message)

def validate_user(user):
    if len(user) < 6:
        raise UsernameException
    else:
        return True

try:
    result = validate_user('vzw')
    print(result)
except UsernameException as error:
    print(error)
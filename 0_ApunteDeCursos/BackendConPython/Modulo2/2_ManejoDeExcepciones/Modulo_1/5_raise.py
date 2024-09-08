''' Clase 8 '''

# Lanzar excepciones

def validate_user(user):
    if len(user) < 6:
        raise Exception('El user debe ser mayor a 6 caracteres')
    else:
        return True

try:
    result = validate_user('vzw')
    print(result)
except Exception as error:
    print(error)
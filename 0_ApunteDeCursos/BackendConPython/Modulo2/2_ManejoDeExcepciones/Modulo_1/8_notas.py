''' Clase 11'''
from Demos.win32ts_logoff_disconnected import username


# Podemos añadir notas a las excepciones
class UsernameException(Exception):
    def __init__(self):
        super().__init__('Username Invalid')

    def is_valid_to_raise(self):
        return len(self.__notes__) > 0


def username_validation(username):

    username_error = UsernameException()
    if len(username) < 5:
        username_error.add_note('Username too short') # Le añadimos la nota

    if username_error.is_valid_to_raise():
        raise username_error

    return True

username = 'vzw'

username_validation(username)
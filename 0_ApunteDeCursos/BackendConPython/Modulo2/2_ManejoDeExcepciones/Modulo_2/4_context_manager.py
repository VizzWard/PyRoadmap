import contextlib
import logging
import traceback
from lib2to3.fixes.fix_input import context

''' Clase 4 '''

logging.basicConfig(
    level=logging.ERROR,
    filename='errors.log', # Con este parametro, almacenaremos los errores en un archivo
    # Podemos modificar el formato de los errores
    format="%(asctime)s:%(levelname)s:%(message)s"
)

# Podemos crear una funcion en la que tengamos la configuracion del bloque except,
# para asi usarlo en cualquier bloque try except
@contextlib.contextmanager
def write_log_error():
    try:
        yield
    except Exception as error:
        exception_info = {
            'message': str(error),
            'detail': traceback.format_exc()
        }
        logging.error(str(exception_info))

with write_log_error():
    num = 10 / 0
    print(num)
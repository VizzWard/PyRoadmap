import logging
import traceback
''' Clase 2 '''

# Generar un archivo de logs, a partir de las excepciones que ocurran en el codigo
# Los logs por default se imprimira en consola

# podemos modificar estos, para almacenarlos en un archivo
logging.basicConfig(
    level=logging.ERROR,
    filename='errors.log', # Con este parametro, almacenaremos los errores en un archivo
    # Podemos modificar el formato de los errores
    format="%(asctime)s:%(levelname)s:%(message)s"
)

try:
    num1 = 10 / 0
except Exception as error:
    # Generada la excepcion, creamos un log
    exception_info = {
        'message': str(error),
        'detail': traceback.format_exc()
    }
    logging.error(str(exception_info))
import logging # importamos la clase logging

'''' Clase 1 '''

# Generar archivos logs
# Que nos servira como un historial de los errores


#Modulo logging
# Nos permite imprimir mensajes en consola
# y estos se encontraran categorizados en INFO, DEBUG, WARNING, ERROR, CRITICAL
# cada categoria tiene un nivel de error, 10, 20, 30, 40 y 50 respectivamente. A mayor nivel mas critico.

# Por default solo se mostraran los mensajes de nivel 30 o mayor
# Para visualizar todos los mensajes usamos:
logging.basicConfig(level=logging.INFO)

# Mensaje de tipo ingo
logging.info('Mensaje informativo')

# Mensaje debug
logging.debug('Mensaje debug')

# Mensaje warning
logging.warning('Mensaje warning')

# Mensaje error
logging.error('Mensaje error')

# Mensaje critico
logging.critical('Mensaje critical')


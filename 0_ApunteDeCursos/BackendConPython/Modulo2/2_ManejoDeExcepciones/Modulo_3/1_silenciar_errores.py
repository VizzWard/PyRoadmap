from contextlib import suppress
''' Clase 1 '''

# Silenciar errores
try:
    raise Exception('No se puede continuar')
except Exception as e:
    pass # Podemos ignorar el error solamento con no hacer nada en el bloque except

# Otra forma es con suppress
with suppress(Exception):
    result = 10 / 0
    print(result)
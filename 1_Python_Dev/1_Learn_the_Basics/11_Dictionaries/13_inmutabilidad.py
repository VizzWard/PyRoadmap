# 12. Consideraciones de Inmutabilidad
# Ejemplo 1: Intento de usar una lista como clave (generará un error)
try:
    dic_invalido = {[1, 2, 3]: "lista"}
except TypeError as e:
    print("Error al usar lista como clave:", str(e))

# Ejemplo 2: Uso de tupla como clave (válido)
dic_valido = {(1, 2, 3): "tupla"}
print("Diccionario con tupla como clave:", dic_valido)
# Ejemplo de uso de dict(), callable(), y breakpoint()

# Creación de un diccionario
mi_diccionario = dict(nombre="Alice", edad=30, ciudad="Madrid")
print("Diccionario:", mi_diccionario)

# Comprobando si un objeto es callable
def funcion_ejemplo():
    return "¡Hola!"

es_callable = callable(funcion_ejemplo)
print(f"¿La función es callable? {es_callable}")

# Iniciar el depurador (descomentar la siguiente línea para usarlo)
# breakpoint()
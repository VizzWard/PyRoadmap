# 9. Comprensión de Diccionarios
# Ejemplo 1: Cuadrados de números
cuadrados = {x: x**2 for x in range(1, 6)}
print("Cuadrados:", cuadrados)

# Ejemplo 2: Filtrado con comprensión de diccionarios
nombres = ["Ana", "Juan", "María", "Pedro", "Lucía"]
nombres_longitud = {nombre: len(nombre) for nombre in nombres if len(nombre) > 3}
print("Nombres y longitudes (más de 3 letras):", nombres_longitud)
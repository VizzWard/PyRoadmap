# 7. Iteración sobre Diccionarios
# Ejemplo 1: Iteración sobre claves
colores = {"rojo": "#FF0000", "verde": "#00FF00", "azul": "#0000FF"}
for color in colores:
    print(f"Color: {color}, Código: {colores[color]}")

# Ejemplo 2: Iteración sobre items
for color, codigo in colores.items():
    print(f"El código de {color} es {codigo}")
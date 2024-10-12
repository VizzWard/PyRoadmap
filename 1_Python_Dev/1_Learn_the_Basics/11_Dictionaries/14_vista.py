# 13. Métodos de Vista
# Ejemplo 1: Demostración de vista dinámica con keys()
numeros = {"uno": 1, "dos": 2, "tres": 3}
claves = numeros.keys()
print("Claves originales:", claves)
numeros["cuatro"] = 4
print("Claves después de añadir un elemento:", claves)

# Ejemplo 2: Uso de vistas en bucles
valores = numeros.values()
for valor in valores:
    print(f"El doble de {valor} es {valor * 2}")
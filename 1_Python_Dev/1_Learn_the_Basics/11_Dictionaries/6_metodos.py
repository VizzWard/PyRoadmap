# 5. Métodos de Diccionarios
# Ejemplo 1: keys(), values(), items()
frutas = {"manzana": 3, "banana": 2, "naranja": 4}
print("Claves:", frutas.keys())
print("Valores:", frutas.values())
print("Items:", frutas.items())

# Ejemplo 2: update() y pop()
frutas.update({"pera": 1, "uva": 5})
print("Diccionario actualizado:", frutas)
fruta_eliminada = frutas.pop("banana")
print(f"Fruta eliminada: {fruta_eliminada}. Diccionario actual: {frutas}")
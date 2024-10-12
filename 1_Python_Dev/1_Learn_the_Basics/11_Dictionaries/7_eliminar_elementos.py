# 6. Eliminación de Elementos
# Ejemplo 1: Usando del
numeros = {"uno": 1, "dos": 2, "tres": 3}
del numeros["dos"]
print("Después de eliminar 'dos':", numeros)

# Ejemplo 2: Usando popitem()
ultimo_item = numeros.popitem()
print(f"Último item eliminado: {ultimo_item}. Diccionario actual: {numeros}")
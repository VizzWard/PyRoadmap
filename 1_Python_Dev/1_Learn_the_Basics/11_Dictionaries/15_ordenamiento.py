from collections import OrderedDict

# 14. Ordenamiento
# Ejemplo 1: Mantener orden de inserción (Python 3.7+)

dict_ordenado = OrderedDict()
dict_ordenado["c"] = 3
dict_ordenado["a"] = 1
dict_ordenado["b"] = 2
print("OrderedDict:", dict_ordenado)

# Ejemplo 2: Ordenar un diccionario por valores
diccionario = {"banana": 3, "manzana": 1, "naranja": 2}
ordenado_por_valor = dict(sorted(diccionario.items(), key=lambda item: item[1]))
print("Diccionario ordenado por valor:", ordenado_por_valor)
# Ejemplo 3: Sets comprehensions y operaciones avanzadas

# Creamos un set usando set comprehension
cuadrados_pares = {x**2 for x in range(10) if x % 2 == 0}
print("Cuadrados de números pares del 0 al 9:", cuadrados_pares)

# Frozen set (set inmutable)
frozenset_ejemplo = frozenset([1, 2, 3, 4, 5])
print("Frozen set:", frozenset_ejemplo)

# Intentamos modificar el frozen set (esto causará un error)
try:
    frozenset_ejemplo.add(6)
except AttributeError as e:
    print("Error al intentar modificar el frozen set:", str(e))

# Uso de sets para eliminar duplicados de una lista manteniendo el orden
def eliminar_duplicados_ordenados(lista):
    return list(dict.fromkeys(lista))

lista_con_duplicados = [1, 2, 2, 3, 4, 3, 5, 1, 4]
lista_sin_duplicados = eliminar_duplicados_ordenados(lista_con_duplicados)
print("Lista original:", lista_con_duplicados)
print("Lista sin duplicados, manteniendo orden:", lista_sin_duplicados)

# Uso de sets para encontrar elementos únicos en múltiples listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
lista3 = [7, 8, 9, 10]

elementos_unicos = set(lista1) ^ set(lista2) ^ set(lista3)
print("Elementos únicos en las tres listas:", elementos_unicos)

# Explicación:
# - Set comprehensions permiten crear sets de manera concisa basados en iteraciones y condiciones.
# - frozenset crea una versión inmutable de un set.
# - Los sets son útiles para eliminar duplicados, pero no mantienen el orden.
#   Podemos usar un truco con dict.fromkeys() para eliminar duplicados manteniendo el orden.
# - Los sets son eficientes para encontrar elementos únicos o comunes entre múltiples colecciones.
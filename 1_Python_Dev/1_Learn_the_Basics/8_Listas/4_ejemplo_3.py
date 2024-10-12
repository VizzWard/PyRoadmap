# Ejemplo 3: List comprehensions y funciones de alto nivel

# Creamos una lista usando list comprehension
cuadrados = [x**2 for x in range(10)]
print("Cuadrados del 0 al 9:", cuadrados)

# Filtramos elementos usando list comprehension
pares = [x for x in cuadrados if x % 2 == 0]
print("Números pares de la lista de cuadrados:", pares)

# Usamos map() para aplicar una función a cada elemento
def duplicar(x):
    return x * 2

duplicados = list(map(duplicar, cuadrados))
print("Lista de cuadrados duplicados:", duplicados)

# Usamos filter() para filtrar elementos
def es_divisible_por_3(x):
    return x % 3 == 0

divisibles_por_3 = list(filter(es_divisible_por_3, cuadrados))
print("Números divisibles por 3:", divisibles_por_3)

# Usamos reduce() para aplicar una función acumulativa
from functools import reduce

def sumar(x, y):
    return x + y

suma_total = reduce(sumar, cuadrados)
print("Suma de todos los cuadrados:", suma_total)

# Explicación:
# - Las list comprehensions son una forma concisa de crear listas basadas en iteraciones y condiciones.
# - map() aplica una función a cada elemento de un iterable y devuelve un iterador con los resultados.
# - filter() crea un iterador con los elementos que cumplen una condición dada por una función.
# - reduce() aplica una función de dos argumentos acumulativamente a los elementos de un iterable.
# - Estas funciones de alto nivel (map, filter, reduce) son útiles para operaciones funcionales en listas.
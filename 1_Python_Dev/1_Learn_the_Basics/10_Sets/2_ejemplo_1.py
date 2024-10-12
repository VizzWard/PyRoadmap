# Ejemplo 1: Creación y operaciones básicas con sets

# Creamos un set de números
numeros = {1, 2, 3, 4, 5}
print("Set original:", numeros)

# Creamos un set a partir de una lista (elimina duplicados automáticamente)
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 5, 5]
set_sin_duplicados = set(lista_con_duplicados)
print("Set sin duplicados:", set_sin_duplicados)

# Añadimos un elemento al set
numeros.add(6)
print("Después de add(6):", numeros)

# Intentamos añadir un elemento duplicado (no tendrá efecto)
numeros.add(5)
print("Después de intentar añadir 5 de nuevo:", numeros)

# Eliminamos un elemento del set
numeros.remove(3)
print("Después de remove(3):", numeros)

# Intentamos eliminar un elemento que no existe
try:
    numeros.remove(10)
except KeyError as e:
    print("Error al intentar eliminar 10:", str(e))

# Usamos discard() para eliminar un elemento sin lanzar error si no existe
numeros.discard(10)
print("Después de discard(10):", numeros)

# Verificamos la pertenencia de un elemento
print("¿Está 4 en el set?", 4 in numeros)
print("¿Está 10 en el set?", 10 in numeros)

# Explicación:
# - Los sets se crean con llaves {} o la función set().
# - Los sets automáticamente eliminan duplicados.
# - add() añade un elemento al set si no existe.
# - remove() elimina un elemento, pero lanza un KeyError si no existe.
# - discard() elimina un elemento sin lanzar error si no existe.
# - Podemos verificar la pertenencia de un elemento con el operador 'in'.
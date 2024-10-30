from collections import deque

# Diferentes formas de inicializar un deque
d1 = deque(['a', 'b', 'c'])                    # Con lista
d2 = deque('abc')                              # Con string
d3 = deque([{'data': 'a'}, {'data': 'b'}])    # Con lista de diccionarios

# Operaciones básicas con deque
llist = deque("abcde")
print("Inicial:", llist)

# Operaciones al final
llist.append("f")
print("Después de append:", llist)
llist.pop()
print("Después de pop:", llist)

# Operaciones al inicio
llist.appendleft("z")
print("Después de appendleft:", llist)
llist.popleft()
print("Después de popleft:", llist)

# Funcionalidades adicionales útiles
llist.extend(['x', 'y'])           # Añade múltiples elementos al final
print("Después de extend:", llist)

llist.extendleft(['1', '2'])       # Añade múltiples elementos al inicio
print("Después de extendleft:", llist)

# Rotación de elementos
llist.rotate(1)                    # Rota un paso a la derecha
print("Después de rotate(1):", llist)
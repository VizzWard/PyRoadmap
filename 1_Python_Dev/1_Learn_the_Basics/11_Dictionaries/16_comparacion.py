import time

# 15. Comparación con Otros Tipos de Datos
# Ejemplo 1: Comparación de tiempo de inserción entre lista y diccionario

lista_tiempo = []
dict_tiempo = {}

inicio = time.time()
for i in range(100000):
    lista_tiempo.append(i)
fin = time.time()
print(f"Tiempo de inserción en lista: {fin - inicio} segundos")

inicio = time.time()
for i in range(100000):
    dict_tiempo[i] = i
fin = time.time()
print(f"Tiempo de inserción en diccionario: {fin - inicio} segundos")

# Ejemplo 2: Uso de set vs lista para verificar membresía
lista_miembros = list(range(10000))
set_miembros = set(range(10000))

inicio = time.time()
for _ in range(1000):
    _ = 9999 in lista_miembros
fin = time.time()
print(f"Tiempo de verificación de membresía en lista: {fin - inicio} segundos")

inicio = time.time()
for _ in range(1000):
    _ = 9999 in set_miembros
fin = time.time()
print(f"Tiempo de verificación de membresía en set: {fin - inicio} segundos")
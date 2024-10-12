import time

# 11. Rendimiento
# Ejemplo 1: Comparación de tiempo de acceso entre lista y diccionario

# Creamos una lista y un diccionario grandes
lista_grande = list(range(1000000))
dict_grande = {str(i): i for i in range(1000000)}

# Medimos el tiempo de acceso a un elemento en la lista
inicio = time.time()
_ = 999999 in lista_grande
fin = time.time()
print(f"Tiempo de búsqueda en lista: {fin - inicio} segundos")

# Medimos el tiempo de acceso a un elemento en el diccionario
inicio = time.time()
_ = "999999" in dict_grande
fin = time.time()
print(f"Tiempo de búsqueda en diccionario: {fin - inicio} segundos")

# Ejemplo 2: Uso de diccionario para optimizar búsquedas
def buscar_en_lista(lista, elemento):
    return elemento in lista

def buscar_en_dict(diccionario, elemento):
    return elemento in diccionario

lista_numeros = list(range(10000))
dict_numeros = {str(i): i for i in range(10000)}

inicio = time.time()
for _ in range(1000):
    buscar_en_lista(lista_numeros, 9999)
fin = time.time()
print(f"Tiempo total de búsquedas en lista: {fin - inicio} segundos")

inicio = time.time()
for _ in range(1000):
    buscar_en_dict(dict_numeros, "9999")
fin = time.time()
print(f"Tiempo total de búsquedas en diccionario: {fin - inicio} segundos")
# Ejemplo 3: Tuplas nombradas y uso de tuplas en diccionarios

from collections import namedtuple

# Creamos una tupla nombrada
Persona = namedtuple('Persona', ['nombre', 'edad', 'ciudad'])

# Creamos una instancia de la tupla nombrada
persona1 = Persona('Alice', 30, 'Nueva York')
print("Persona:", persona1)

# Accedemos a los elementos por nombre
print(f"Nombre: {persona1.nombre}, Edad: {persona1.edad}, Ciudad: {persona1.ciudad}")

# Usamos tuplas como claves en un diccionario
coordenadas = {
    (0, 0): 'Origen',
    (1, 0): 'Este',
    (0, 1): 'Norte',
    (-1, 0): 'Oeste',
    (0, -1): 'Sur'
}

# Accedemos a valores usando tuplas como claves
print("Ubicación en (0, 0):", coordenadas[(0, 0)])
print("Ubicación en (1, 0):", coordenadas[(1, 0)])

# Iteramos sobre el diccionario de tuplas
for coordenada, ubicacion in coordenadas.items():
    print(f"Coordenada {coordenada}: {ubicacion}")

# Explicación:
# - namedtuple crea una subclase de tupla con campos nombrados.
# - Las tuplas nombradas permiten acceder a los elementos por nombre, además de por índice.
# - Las tuplas pueden usarse como claves en diccionarios porque son inmutables.
# - Esto es útil para representar pares de valores como coordenadas.
# - Las tuplas son eficientes en memoria y rápidas para acceder, lo que las hace ideales como claves.
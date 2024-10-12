# Ejemplo de Retorno de Valores en Funciones Python

# Ejemplo 1: Retorno de múltiples valores y desempaquetado
def analizar_texto(texto):
    """
    Analiza un texto y retorna varias estadísticas.

    Esta función demuestra cómo una función puede retornar múltiples valores.
    En Python, esto se logra retornando una tupla, que luego puede ser
    desempaquetada al llamar a la función.

    :param texto: str - El texto a analizar
    :return: tuple - Una tupla conteniendo:
        - int: Número de caracteres
        - int: Número de palabras
        - int: Número de frases
        - str: La palabra más larga
    """
    # Contar caracteres (incluyendo espacios y puntuación)
    num_caracteres = len(texto)

    # Contar palabras
    palabras = texto.split()
    num_palabras = len(palabras)

    # Contar frases (asumiendo que las frases terminan en '.', '!' o '?')
    num_frases = texto.count('.') + texto.count('!') + texto.count('?')

    # Encontrar la palabra más larga
    palabra_mas_larga = max(palabras, key=len)

    # Retornar múltiples valores como una tupla
    return num_caracteres, num_palabras, num_frases, palabra_mas_larga


# Uso de la función y desempaquetado de los valores retornados
texto_ejemplo = "¡Hola mundo! Este es un ejemplo de texto. Contiene múltiples frases y palabras."
caracteres, palabras, frases, palabra_larga = analizar_texto(texto_ejemplo)

print(f"Análisis del texto:")
print(f"Número de caracteres: {caracteres}")
print(f"Número de palabras: {palabras}")
print(f"Número de frases: {frases}")
print(f"Palabra más larga: '{palabra_larga}'")
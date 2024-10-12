# Ejemplo de uso de bin(), chr(), y len()

# Conversión a binario
numero_entero = 42
binario = bin(numero_entero)
print(f"El número {numero_entero} en binario es {binario}")

# Obtener carácter Unicode
codigo_unicode = 65  # 'A'
caracter = chr(codigo_unicode)
print(f"El carácter Unicode para el código {codigo_unicode} es '{caracter}'")

# Longitud de una cadena
cadena = "Hola, Mundo!"
longitud = len(cadena)
print(f"La longitud de la cadena '{cadena}' es {longitud}")
# Ejemplo 2: Tuplas como retorno de funciones y desempaquetado

def obtener_datos():
    return (10, "Hola", 3.14)

# Obtenemos una tupla como retorno de una función
resultado = obtener_datos()
print("Tupla retornada:", resultado)

# Desempaquetado de tupla
numero, texto, pi = resultado
print(f"Desempaquetado: numero = {numero}, texto = '{texto}', pi = {pi}")

# Desempaquetado con * para capturar elementos restantes
primero, *resto = numeros
print(f"Primer elemento: {primero}, Resto: {resto}")

# Intercambio de variables usando tuplas
a, b = 1, 2
print(f"Antes del intercambio: a = {a}, b = {b}")
a, b = b, a
print(f"Después del intercambio: a = {a}, b = {b}")

# Explicación:
# - Las funciones pueden retornar múltiples valores empaquetados en una tupla.
# - El desempaquetado de tuplas permite asignar sus elementos a variables individuales.
# - El operador * en el desempaquetado captura múltiples elementos en una lista.
# - Las tuplas permiten un intercambio de variables sencillo y eficiente.
# Ejemplo de uso de abs(), all(), y any()

# Valor absoluto
numero = -10
valor_absoluto = abs(numero)
print(f"El valor absoluto de {numero} es {valor_absoluto}")

# Comprobando si todos los elementos son verdaderos
lista = [True, True, False]
todos_verdaderos = all(lista)
print(f"¿Todos los elementos son verdaderos? {todos_verdaderos}")

# Comprobando si al menos un elemento es verdadero
algun_verdadero = any(lista)
print(f"¿Al menos un elemento es verdadero? {algun_verdadero}")
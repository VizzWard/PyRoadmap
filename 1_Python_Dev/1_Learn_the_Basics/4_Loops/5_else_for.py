# Ejemplo 1: Buscar un número par
for num in range(1, 6):
    if num % 2 == 0:
        print(f"Número par encontrado: {num}")
        break
else:
    print("No se encontraron números pares")

# Ejemplo 2: Verificar si todos los elementos cumplen una condición
numeros = [1, 3, 5, 7, 9]
for num in numeros:
    if num % 2 == 0:
        print("Se encontró un número par")
        break
else:
    print("Todos los números son impares")
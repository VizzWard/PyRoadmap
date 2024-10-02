# Ejemplo 1: Contador simple
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# Ejemplo 2: Adivinar un número
import random
numero_secreto = random.randint(1, 10)
adivinanza = 0
while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (1-10): "))
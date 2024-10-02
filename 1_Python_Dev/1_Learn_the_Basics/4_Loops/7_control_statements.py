# Ejemplo 1: For con continue, pass y break
for i in range(10):
    if i % 2 == 0:
        continue  # Salta los números pares
    if i == 7:
        break  # Termina el bucle en 7
    if i == 5:
        pass  # No hace nada especial para 5
    print(i)

# Ejemplo 2: While con continue, pass y break
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue  # Salta los números pares
    if contador == 7:
        break  # Termina el bucle en 7
    if contador == 5:
        pass  # No hace nada especial para 5
    print(contador)
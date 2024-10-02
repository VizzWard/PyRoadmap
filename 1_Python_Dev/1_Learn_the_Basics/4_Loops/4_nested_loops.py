import random

# Bucle for anidado

## Ejemplo 1: Tabla de multiplicar
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("----")

## Ejemplo 2: Patrones
for i in range(4):
    for j in range(i+1):
        print("*", end="")
    print()


# Bucle while anidado

## Ejemplo 1: Menú y submenú
opcion_principal = None
while opcion_principal != "salir":
    opcion_principal = input("Menú principal (comida/bebida/salir): ")
    if opcion_principal in ["comida", "bebida"]:
        opcion_secundaria = None
        while opcion_secundaria != "volver":
            opcion_secundaria = input(f"Submenú de {opcion_principal} (elige o 'volver'): ")
            if opcion_secundaria != "volver":
                print(f"Has elegido {opcion_secundaria} de {opcion_principal}")

## Ejemplo 2: Juego de adivinanza con vidas
vidas = 3
while vidas > 0:
    numero_secreto = random.randint(1, 10)
    adivinado = False
    while not adivinado and vidas > 0:
        intento = int(input(f"Adivina el número (1-10), te quedan {vidas} vidas: "))
        if intento == numero_secreto:
            print("¡Correcto!")
            adivinado = True
        else:
            vidas -= 1
            print("Incorrecto.")
    if vidas > 0:
        print("¿Quieres jugar otra vez?")
    else:
        print("Game Over")
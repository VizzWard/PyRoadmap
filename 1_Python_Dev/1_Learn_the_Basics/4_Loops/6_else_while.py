# Ejemplo 1: Intentos limitados
intentos = 3
while intentos > 0:
    password = input("Ingresa la contraseña: ")
    if password == "secreto":
        print("Acceso concedido")
        break
    intentos -= 1
else:
    print("Has agotado tus intentos")

# Ejemplo 2: Búsqueda en lista
lista = [1, 3, 5, 7, 9]
objetivo = 6
i = 0
while i < len(lista):
    if lista[i] == objetivo:
        print(f"Encontrado en posición {i}")
        break
    i += 1
else:
    print("El número no está en la lista")
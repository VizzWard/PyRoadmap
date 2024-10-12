# Ejemplo de Recursión en Python: Torre de Hanoi

def hanoi(n, origen, destino, auxiliar):
    """
    Resuelve el problema de la Torre de Hanoi usando recursión.

    :param n: int - Número de discos
    :param origen: str - Nombre de la torre de origen
    :param destino: str - Nombre de la torre de destino
    :param auxiliar: str - Nombre de la torre auxiliar
    """
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return

    # Mover n-1 discos de origen a auxiliar
    hanoi(n - 1, origen, auxiliar, destino)

    # Mover el disco n de origen a destino
    print(f"Mover disco {n} de {origen} a {destino}")

    # Mover n-1 discos de auxiliar a destino
    hanoi(n - 1, auxiliar, destino, origen)


# Función para visualizar el proceso
def visualizar_hanoi(n):
    """
    Visualiza el proceso de resolución de la Torre de Hanoi.

    :param n: int - Número de discos
    """
    torres = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }

    def imprimir_torres():
        for torre, discos in torres.items():
            print(f"Torre {torre}: {discos}")
        print()

    def mover_disco(origen, destino):
        disco = torres[origen].pop()
        torres[destino].append(disco)
        print(f"Mover disco {disco} de {origen} a {destino}")
        imprimir_torres()

    def hanoi_visual(n, origen, destino, auxiliar):
        if n == 1:
            mover_disco(origen, destino)
            return

        hanoi_visual(n - 1, origen, auxiliar, destino)
        mover_disco(origen, destino)
        hanoi_visual(n - 1, auxiliar, destino, origen)

    print("Estado inicial:")
    imprimir_torres()
    hanoi_visual(n, 'A', 'C', 'B')


# Ejemplo de uso
print("Solución para la Torre de Hanoi con 3 discos:")
hanoi(3, 'A', 'C', 'B')

print("\nVisualización del proceso para la Torre de Hanoi con 3 discos:")
visualizar_hanoi(3)


# Análisis de la complejidad
def contar_movimientos(n):
    """
    Cuenta el número de movimientos necesarios para resolver la Torre de Hanoi.

    :param n: int - Número de discos
    :return: int - Número de movimientos
    """
    if n == 1:
        return 1
    return 2 * contar_movimientos(n - 1) + 1


print("\nAnálisis de complejidad:")
for i in range(1, 6):
    movimientos = contar_movimientos(i)
    print(f"Para {i} discos: {movimientos} movimientos")

# Explicación de la recursión
"""
Explicación de la recursión en la Torre de Hanoi:

1. Caso base: Si solo hay un disco, simplemente lo movemos del origen al destino.

2. Caso recursivo:
    a. Movemos n-1 discos del origen al auxiliar (usando el destino como auxiliar).
    b. Movemos el disco n del origen al destino.
    c. Movemos los n-1 discos del auxiliar al destino (usando el origen como auxiliar).

La recursión funciona dividiendo el problema en subproblemas más pequeños:
- Resolver para n discos implica resolver primero para n-1 discos.
- Cada llamada recursiva reduce el número de discos hasta llegar al caso base.

La complejidad temporal de este algoritmo es O(2^n), lo que significa que el número
de movimientos crece exponencialmente con el número de discos.
"""
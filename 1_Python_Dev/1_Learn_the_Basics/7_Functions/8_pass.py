# Ejemplo de Uso de 'pass' en Python

# Ejemplo 1: Uso de 'pass' en la definición de clases y funciones

class ClaseEnDesarrollo:
    """
    Esta clase está en desarrollo y aún no tiene métodos implementados.
    """
    pass

def funcion_por_implementar():
    """
    Esta función está planificada pero aún no se ha implementado.
    """
    pass

# Uso de las clases y funciones vacías
objeto = ClaseEnDesarrollo()
print(f"Objeto creado: {objeto}")

funcion_por_implementar()
print("La función fue llamada pero no hizo nada.")

# Ejemplo de uso en un bucle
for i in range(5):
    if i == 2:
        pass  # No hacemos nada especial para i == 2
    else:
        print(f"El valor de i es: {i}")

print("\n--- Fin del Ejemplo 1 ---\n")

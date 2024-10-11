import time

# Ejemplo de try-except-finally
try:
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("El archivo no se encontró.")
finally:
    print("Cerrando recursos...")
    if 'archivo' in locals():
        archivo.close()


# Ejemplo adicional de try-except-finally
try:
    print("Iniciando proceso...")
    time.sleep(2)
    # Simulamos un error
    raise Exception("¡Ocurrió un error inesperado!")
except Exception as e:
    print(f"Se capturó una excepción: {e}")
finally:
    print("Finalizando proceso, limpiando recursos...")
    time.sleep(1)
    print("Proceso terminado.")
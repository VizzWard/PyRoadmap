# Ejemplo de try-except-else
try:
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no se encontró.")
else:
    print("Contenido del archivo:")
    print(contenido)
    archivo.close()
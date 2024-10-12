# Ejemplos de Argumentos en Funciones Python

# 1. Argumentos posicionales
# Formato: def función(arg1, arg2, ...)
# Tipo de datos: Cualquier tipo (en este caso, ambos son strings)
def saludar(nombre, mensaje):
    print(f"{mensaje}, {nombre}!")

saludar("María", "Hola")  # Salida: Hola, María!
saludar("Juan", "Bienvenido")  # Salida: Bienvenido, Juan!



# 2. Argumentos de palabra clave (keyword arguments)
# Formato: función(arg1=valor1, arg2=valor2, ...)
# Tipo de datos: Cualquier tipo (aquí, dos strings y un int)
def describir_persona(nombre, edad, ciudad):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")

describir_persona(nombre="Ana", edad=30, ciudad="Madrid")
describir_persona(ciudad="Barcelona", nombre="Carlos", edad=25)



# 3. Argumentos por defecto
# Formato: def función(arg1, arg2=valor_por_defecto)
# Tipo de datos: Cualquier tipo (aquí, un string y otro string con valor por defecto)
def saludar_con_idioma(nombre, idioma="español"):
    if idioma == "español":
        print(f"Hola, {nombre}")
    elif idioma == "inglés":
        print(f"Hello, {nombre}")
    else:
        print(f"No reconozco el idioma {idioma}")

saludar_con_idioma("María")  # Usa el valor por defecto "español"
saludar_con_idioma("John", "inglés")
saludar_con_idioma("Pierre", "francés")



# 4. Número variable de argumentos (*args)
# Formato: def función(*args)
# Tipo de datos: Tupla (contiene todos los argumentos posicionales adicionales)
def suma(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

print(suma(1, 2, 3))  # Pasa una tupla (1, 2, 3)
print(suma(10, 20, 30, 40))  # Pasa una tupla (10, 20, 30, 40)



# 5. Número variable de argumentos de palabra clave (**kwargs)
# Formato: def función(**kwargs)
# Tipo de datos: Diccionario (contiene todos los argumentos de palabra clave adicionales)
def imprimir_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

imprimir_info(nombre="Luis", edad=28, profesion="Ingeniero")
# Pasa un diccionario {'nombre': 'Luis', 'edad': 28, 'profesion': 'Ingeniero'}

imprimir_info(titulo="Sr.", apellido="García", pais="España")
# Pasa un diccionario {'titulo': 'Sr.', 'apellido': 'García', 'pais': 'España'}



# 6. Combinación de tipos de argumentos
# Formato: def función(arg1, arg2, *args, kwarg1=valor, **kwargs)
# Tipo de datos: Combinación de tipos (posicionales, tupla, valor por defecto, diccionario)
def funcion_mixta(arg1, arg2, *args, kwarg1="default", **kwargs):
    print(f"arg1: {arg1}")  # Argumento posicional
    print(f"arg2: {arg2}")  # Argumento posicional
    print(f"args: {args}")  # Tupla de argumentos adicionales
    print(f"kwarg1: {kwarg1}")  # Argumento de palabra clave con valor por defecto
    print(f"kwargs: {kwargs}")  # Diccionario de argumentos de palabra clave adicionales

funcion_mixta(1, 2, 3, 4, 5, kwarg1="no default", x=10, y=20)



# 7. Argumentos posicionales obligatorios (Python 3.8+)
# Formato: def función(arg1, arg2, /)
# Tipo de datos: Cualquier tipo, pero deben ser pasados posicionalmente
def multiplicar(a, b, /):
    return a * b

print(multiplicar(3, 4))  # Válido
# print(multiplicar(a=3, b=4))  # Esto causaría un error



# 8. Argumentos de solo palabra clave
# Formato: def función(*, kwarg1=valor1, kwarg2=valor2)
# Tipo de datos: Cualquier tipo, pero deben ser pasados como argumentos de palabra clave
def configurar(*, host='localhost', puerto=8080):
    print(f"Configuración: host={host}, puerto={puerto}")

configurar(puerto=8000)
# configurar(8000)  # Esto causaría un error



# 9. Desempaquetado de argumentos
# Formato: función(*lista) o función(**diccionario)
# Tipo de datos: Lista o tupla para *, diccionario para **
def suma_tres(a, b, c):
    return a + b + c

numeros = [1, 2, 3]  # Lista
print(suma_tres(*numeros))  # Desempaqueta la lista

datos = {"a": 4, "b": 5, "c": 6}  # Diccionario
print(suma_tres(**datos))  # Desempaqueta el diccionario
# Ejemplo básico de try-except
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"El resultado es: {resultado}")
except ValueError:
    print("Error: Debes ingresar un número válido.")
except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")


# Ejemplo adicional de try-except-else
try:
    edad = int(input("Ingresa tu edad: "))
except ValueError:
    print("Por favor, ingresa un número válido para la edad.")
else:
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")
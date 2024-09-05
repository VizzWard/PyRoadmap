# Entrada de datos


En Python, la función input() se utiliza para capturar datos del usuario a través de la consola. Cuando se llama a input(), el programa se detiene y espera a que el usuario ingrese un valor y presione Enter. El valor ingresado se devuelve como una cadena de texto (str), sin importar el tipo de dato que el usuario haya introducido.

## Uso básico de input()

Sintaxis:

```python
variable = input(prompt)
```

- `prompt` (opcional): Es un mensaje que se muestra al usuario para indicar qué tipo de entrada se espera. Es opcional, pero generalmente se usa para guiar al usuario.

## Consideraciones

- Tipo de dato: Dado que input() siempre devuelve una cadena de texto, si necesitas otro tipo de dato (como un número), debes convertirlo explícitamente:

```python
edad = int(input("¿Cuántos años tienes? "))
print("Tendrás", edad + 1, "el próximo año.")
```

- Seguridad: Ten en cuenta que input() puede ser una fuente de errores si el usuario ingresa un valor inesperado. Por ejemplo, intentar convertir una entrada no numérica a un entero causará un error.

## Convertir a distintos tipos de datos

Para convertir la entrada de la función input() en diferentes tipos de datos en Python, puedes utilizar las funciones de conversión de tipo. Aquí te explico cómo puedes hacerlo para los tipos de datos más comunes:

1. Convertir a Entero (`int`)

```python
entrada = input("Ingresa un número entero: ")
numero = int(entrada)
print("El número ingresado más 10 es:", numero + 10)
```

2. Convertir a Flotante (`float`)

```python
entrada = input("Ingresa un número decimal: ")
numero = float(entrada)
print("La mitad del número ingresado es:", numero / 2)
```

3. Convertir a Booleano (`bool`)

```python
entrada = input("Ingresa algo (esto se convertirá a booleano): ")
booleano = bool(entrada)
print("El valor booleano es:", booleano)
```

4. Convertir a Lista (`list`)

```python
entrada = input("Ingresa varios números separados por comas: ")
lista = entrada.split(",")
print("La lista resultante es:", lista)
```

5. Convertir a otros tipos (como tuple, set)

- A tupla

```python
entrada = input("Ingresa valores separados por comas: ")
tupla = tuple(entrada.split(","))
print("La tupla resultante es:", tupla)
```

- A conjunto

```python
entrada = input("Ingresa valores separados por comas: ")
conjunto = set(entrada.split(","))
print("El conjunto resultante es:", conjunto)
```
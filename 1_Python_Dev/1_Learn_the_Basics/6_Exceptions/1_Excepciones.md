# Excepciones

Las excepciones en Python son un mecanismo fundamental para manejar errores que pueden surgir durante la ejecución de un programa. A continuación, se presenta una explicación detallada sobre qué son las excepciones, cómo manejarlas y los aspectos importantes a considerar.

## ¿Qué son las Excepciones?

Las excepciones son eventos que ocurren durante la ejecución de un programa y que interrumpen su flujo normal. Cuando se produce un error, Python genera una excepción, la cual puede ser manejada para evitar que el programa se detenga abruptamente. Si no se maneja, la excepción provocará que el programa muestre un mensaje de error y termine su ejecución.

## Tipos Comunes de Excepciones

Algunas de las excepciones más comunes en Python incluyen:

- ZeroDivisionError: Ocurre al intentar dividir por cero.
- TypeError: Se lanza cuando se aplica una operación o función a un tipo de dato inapropiado.
- IndexError: Se produce al intentar acceder a un índice que no existe en una lista o secuencia.
- KeyError: Ocurre al intentar acceder a una clave inexistente en un diccionario.
- FileNotFoundError: Se lanza al intentar abrir un archivo que no existe.

## Manejo de Excepciones

### Estructura Básica

El manejo de excepciones en Python se realiza principalmente mediante los bloques `try`, `except`, `else` y `finally`.

1. Bloque `try`: Aquí se coloca el código que puede generar una excepción.
2. Bloque `except`: Captura y maneja la excepción si ocurre.
3. Bloque `else` (opcional): Se ejecuta si no hay excepciones en el bloque try.
4. Bloque `finally` (opcional): Se ejecuta siempre, independientemente de si ocurrió o no una excepción.

#### Ejemplo de Manejo de Excepciones

```python
try:
    result = 10 / 0  # Esto generará un ZeroDivisionError
except ZeroDivisionError:
    print("No se puede dividir por cero.")
else:
    print(f"El resultado es {result}.")
finally:
    print("Este bloque siempre se ejecuta.")
```

En este ejemplo, si se intenta dividir por cero, el bloque except manejará la excepción y evitará que el programa se detenga.

### Múltiples Excepciones

Es posible manejar múltiples tipos de excepciones usando varias cláusulas `except`:

```python
try:
    x = int(input("Introduce un número: "))
    result = 10 / x
except ValueError:
    print("Eso no es un número válido.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")
```

También puedes capturar múltiples excepciones en una sola cláusula:

```python
try:
    # Código que puede causar múltiples excepciones
    pass
except (ValueError, ZeroDivisionError) as e:
    print(f"Ocurrió un error: {e}")
```

## Lanzar Excepciones

Además de manejar excepciones, también puedes lanzar tus propias excepciones usando la palabra clave raise. Esto es útil para validar condiciones específicas en tu código.

### Ejemplo de Lanzamiento de Excepción

```python
value = -1
if value < 0:
    raise ValueError("El valor no puede ser negativo.")
```


# Argumentos avanzados

## Argumentos Posicionales en Python

### Introducción

En Python, los argumentos posicionales son una forma fundamental de pasar información a las funciones.

### Argumentos Posicionales Básicos

Los argumentos posicionales son aquellos que se pasan a una función en un orden específico, correspondiendo al orden de los parámetros en la definición de la función.

#### Ejemplo:

```python
def saludar(nombre, mensaje):
    print(f"{mensaje}, {nombre}!")

# Llamada con argumentos posicionales
saludar("María", "Hola")  # Salida: Hola, María!

# También se pueden usar como argumentos de palabra clave
saludar(mensaje="Bienvenido", nombre="Juan")  # Salida: Bienvenido, Juan!
```

En este ejemplo, `"María"` y `"Hola"` son argumentos posicionales que corresponden a `nombre` y `mensaje` respectivamente.

### Argumentos Posicionales Obligatorios (Python 3.8+)

Python 3.8 introdujo el concepto de argumentos posicionales obligatorios, que solo pueden ser pasados por posición, no por nombre.

#### Sintaxis:

Se utiliza el símbolo `/` en la definición de la función para indicar que los parámetros antes de él son posicionales obligatorios.

#### Ejemplo:

```python
def multiplicar(a, b, /):
    return a * b

# Uso correcto: argumentos posicionales
print(multiplicar(3, 4))  # Salida: 12

# Esto causará un error
# print(multiplicar(a=3, b=4))  # TypeError
```

### Argumentos de Solo Palabra Clave (Keyword-Only Arguments)

Los argumentos de solo palabra clave son aquellos que deben ser especificados por su nombre al llamar a la función, no pueden ser pasados como argumentos posicionales.

#### Sintaxis:

Se utiliza el símbolo `*` en la definición de la función para indicar que los parámetros después de él son de solo palabra clave.

#### Ejemplo:

```python
def configurar(*, host='localhost', puerto=8080, debug=False):
    print(f"Configuración: host={host}, puerto={puerto}, debug={debug}")

# Uso correcto
configurar(puerto=8000, debug=True)

# Esto causará un error
# configurar('127.0.0.1', 8000, True)  # TypeError
```

#### Ventajas:

1. Mejoran la legibilidad del código al forzar el uso de nombres para parámetros específicos.
2. Evitan errores causados por el orden incorrecto de los argumentos.
3. Permiten tener funciones con muchos parámetros opcionales de manera clara y explícita.

### Combinación de Tipos de Argumentos

Se pueden combinar diferentes tipos de argumentos en una sola función para mayor flexibilidad.

#### Ejemplo:

```python
def funcion_mixta(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

# Uso correcto
funcion_mixta(1, 2, 3, d=4, e=5, f=6)
```

En este ejemplo:
- `a` y `b` son posicionales obligatorios
- `c` y `d` pueden ser posicionales o de palabra clave
- `e` y `f` son solo de palabra clave
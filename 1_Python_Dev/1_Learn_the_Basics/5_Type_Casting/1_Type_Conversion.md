# Python Type Conversion

La conversión de tipos es el proceso de convertir datos de un tipo a otro. Por ejemplo: convertir datos `int` a `str`.

Hay dos tipos de conversión de tipos en Python:

- Conversión implícita: conversión automática de tipos
- Conversión explícita - conversión manual de tipos

## Conversión de tipos implícita en Python

En ciertas situaciones, Python convierte automáticamente un tipo de datos en otro. Esto se conoce como conversión implícita de tipos.

### Ejemplo

```python
integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# mostrar el nuevo valor y el tipo de datos resultante
print("Value:",new_number)
print("Data Type:",type(new_number))
```

__Salida:__

```text
Value: 124.23
Data Type: <class 'float'>
```

En el ejemplo anterior, hemos creado dos variables: `integer_number` y `float_number` de tipo `int` y `float` respectivamente.

Luego sumamos estas dos variables y almacenamos el resultado en `new_number`.

Como podemos ver `new_number` tiene valor 124.23 y es del tipo de datos `float`.

Esto se debe a que Python siempre convierte los tipos de datos más pequeños en tipos de datos más grandes para evitar la pérdida de datos.

> Note:
> - Obtenemos TypeError, si intentamos sumar `str` e `int`. Por ejemplo, `'12' + 23`. Python no es capaz de utilizar la conversión implícita en tales condiciones.

## Conversión explícita de tipos

En la Conversión Explícita de Tipos, los usuarios convierten el tipo de datos de un objeto al tipo de datos requerido.

Utilizamos las funciones incorporadas como `int()`, `float()`, `str()`, etc para realizar la conversión explícita de tipos.

Este tipo de conversión también se denomina typecasting, ya que el usuario convierte (cambia) el tipo de datos de los objetos.

### Ejemplo

```python
num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# conversión explícita de tipos
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))
```

__Salida:__

```text
Data type of num_string before Type Casting: <class 'str'>
Data type of num_string after Type Casting: <class 'int'>
Sum: 35
Data type of num_sum: <class 'int'>
```

En el ejemplo anterior, hemos creado dos variables: `num_string` y `num_integer` con valores de tipo `str` e `int` respectivamente. Fíjate en el código:

```python
num_string = int(num_string)
```

Aquí, hemos utilizado `int()` para realizar la conversión de tipo explícita de `num_string` a tipo entero.

Después de convertir `num_string` en un valor entero, Python es capaz de sumar estas dos variables.

Por último, tenemos el valor `num_sum` es decir 35 y el tipo de datos es `int`.

## Puntos a recordar

- La conversión de tipos es la conversión de un objeto de un tipo de datos a otro tipo de datos.
- La conversión de tipos implícita la realiza automáticamente el intérprete de Python.
- Python evita la pérdida de datos en la conversión implícita de tipos.
- La conversión explícita de tipos también se denomina Type Casting, los tipos de datos de los objetos se convierten utilizando funciones predefinidas por el usuario.
- En Type Casting, puede producirse una pérdida de datos al forzar el objeto a un tipo de datos específico.
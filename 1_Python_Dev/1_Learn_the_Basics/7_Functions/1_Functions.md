# Python Functions

Una función es un bloque de código que sólo se ejecuta cuando se le llama. 

A una función se le pueden pasar datos, conocidos como parámetros. 

Una función puede devolver datos como resultado.

## Crear una funcion

En Python, una función se define mediante la palabra clave `def`:

```python
def my_function():
  print("Hello")
```

## Llamando una funcion

Para llamar a una función, utilice el nombre de la función seguido de un paréntesis:

```python
def my_function():
  print("Hello")

my_function() # Llamada de la funcion
```

## Argumentos

La información puede introducirse en las funciones como argumento.

Los argumentos se especifican después del nombre de la función, dentro de los paréntesis. Puede añadir tantos argumentos como desee, sólo tiene que separarlos con una coma.

El siguiente ejemplo tiene una función con un argumento (fname). Cuando se llama a la función, pasamos un nombre, que se utiliza dentro de la función para imprimir el nombre completo:

```python
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
```

> Los argumentos a menudo se abrevian args en la documentación de Python.

### ¿Parámetros o argumentos?

Los términos parámetro y argumento pueden utilizarse para lo mismo: información que se pasa a una función.

> Desde la perspectiva de una función:
> 
> - Un parámetro es la variable que aparece entre paréntesis en la definición de la función.
> - Un argumento es el valor que se envía a la función cuando es llamada.

### Número de argumentos

Por defecto, una función debe ser llamada con el número correcto de argumentos. Lo que significa que si tu función espera 2 argumentos, tienes que llamar a la función con 2 argumentos, ni más, ni menos.

```python
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
```

Si intentas llamar a la función con 1 o 3 argumentos, obtendrás un error:

```python
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
```

### Argumentos arbitrarios, *args

Si no sabes cuántos argumentos se pasarán a su función, añada un `*` antes del nombre del parámetro en la definición de la función.

De este modo, la función recibirá una tupla de argumentos y podrá acceder a los elementos en consecuencia:

```python
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
```

> Los Argumentos Arbitrarios son a menudo abreviados como `*args` en la documentación de Python.

### Keyword Arguments

También puedes enviar argumentos con la sintaxis clave = valor.

De este modo, el orden de los argumentos no importa.

```python
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
```

> La frase Keyword Arguments a menudo se abrevia como kwargs en las documentaciones de Python.

### Argumentos arbitrarios de palabras clave, **kwargs

Si no sabes cuántos argumentos de palabra clave se pasarán a su función, añade dos asteriscos `**` antes del nombre del parámetro en la definición de la función.

De este modo, la función recibirá un diccionario de argumentos y podrá acceder a los elementos correspondientes:

```python
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
```

> Los Argumentos Kword Arbitrarios son a menudo abreviados como **kwargs en las documentaciones de Python.

## Default Parameter Value

Un valor de parámetro por defecto es un valor que se asigna automáticamente a un parámetro de una función si no se proporciona un argumento para ese parámetro al llamar a la función.

### Sintaxis

Se define usando el operador de asignación (=) en la declaración de la función:

```python
def funcion(parametro=valor_por_defecto):
```

### Funcionamiento:

Si se llama a la función sin proporcionar un valor para el parámetro, se usa el valor por defecto.

Si se proporciona un valor, este sobrescribe el valor por defecto.

```python
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
```

## Pasar una lista como argumento

Puedes enviar cualquier tipo de dato de argumento a una función (cadena, número, lista, diccionario, etc.), y será tratado como el mismo tipo de dato dentro de la función.

Por ejemplo, si envías una lista como argumento, seguirá siendo una lista cuando llegue a la función:

```python
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
```

## Retornar valores

Para que una función devuelva un valor, utilice la sentencia `return`:

```python
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
```

## Pass

las definiciones de función no pueden estar vacías, pero si por alguna razón tienes una definición de función sin contenido, pon la sentencia pass para evitar obtener un error.

```python
def myfunction():
  pass
```


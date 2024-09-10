# Conceptos de Python para el Backend

## ¿Qué son los decoradores?

Son un patrón de diseño en Python que permite agregar funcionalidades a un objeto existente (funciones) sin modificar su estructura.

```python
#@example_decorator
def test_function():
    return "output"
```

### Cómo trabajan las funciones

Las funciones son muy importantes en Python y estas retornan un valor de acuerdo a los argumentos que les pasamos:

```python
def plus_one(number):
    return number + 1
print(plus_one(8))
```

### Asignando funciones a variables

```python
def plus_one(number):
    return number + 1

add_one = plus_one
print(add_one(5))
```

### Definiendo funciones dentro de otras funciones

```python
def plus_one(number):
    def add_one(number):
        print("Executing add_one")
        return number + 1

    print("Executing plus_one")
    result = add_one(number)
    return result

print(plus_one(4))
```

### Pasando funciones como argumentos de otras funciones

```python
def plus_one(number):
    print("Executing plus_one")
    return number + 1

def function_call(function):
    print("Executing function_call")
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)
```

### Funciones retornando otras funciones

```python
def hello_function():
    def say_hi():
        print("Executing say_hi")
        return "Hi"
    print("Executing hello_function")
    return say_hi

hello = hello_function()
hello()
```

### Las funciones anidadas tienen acceso al las variables de la función envolvente

```python
def print_message(message):
    """Enclosing Function"""

    def message_sender():
        """Nested Function"""

        print(message)

    message_sender()

print_message("Some random message")
```

## Creando decoradores

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
say_whee()
```

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
    
say_whee()
```

### Aplicando multiples decoradores a una misma función

```python
def uppercase_decorator(function):
    print("Applying uppercase decorator")
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def split_string(function):
    print("Applying split decorator")
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()
```

### Decorando funciones con argumentos

```python
def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print(f"My arguments are: {arg1}, {arg2}")
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print(f"Cities I love are {city_one} and {city_two}")

cities("Pereira", "Medellín")
```

### Definiendo decoradores de propósito general

```python
def test_args_and_kwargs(*args, **kwargs):
    print("Showing *args:")
    for arg in args:
        print("Arguments of *args:", arg)
    print("Showing **kwargs:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

args = (1, 2, "Hola")
kwargs = {"first_name": "Carolina", "last_name": "Gomez"}
test_args_and_kwargs(args, **kwargs)
```

```python
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

function_with_arguments(1,2,3)
```

```python
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments(first_name="", last_name="", country="Colombia"):
    print(f"This has shown keyword arguments: ")
    print(f"first_name: {first_name}")
    print(f"last_name: {last_name}")
    print(f"country: {country}")

function_with_keyword_arguments(first_name="Derrick", last_name="Mwiti")
```


### Pasando argumentos al decorador

```python
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3) :
            """This is the wrapper function"""
            
            print(f"The wrapper can access all the variables\n"
                  f"\t- from the decorator maker: {decorator_arg1} {decorator_arg2} {decorator_arg3}\n"
                  f"\t- from the function call: {function_arg1} {function_arg2} {function_arg3}\n"
                  f"and pass them to the decorated function")
            return func(function_arg1, function_arg2, function_arg3)

        return wrapper

    return decorator

pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2, function_arg3):
    print("This is the decorated function and it only knows about its arguments: ")
    print(f"{function_arg1} {function_arg2} {function_arg3}")

decorated_function_with_arguments(pandas, "Science", "Tools")
```

### Debugueando decoradores

```python
# decorator
def make_geek_happy(func):
    def wrapper():
        neutral_message = func()
        happy_message = neutral_message + " You are happy!"
        return happy_message
    return wrapper
  
def speak():
    """Returns a neutral message"""
    return "Hi!"
  
  
# wrapping the function in the decorator
# and assigning it to positive_message
positive_message = make_geek_happy(speak)
  
print(positive_message())
  
print(f"Function name: {speak.__name__}") 
print(f"Function doc: {speak.__doc__}") 
print(f"Function name with decorator: {positive_message.__name__}")
print(f"Function doc with decorator: {positive_message.__doc__}")
```

```python
# importing the module
import functools
  
# decorator
def make_geek_happy(func):
    @functools.wraps(func)
    def wrapper():
        neutral_message = func()
        happy_message = neutral_message + " You are happy!"
        return happy_message
    return wrapper
  
def speak():
    """Returns a neutral message"""
    return "Hi!"
  
positive_message = make_geek_happy(speak)
print(positive_message())
  
print(f"Function name: {speak.__name__}") 
print(f"Function doc: {speak.__doc__}") 
print(f"Function name with decorator: {positive_message.__name__}")
print(f"Function doc with decorator: {positive_message.__doc__}")
```

## Funciones Lambda

Son también conocidas como funciones anónimas y son funciones que pueden definir cualquier número de parámetros pero una única expresión. Esta expresión es evaluada y devuelta.

```python
cuadrado = lambda x: x ** 2

print(cuadrado(4))
```

### Uso apropiado de las funciones lambda

#### `map()`
La función map() en Python aplica una función a cada uno de los elementos de una lista.

```python
enteros = [1, 2, 4, 7]
cuadrados = []
for e in enteros:
    cuadrados.append(e ** 2)
     
print(cuadrados)
```

```python
enteros = [1, 2, 4, 7]
cuadrados = list(map(lambda x : x ** 2, enteros))
print(cuadrados)
```

#### `filter()`

La función filter() filtra una lista de elementos para los que una función devuelve True.

```python
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = []
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
print("Pares-> ", pares)
```

```python
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(lambda x : x % 2 == 0, valores))
print("Pares-> ", pares)
```

#### `reduce()`

Esta función se utiliza principalmente para llevar a cabo un cálculo acumulativo sobre una lista de valores y devolver el resultado.

```python
valores = [2, 4, 6, 5, 4]
suma = 0
for el in valores:
    suma += el
print(suma)
```

```python
valores = [2, 4, 6, 5, 4]
from functools import reduce
suma = reduce(lambda x, y: x + y, valores)
print(suma)
```

#### `sorted()`

Esta función ordena una lista en forma lexicográfica.

```python
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
print(sorted(ids)) # Lexicographic sort
```

```python
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
sorted_ids = sorted(ids, key=lambda x: int(x[2:])) # Integer sort
print(sorted_ids)
```

## Properties

Las properties son la forma pythonica de evitar la creación de métodos para obtener y modificar atributos de una clase. Esta función nos ayuda a convertir atributos de una clase en properties o managed attributes.

```python
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value


point = Point(5, 9)

point.get_x()
point.set_x(8)
point.get_x()
point._x
```

### Creando properties con la inicialización de la función `property()`

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )

circle = Circle(42.0)
circle.radius

circle.radius = 50
circle.radius

del circle.radius
```

### Usando `property()` como decorador

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property."""
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Set radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius

circle = Circle(42.0)
circle.radius
circle.radius = 50
circle.radius


del circle.radius
circle.radius
```

#### Creando atributos de solo lectura

```python
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

point = Point(12, 5)
point.x
point.y
point.x = 10
```

#### Creando atributos de solo escritura

```python
import hashlib
import os

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @property
    def password(self):
        raise AttributeError("Password is write-only")

    @password.setter
    def password(self, plaintext):
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac(
            "sha256", plaintext.encode("utf-8"), salt, 100_000
        )

user = User("Carolina", "secure_password")
user.password

user.password = "another_Secure_password"
```

### Algunos casos de uso de las `properties()`

#### 1. Validando atributos

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"x" must be a number') from None

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        try:
            self._y = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"y" must be a number') from None

point = Point(2, 5)
point.x = "hola"
```

#### 2. Para agregar atributos que requieren algún calculo

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

rectangle = Rectangle(30, 50)
rectangle.area
```

## Métodos de instancia, métodos de clase y métodos estáticos

Los **métodos de instancia** son creados para modificar un objeto instanciado de una clase.

Los **métodos de clase** trabajan directamente con la clase, desde que su parámetro es la clase en sí.

Los **métodos estáticos** no saben nada acerca de la clase, solo trabajan con los parámetros recibidos.

```python
class MyClass:
    def method(self):
        """ Instance method """
        return 'instance method called', self

    @classmethod
    def class_method(cls):
        """ Class method """
        return 'class method called', cls

    @staticmethod
    def static_method():
        """ Static method """
        return 'static method called'

obj = MyClass()
obj.method()
MyClass.method(obj)
obj.class_method()
obj.static_method()
```

### ¿Qué pasa si accedemos a los metodos sin instanciar un objeto de la clase?

```python
class MyClass:
    def method(self):
        """ Instance method """
        return 'instance method called', self

    @classmethod
    def class_method(cls):
        """ Class method """
        return 'class method called', cls

    @staticmethod
    def static_method():
        """ Static method """
        return 'static method called'

MyClass.class_method()
MyClass.static_method()
MyClass.method()
```

### Ejemplos de uso

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'

margherita = Pizza(['mozzarella', 'tomatoes'])
cheese = Pizza(['mozzarella', 'provolone', 'cheddar', 'Parmesan'])

print(margherita)
print(cheese)
```

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'
    
    def create_custom_pizza(self, ingredients):
        self.ingredients = ingredients
        return self

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def cheese(cls):
        return cls(['mozzarella', 'provolone', 'cheddar', 'Parmesan'])

Pizza.margherita()
Pizza.cheese()

first_pizza = Pizza([])
first_pizza.ingredients
first_pizza.create_custom_pizza(['chicken', 'mozzarella'])

# Podemos mostrar los metodos de clase asociados a la clase Pizza sin cambiar el comportamiento de la instancia
first_pizza.margherita()

first_pizza.ingredients
```

```python
# Usando metodos estáticos
import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius}, '
                f'{self.ingredients})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

p = Pizza(4, ['mozzarella', 'tomatoes'])
p.area()

Pizza.circle_area(4)
Pizza.circle_area(5)
p.area()
```
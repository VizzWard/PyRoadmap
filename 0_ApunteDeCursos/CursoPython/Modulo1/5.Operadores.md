# Operadores

Los operadores en programación son símbolos o palabras clave que indican a un lenguaje de programación que realice una operación específica sobre uno o más operandos (valores o variables). Los operadores permiten realizar cálculos, comparaciones, y manipular datos de diversas maneras.

## Principales tipos de operadores en Python:

1. Operadores aritméticos: Realizan operaciones matemáticas.

    - `+` (suma), `-` (resta), `*` (multiplicación), `/` (división), `%` (módulo), `**` (exponenciación).

2. Operadores de comparación (relacionales): Comparan dos valores y devuelven un valor booleano (True o False).
3. Operadores lógicos: Combina expresiones booleanas.
4. Operadores de asignación: Asignan un valor a una variable.

    - `=` (asignación), `+=` (suma y asigna), `-=` (resta y asigna).

5. Operadores de identidad: Verifican si dos objetos son idénticos (mismo objeto en la memoria).

    - `is`, `is not`.

6. Operadores de pertenencia: Verifican si un valor está presente en una secuencia (como una lista, tupla, etc.).

    - `in`, `not in`.

7. Operadores bit a bit: Realizan operaciones a nivel de bits.

    - `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (desplazamiento a la izquierda), `>>` (desplazamiento a la derecha).

## Operadores relacionales

Los operadores relacionales son utilizados para comparar dos valores. Estos operadores devuelven un valor booleano (True o False) basado en la relación entre los valores que se comparan. Los operadores relacionales en Python son los siguientes:

1. Mayor que (>): Devuelve True si el operando de la izquierda es mayor que el operando de la derecha.

```python
5 > 3  # True
```

2. Menor que (<): Devuelve True si el operando de la izquierda es menor que el operando de la derecha.

```python
5 < 3  # False
```

3. Mayor o igual que (>=): Devuelve True si el operando de la izquierda es mayor o igual que el operando de la derecha.

```python
5 >= 3  # True
5 >= 5  # True
```

4. Menor o igual que (<=): Devuelve True si el operando de la izquierda es menor o igual que el operando de la derecha.

```python
5 <= 3  # False
5 <= 5  # True
```

5. Igual a (==): Devuelve True si ambos operandos son iguales.

```python
5 == 5  # True
5 == 3  # False
```

6. Distinto de (!=): Devuelve True si ambos operandos son diferentes.

```python
5 != 3  # True
5 != 5  # False
```

## Operadores Logicos

Los operadores lógicos se utilizan para combinar o invertir expresiones booleanas (es decir, expresiones que resultan en True o False). Los operadores lógicos permiten tomar decisiones más complejas en función de múltiples condiciones.

1. `and`: Devuelve `True` si ambas expresiones son `True`. Si alguna de las expresiones es `False`, devuelve `False`.

```python
x = 5
y = 10
resultado = (x > 3) and (y < 15)  # True porque ambas condiciones son True
```

2. `or`: Devuelve `True` si al menos una de las expresiones es `True`. Si ambas expresiones son `False`, devuelve `False`.

```python
x = 5
y = 10
resultado = (x > 3) or (y > 15)  # True porque al menos una condición es True
```

3. `not`: Invierte el valor lógico de la expresión. Si la expresión es `True`, not la convierte en `False`, y viceversa.

```python
x = 5
resultado = not (x > 3)  # False porque x > 3 es True, y not True es False
```
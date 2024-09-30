# Condicionales

Las condicionales son estructuras de control de flujo que permiten a un programa tomar decisiones basadas en ciertas condiciones. En Python, las principales estructuras condicionales son `if`, `elif` (else if) y `else`.

## if

El if se usa para ejecutar un bloque de código si una condición es verdadera.

Ejemplo:

```python
temperatura = 30

if temperatura > 25:
    print("Hace calor hoy")

# Si la temperatura es mayor que 25, imprimirá: "Hace calor hoy"
```

## elif (else if)

elif se usa para comprobar múltiples condiciones después de un if. Se ejecuta si las condiciones anteriores son falsas y su propia condición es verdadera.

Ejemplo:

```python
puntuacion = 75

if puntuacion >= 90:
    print("A")
elif puntuacion >= 80:
    print("B")
elif puntuacion >= 70:
    print("C")
elif puntuacion >= 60:
    print("D")

# Imprimirá: "C"
```

## else

else se ejecuta cuando ninguna de las condiciones anteriores (if o elif) es verdadera.

Ejemplo:

```python
edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Imprimirá: "Eres menor de edad"
```

## Operadores de comparación

Los operadores de comparación se usan para comparar valores:

- `==`: igual a.
- `!=`: diferente de.
- `>`: mayor que.
- `<`: menor que.
- `>=`: mayor o igual que.
- `<=`: menor o igual que.

Ejemplo:

```python
x = 5
y = 10

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= 5)  # True
print(y <= 10) # True
```

## Operadores lógicos

Los operadores lógicos se usan para combinar condiciones:

- `and`: Verdadero si ambas condiciones son verdaderas
- `or`: Verdadero si al menos una condición es verdadera
- `not`: Invierte el resultado, Verdadero si la condición es Falsa y viceversa

Ejemplo:


```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
print(not b)    # True
```
# Condicionales

Las condicionales son estructuras de control de flujo que permiten tomar decisiones en función de si una condición es verdadera (`True`) o falsa (`False`). Estas estructuras te permiten ejecutar bloques de código específicos solo cuando se cumplen ciertas condiciones.

## Principales Condicionales

1. `if`: Evalúa una condición. Si la condición es `True`, se ejecuta el bloque de código asociado.
2. `elif` (else if): Se utiliza para verificar múltiples condiciones. Si la condición del `if` no se cumple y la condición del elif es `True`, se ejecuta el bloque de código asociado al `elif`.
3. `else`: Se ejecuta si ninguna de las condiciones anteriores (`if` y `elif`) se cumple. No requiere condición, ya que actúa como un "de lo contrario".

## Estructura Básica

```python
if condicion:
    # Bloque de código si la condición es verdadera
elif otra_condicion:
    # Bloque de código si la segunda condición es verdadera
else:
    # Bloque de código si ninguna de las condiciones anteriores es verdadera
```

### Ejemplos

#### Ejemplo 1

Condicional Simple con `if`

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
```

#### Ejemplo 2

Condicional con `if`, `elif`, y `else`.
 
```python
edad = 16

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres un adolescente")
else:
    print("Eres un niño")
```
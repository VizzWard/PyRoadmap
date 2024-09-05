# Ciclos o Loops

Los ciclos o loops son estructuras de control de flujo que permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición o para un número determinado de veces. Los loops son útiles para automatizar tareas repetitivas y recorrer estructuras de datos como listas, tuplas, diccionarios, entre otras.

## Tipos de Loops

1. `for` loop: Se utiliza para iterar sobre una secuencia (como una lista, tupla, cadena, o rango) y ejecutar un bloque de código para cada elemento de esa secuencia.
2. `while` loop: Se utiliza para repetir un bloque de código mientras una condición específica sea verdadera (True). Cuando la condición deja de ser verdadera, el loop se detiene.

### for Loop

El `for` loop en Python se utiliza principalmente para iterar sobre los elementos de una secuencia. Cada iteración del loop asigna el siguiente elemento de la secuencia a una variable y luego ejecuta el bloque de código dentro del loop.

```python
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)
```

En este ejemplo, el loop for itera sobre la lista frutas y, en cada iteración, imprime el elemento actual de la lista. El resultado será:

```text
manzana
banana
cereza
```

También puedes usar el `for` loop junto con la función `range()` para iterar un número específico de veces.

```python
for i in range(5):
    print(i)
```

Este loop imprimirá los números del 0 al 4.

### while Loop

El while loop en Python ejecuta un bloque de código mientras una condición dada sea verdadera. Si la condición es falsa desde el principio, el loop no se ejecutará.

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

En este ejemplo, el `while` loop seguirá ejecutándose mientras `contador` sea menor que 5. En cada iteración, se imprime el valor de `contador` y luego se incrementa en 1. El resultado será:

```text
0
1
2
3
4
```

## Palabras clave especiales en Loops

1. `break`: Termina el loop prematuramente, incluso si la condición no se ha cumplido. Útil para salir de un loop cuando se ha cumplido una condición especial.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Este loop imprimirá los números del 0 al 4 y luego se detendrá debido a la condición `i == 5`.

2. `continue`: Omite el resto del código en la iteración actual y continúa con la siguiente iteración del loop.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Este loop imprimirá los números 0, 1, 3, y 4. La iteración donde `i == 2` es omitida.

3. `else` en loops: Puedes usar la palabra clave `else` con loops para ejecutar un bloque de código cuando el loop termina normalmente (es decir, sin haber usado `break`).

```python
for i in range(5):
    print(i)
else:
    print("El loop ha terminado")
```

Este loop imprimirá los números del 0 al 4, y luego imprimirá "El loop ha terminado".
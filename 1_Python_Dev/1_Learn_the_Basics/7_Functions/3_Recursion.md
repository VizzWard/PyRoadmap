# Recursión en Python

## ¿Qué es la Recursión?

La recursión es una técnica de programación donde una función se llama a sí misma para resolver un problema. Es como resolver un gran problema dividiéndolo en versiones más pequeñas del mismo problema.

## Conceptos Clave de la Recursión

1. **Caso Base**: Es la condición que detiene la recursión. Sin esto, la función se llamaría a sí misma indefinidamente.
2. **Caso Recursivo**: Es donde la función se llama a sí misma, generalmente con un problema más pequeño.

## Ejemplo Simple: Factorial

Veamos un ejemplo sencillo para entender la recursión: el cálculo del factorial de un número.

```python
def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:  # Caso recursivo
        return n * factorial(n - 1)

print(factorial(5))  # Salida: 120
```

Explicación:
- El caso base es cuando `n` es 0 o 1, donde sabemos que el factorial es 1.
- En otros casos, multiplicamos `n` por el factorial de `n - 1`.

## Ventajas y Precauciones

### Ventajas:
- Puede hacer que el código sea más limpio y elegante para ciertos problemas.
- Es útil para tareas que tienen una naturaleza recursiva (como recorrer estructuras de árbol).

### Precauciones:
- Puede consumir mucha memoria si la recursión es muy profunda.
- Si no se maneja correctamente, puede llevar a un bucle infinito.
- A veces, una solución iterativa (con bucles) puede ser más eficiente.

## Ejemplo Avanzado: Suma Triangular

Analicemos el ejemplo proporcionado de `tri_recursion`:

```python
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\nRecursion Example Results")
tri_recursion(6)
```

Explicación paso a paso:
1. La función `tri_recursion(k)` suma todos los números desde `k` hasta 1.
2. Caso base: Cuando `k` es 0 o negativo, retorna 0.
3. Caso recursivo: Suma `k` al resultado de `tri_recursion(k - 1)`.
4. La función se llama con `k = 6`.
5. Salida:
```text
1
3
6
10
15
21
```

- Cada número es la suma de sí mismo y todos los números anteriores.
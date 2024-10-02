# Loops

Los bucles en Python son estructuras de control que permiten ejecutar un bloque de código repetidamente.

## while

Un bucle while se utiliza para ejecutar un bloque de sentencias repetidamente hasta que se cumpla una condición dada.

Cuando la condición se convierte en falsa, se ejecuta la línea inmediatamente posterior al bucle en el programa.

```python
count = 0
while (count < 3):
    count = count + 1
    print("Hello")
```

### Uso de la sentencia else con el bucle while

La cláusula else sólo se ejecuta cuando la condición while se convierte en falsa. Si se sale del bucle, o si se produce una excepción, no se ejecutará.

```python
count = 0
while (count < 3):
    count = count + 1
    print("Hello")
else:
    print("In Else Block")
```

### while infinito

Si queremos que un bloque de código se ejecute infinitas veces, podemos utilizar el bucle while para hacerlo.

```python
while True:
    print("Hello")
```

>  Se sugiere no utilizar este tipo de bucle ya que es un bucle infinito sin fin donde la condición es siempre verdadera y hay que terminar forzosamente el compilador.

## for

Los bucles For se utilizan para recorrer secuencias. Por ejemplo: recorrer una lista, una cadena, un array, etc.

```python
n = 4
for i in range(0, n):
    print(i)
```

- El código utiliza un bucle for de Python que itera sobre los valores de 0 a 3 (sin incluir 4), tal y como especifica la construcción range(0, n). Imprimirá los valores de 'i' en cada iteración del bucle.

### Iterar por el índice de secuencias

También podemos utilizar el índice de los elementos de la secuencia para iterar. La idea clave es calcular primero la longitud de la lista e iterar sobre la secuencia dentro del rango de esta longitud.

```python
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])
```

### Uso de la sentencia else con for

También podemos combinar la sentencia else con el bucle for como en el bucle while. Pero como no hay ninguna condición en el bucle for en base a la cual la ejecución terminará, el bloque else se ejecutará inmediatamente después de que el bloque for termine su ejecución.

```python
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])
else:
    print("Inside Else Block")
```

## Bucles anidados

Podemos usar bucles dentro de otros bucles, a esto se le conoce como bucle anidado.

> Podemos poner cualquier tipo de bucle dentro de cualquier otro tipo de bucles

```python
for i in range(1, 5):
    for j in range(i):
        print(i)
    print()
```

## Declaraciones de control de bucle

Las sentencias de control en los bucles de Python (como `break` y `continue`) te permiten alterar el flujo normal de un bucle. Estas sentencias te dan el poder de decidir cuándo quieres saltar una parte del bucle o salir de él por completo, en lugar de simplemente dejar que se ejecute de principio a fin.

Además, Python es inteligente en cuanto a la gestión de la memoria. Cuando un bucle o una función termina, Python automáticamente limpia y libera la memoria que estaban usando las variables creadas dentro de ese bucle o función. Esto te ahorra tener que preocuparte por limpiar manualmente la memoria que ya no necesitas.

### Continue

El `continue` se usa para saltar el resto del código dentro de un bucle para la iteración actual y pasar a la siguiente iteración.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)

# Salida:
# 0
# 1
# 3
# 4
```

- En este ejemplo, cuando `i` es 2, el `continue` hace que se salte esa iteración y no se imprima el 2.

### Break

El `break` se usa para salir completamente del bucle, independientemente de la condición del bucle.

```python
for i in range(5):
    if i == 3:
        break
    print(i)

print("Bucle terminado")

# Salida:
# 0
# 1
# 2
# Bucle terminado
```

- En este ejemplo, cuando `i` llega a 3, el `break` hace que salgamos completamente del bucle, por lo que no se imprimen ni el 3 ni el 4.

### Pass

El `pass` es una operación nula en Python. Esencialmente, no hace nada. Puede parecer extraño tener una instrucción que no hace nada, pero en realidad es bastante útil en ciertas situaciones.

Usos comunes de pass:

1. En funciones o clases que aún no tienen implementación:

```python
def funcion_por_implementar():
    pass

class ClasePorImplementar:
    pass
```

2. En bloques condicionales o bucles donde temporalmente no quieres hacer nada:

```python
for i in range(5):
    if i == 2:
        pass  # No hacemos nada especial cuando i es 2
    else:
        print(i)
```

3. Como marcador de posición en estructuras que requieren contenido:

```python
while True:
    if condicion:
        break
    elif otra_condicion:
        pass  # Haremos algo aquí más tarde
    else:
        continue
```
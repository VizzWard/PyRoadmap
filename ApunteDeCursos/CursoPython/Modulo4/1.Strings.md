# Strings

Un string (o cadena de caracteres) es una secuencia inmutable de caracteres, que se utiliza para representar texto. Los strings se pueden definir utilizando comillas simples ('...'), comillas dobles ("..."), o comillas triples ('''...''' o """...""") para cadenas de múltiples líneas.

## Características

- Inmutables: Una vez que un string es creado, no puede ser modificado. Cualquier operación que parezca modificar un string, en realidad, crea un nuevo string.
- Indexación: Puedes acceder a caracteres individuales dentro de un string usando índices, comenzando desde 0.
- Slicing: Puedes extraer una subcadena utilizando el operador de slicing (`[inicio:fin]`)

## Ejemplo básicos

```python
mi_string = "Hola, Mundo!"
print(mi_string[0])  # Imprime: 'H'
print(mi_string[-1])  # Imprime: '!'
print(mi_string[0:4])  # Imprime: 'Hola'
```

## Métodos más utilizados

Python proporciona una amplia gama de métodos integrados para trabajar con strings. A continuación, se describen algunos de los más comunes:

### len()

Retorna la longitud del string (número de caracteres).

```python
longitud = len("Hola, Mundo!")
print(longitud)  # Imprime: 12
```

### upper()

Convierte todos los caracteres de un string a mayúsculas.

```python
mayusculas = "hola".upper()
print(mayusculas)  # Imprime: 'HOLA'
```

### lower()

Convierte todos los caracteres de un string a minúsculas.

```python
minusculas = "HOLA".lower()
print(minusculas)  # Imprime: 'hola'
```

### strip()

Elimina los espacios en blanco al inicio y al final del string (también puede eliminar otros caracteres específicos si se le pasa un argumento).

```python
limpio = "  Hola, Mundo!  ".strip()
print(limpio)  # Imprime: 'Hola, Mundo!'
```

### replace(old, new)

Reemplaza todas las apariciones de un substring por otro.

```python
reemplazado = "Hola, Mundo!".replace("Mundo", "Python")
print(reemplazado)  # Imprime: 'Hola, Python!'
```

### split(delimiter)

Divide un string en una lista de substrings, utilizando un delimitador.

```python
partes = "uno,dos,tres".split(",")
print(partes)  # Imprime: ['uno', 'dos', 'tres']
```

### join(iterable)

Une una secuencia de strings en un solo string, utilizando el string actual como delimitador.

```python
unido = "-".join(["uno", "dos", "tres"])
print(unido)  # Imprime: 'uno-dos-tres'
```

### find(substring)

Retorna el índice de la primera aparición de un substring en el string, o -1 si no se encuentra.

```python
indice = "Hola, Mundo!".find("Mundo")
print(indice)  # Imprime: 6
```

### startswith(prefix) y endswith(suffix)

Verifican si un string comienza o termina con un substring específico.

```python
empieza_con = "Hola, Mundo!".startswith("Hola")
termina_con = "Hola, Mundo!".endswith("Mundo!")
print(empieza_con)  # Imprime: True
print(termina_con)  # Imprime: True
```

### count(substring)

Cuenta cuántas veces aparece un substring dentro del string.

```python
veces = "Hola, Hola, Hola!".count("Hola")
print(veces)  # Imprime: 3
```

Los strings en Python son una parte fundamental del lenguaje, utilizados para representar y manipular texto. Gracias a su inmutabilidad y a los numerosos métodos que ofrecen, son muy poderosos y flexibles para todo tipo de operaciones con texto. Estos métodos permiten desde operaciones simples, como cambiar la capitalización, hasta tareas más complejas, como búsqueda y manipulación de substrings.
# Basic Syntax

La sintaxis de Python define un conjunto de reglas que se utilizan para crear un Programa Python.

## First Python Program

Vamos a ejecutar un programa Python para imprimir "¡Hola, Mundo!" en dos modos diferentes de Programación Python. (a) Programación en Modo Interactivo (b) Programación en Modo Script.

### Python - Interactive Mode Programming

Podemos invocar un intérprete de Python desde la línea de comandos escribiendo python en el símbolo del sistema de la siguiente manera

```text
$ python3
Python 3.10.6 (main, Mar 10 2023, 10:55:28) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Aquí `>>>` denota un prompt de comandos Python donde puedes escribir tus comandos. Escribamos el siguiente texto en el prompt de Python y pulsemos Enter:

```text
>>> print ("Hello, World!")
```

Si estás ejecutando una versión antigua de Python, como Python 2.4.x, entonces necesitarías usar la sentencia print sin paréntesis como en print "¡Hola, Mundo!". Sin embargo en Python versión 3.x, esto produce el siguiente resultado:

```text
Hello, World!
```

### Python - Script Mode Programming

Podemos invocar al intérprete de Python con un parámetro de script que inicia la ejecución del script y continúa hasta que éste finaliza. Cuando el script finaliza, el intérprete deja de estar activo.

Escribamos un simple programa Python en un script que es un simple archivo de texto. Los archivos Python tienen extensión .py. Escriba el siguiente código fuente en un archivo test.py:

```text
print ("Hello, World!")
```

Asumimos que tienes la ruta del intérprete de Python en la variable PATH. Ahora, vamos a tratar de ejecutar este programa de la siguiente manera:

```text
$ python3 test.py
```

Esto produce el siguiente resultado:

```text
Hello, World!
```

## Python Identifiers

Un identificador Python es un nombre usado para identificar una variable, función, clase, módulo u otro objeto. Un identificador comienza con una letra de la A a la Z o de la a a la z o un guión bajo (_) seguido de cero o más letras, guiones bajos y dígitos (0 a 9).

Python no permite caracteres de puntuación como @, $ y % dentro de los identificadores.

> Python es un lenguaje de programación que distingue entre mayúsculas y minúsculas. Por lo tanto, `Manpower` y `manpower` son dos identificadores diferentes en Python.

Estas son las convenciones de nomenclatura para los identificadores de Python:

- Los nombres de clases de Python comienzan con una letra mayúscula. Todos los demás identificadores comienzan con una letra minúscula.
- Comenzar un identificador con un guión bajo inicial indica que se trata de un identificador privado.
- Comenzar un identificador con dos guiones bajos indica que se trata de un identificador muy privado.
- Si el identificador también termina con dos guiones bajos, el identificador es un nombre especial definido por el lenguaje.

## Python Reserved Words

La siguiente lista muestra las palabras clave de Python. Son palabras reservadas y no puedes usarlas como nombres de constantes o variables o cualquier otro identificador. Todas las palabras clave de Python contienen sólo letras minúsculas.

| and   | as      | assert   |
|-------|---------|----------|
| break | class   | continue |
| def   | del     | elif     |
| else  | except  | False    |
| finally | for   | from     |
| global | if     | import   |
| in    | is      | lambda   |
| None  | nonlocal | not     |
| or    | pass    | raise    |
| return | True   | try      |
| while | with    | yield    |

## Python Lines and Indentation

La programación en Python no proporciona llaves para indicar bloques de código para definiciones de clases y funciones o control de flujo. Los bloques de código se indican mediante la sangría de línea, que se aplica rígidamente.

El número de espacios en la sangría es variable, pero todas las sentencias del bloque deben tener la misma sangría. Por ejemplo:

```python
if True:
   print ("True")
else:
   print ("False")
```

Sin embargo, el siguiente bloque genera un error:

```python
if True:
   print ("Answer")
   print ("True")
else:
   print ("Answer")
   print ("False")
```

Así, en Python todas las líneas continuas sangradas con el mismo número de espacios formarían un bloque. El siguiente ejemplo tiene varios bloques de sentencias:

> No intentes entender la lógica en este momento. Solo de que has entendido la identacion de varios bloques, incluso si están sin llaves.

```python
import sys

try:
   # open file stream
   file = open(file_name, "w")
except IOError:
   print "There was an error writing to", file_name
   sys.exit()
   
print "Enter '", file_finish,
print "' When finished"

while file_text != file_finish:
   file_text = raw_input("Enter text: ")
   if file_text == file_finish:
      # close the file
      file.close
      break
       
   file.write(file_text)
   file.write("\n")
   
file.close()
file_name = raw_input("Enter filename: ")

if len(file_name) == 0:
   print "Next time please enter something"
   sys.exit()
   
try:
   file = open(file_name, "r")
except IOError:
   print "There was an error reading file"
   sys.exit()
   
file_text = file.read()
file.close()
print file_text
```

## Python Multi-Line Statements

Las sentencias en Python normalmente terminan con una nueva línea. Sin embargo, Python permite el uso del carácter de continuación de línea (\) para indicar que la línea debe continuar. Por ejemplo:

```text
total = item_one + \
        item_two + \
        item_three
```

Las sentencias contenidas entre corchetes [], {} o () no necesitan utilizar el carácter de continuación de línea. Por ejemplo, la siguiente sentencia funciona bien en Python:

```python
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
```

## Quotations in Python

Python acepta comillas simples ('), dobles (") y triples (''' o """) para denotar literales de cadena, siempre que el mismo tipo de comillas comience y termine la cadena.

Las comillas triples se utilizan para que la cadena abarque varias líneas. Por ejemplo:

```python
word = 'word'
print (word)

sentence = "This is a sentence."
print (sentence)

paragraph = """This is a paragraph. It is
 made up of multiple lines and sentences."""
print (paragraph)
```

## Comments in Python

Un comentario es una explicación o anotación legible por el programador en el código fuente de Python. Se añaden con el propósito de hacer el código fuente más fácil de entender para los humanos, y son ignorados por el intérprete de Python.

Al igual que la mayoría de los lenguajes modernos, Python admite comentarios de una línea (o de fin de línea) y de varias líneas (bloque).

Un signo de almohadilla (#) que no esté dentro de una cadena literal inicia un comentario. Todos los caracteres después de # y hasta el final de la línea física forman parte del comentario y el intérprete de Python los ignora.

```python
# First comment
print ("Hello, World!") # Second comment
```

Puede escribir un comentario en la misma línea después de una sentencia o expresión

```python
name = "Madisetti" # This is again comment
```

Puede comentar varias líneas de la siguiente manera:

```python
# This is a comment.
# This is a comment, too.
# This is a comment, too.
# I said that already.
```

La siguiente cadena entre comillas triples también es ignorada por el intérprete de Python y puede utilizarse como comentario multilínea:

```python
'''
This is a multiline
comment.
'''
```

## Uso de líneas en blanco en programas Python

Una línea que sólo contiene espacios en blanco, posiblemente con un comentario, se conoce como línea en blanco y Python la ignora totalmente.

En una sesión de intérprete interactiva, debe introducir una línea física vacía para terminar una sentencia multilínea.

## A la espera del usuario

La siguiente línea del programa muestra el prompt, la sentencia que dice "Pulse la tecla intro para salir", y espera a que el usuario actúe:

```python
#!/usr/bin/python

raw_input("\n\nPress the enter key to exit.")
```

Aquí, "\n\n" se utiliza para crear dos nuevas líneas antes de mostrar la línea real. Una vez que el usuario pulsa la tecla, el programa termina. Este es un buen truco para mantener una ventana de consola abierta hasta que el usuario haya terminado con una aplicación.

## Varias declaraciones en una sola línea

El punto y coma ( ; ) permite incluir varias sentencias en una misma línea, siempre que ninguna de ellas inicie un nuevo bloque de código. A continuación se muestra un ejemplo de uso del punto y coma:

```python
import sys; x = 'foo'; sys.stdout.write(x + '\n')
```

## Grupos de declaraciones múltiples como suites

Un grupo de sentencias individuales, que forman un único bloque de código se denominan suites en Python. Las sentencias compuestas o complejas, como if, while, def y class requieren una línea de cabecera y una suite.

Las líneas de encabezado comienzan la sentencia (con la palabra clave) y terminan con dos puntos ( : ) y van seguidas de una o varias líneas que componen la suite. Por ejemplo

```python
if expression :
   suite
elif expression :
   suite
else :
   suite
```

## Argumentos de línea de comandos en Python

Muchos programas pueden ejecutarse para proporcionarle alguna información básica sobre cómo deben ejecutarse. Python le permite hacer esto con -h -.

```text
$ python3 -h
usage: python3 [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options and arguments (and corresponding environment variables):
-c cmd : program passed in as string (terminates option list)
-d     : debug output from parser (also PYTHONDEBUG=x)
-E     : ignore environment variables (such as PYTHONPATH)
-h     : print this help message and exit

[ etc. ]
```

También puedes programar tu script de forma que acepte varias opciones.
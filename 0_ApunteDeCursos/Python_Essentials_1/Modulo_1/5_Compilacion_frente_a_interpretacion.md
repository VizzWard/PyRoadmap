# La compilación frente a la interpretación

<mark>La programación de computadora es el acto de establecer una secuencia de instrucciones con la cual se causará el efecto deseado.</mark> El efecto podría ser diferente en cada caso específico: depende de la imaginación, el conocimiento y la experiencia del programador.

Por supuesto, tal composición tiene que ser correcta en muchos sentidos, tales como:

- **Alfabéticamente**: un programa debe escribirse en una secuencia de comandos reconocible, por ejemplo, el Romano, Cirílico, etc.
- **Léxicamente**: cada lenguaje de programación tiene su diccionario y necesitas dominarlo; afortunadamente, es mucho más simple y más pequeño que el diccionario de cualquier lenguaje natural.
- **Sintácticamente**: cada idioma tiene sus reglas y deben ser obedecidas.
- **Semánticamente**: El programa tiene que tener sentido.

Desafortunadamente, un programador también puede cometer errores en cada uno de los cuatro sentidos anteriores. Cada uno de ellos puede hacer que el programa se vuelva completamente inútil.

Supongamos que has escrito correctamente un programa. ¿Cómo persuadimos a la computadora para que lo ejecute? Tienes que convertir tu programa en lenguaje máquina. Afortunadamente, la traducción puede ser realizada por la computadora, haciendo que todo el proceso sea rápido y eficiente.

Existen dos formas diferentes de transformar un programa de un lenguaje de programación de alto nivel a un lenguaje de máquina:

`COMPILACIÓN` - <mark>el programa fuente se traduce una vez (sin embargo, esta ley debe repetirse cada vez que se modifique el código fuente) obteniendo un archivo (por ejemplo, un archivo .exe si el código está diseñado para ejecutarse en MS Windows) que contiene el código máquina</mark>; ahora puedes distribuir el archivo en todo el mundo; el programa que realiza esta traducción se llama compilador o traductor.

`INTERPRETACIÓN` - <mark>Tú (o cualquier usuario del código) puedes traducir el programa fuente cada vez que se ejecute; el programa que realiza este tipo de transformación se denomina intérprete, ya que interpreta el código cada vez que está destinado a ejecutarse</mark>; también significa que no puede distribuir el código fuente tal como está, porque el usuario final también necesita que el intérprete lo ejecute.

Debido a algunas razones muy fundamentales, un lenguaje de programación de alto nivel en particular está diseñado para caer en una de estas dos categorías.

Existen muy pocos idiomas que se pueden ser tanto compilados como interpretados. Por lo general, un lenguaje de programación se proyecta con este factor en la mente de sus constructores: ¿Se compilará o interpretará?
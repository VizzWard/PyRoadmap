# ¿Qué hace realmente el intérprete?

Supongamos una vez más que has escrito un programa. Ahora, existe como un archivo de computadora: un programa de computadora es en realidad una pieza de texto, por lo que el código fuente generalmente se coloca en archivos de texto.

> Nota: debe ser texto puro, sin ninguna decoración, como diferentes fuentes, colores, imágenes incrustadas u otros medios. Ahora tienes que invocar al intérprete y dejar que lea el archivo fuente.

<mark>El intérprete lee el código fuente de una manera que es común en la cultura occidental: de arriba hacía abajo y de izquierda a derecha.</mark> Hay algunas excepciones: se cubrirán más adelante en el curso.

En primer lugar, <mark>el intérprete verifica si todas las líneas subsiguientes son correctas</mark> (utilizando los cuatro aspectos tratados anteriormente).

<mark>Si el intérprete encuentra un error, termina su trabajo inmediatamente</mark>. El único resultado en este caso es un mensaje de error.

<mark>El intérprete te informará dónde se encuentra el error y qué lo causó</mark>. Sin embargo, estos mensajes pueden ser engañosos, ya que el intérprete no puede seguir tus intenciones exactas y puede detectar errores a cierta distancia de sus causas reales.

Por ejemplo, si intentas usar una entidad de un nombre desconocido, causará un error, pero el error se descubrirá en el lugar donde se intenta usar la entidad, no donde se introdujo el nombre de la nueva entidad.

En otras palabras, la razón real generalmente se ubica un poco antes en el código, por ejemplo, en el lugar donde se tuvo que informar al intérprete de que usarías la entidad del nombre.

<mark>Si la línea se ve bien, el intérprete intenta ejecutarla</mark>.

> Nota: cada línea generalmente se ejecuta por separado, por lo que el trío "Lectura - Verificación - Ejecución", puede repetirse muchas veces, más veces que el número real de líneas en el archivo fuente, debido a que algunas partes del código pueden ejecutarse más de una vez.

También es posible que una parte significativa del código se ejecute con éxito antes de que el intérprete encuentre un error. Este es el comportamiento normal en este modelo de ejecución.

Puedes preguntar ahora: ¿Cuál es mejor? ¿El modelo de "compilación" o el modelo de "interpretación"? No hay una respuesta obvia. Si lo hubiera, uno de estos modelos habría dejado de existir hace mucho tiempo. Ambos tienen sus ventajas y sus desventajas.

## La compilación frente a la interpretación - ventajas y desventajas

| | COMPILACIÓN | INTERPRETACIÓN|
|---|---|---|
|VENTAJAS|• La ejecución del código traducido suele ser más rápida.<br> • Solo el programador debe tener el compilador; el usuario final puede usar el código sin él.<br> • El código traducido se almacena en lenguaje máquina, ya que es muy difícil de entender, es probable que tus propios inventos y trucos de programación sigan siendo un secreto. | • Puedes ejecutar el código en cuanto lo completes; no hay fases adicionales de traducción.<br> • El código se almacena utilizando el lenguaje de programación, no el de la máquina; esto significa que puede ejecutarse en computadoras que utilizan diferentes lenguajes máquina; no se compila el código por separado para cada arquitectura diferente.|
|DESVENTAJAS| • La compilación en sí misma puede llevar mucho tiempo; es posible que no puedas ejecutar tu código inmediatamente después de cualquier modificación.<br> • Tienes que tener tantos compiladores como plataformas de hardware en las que deseas que se ejecute tu código.| • No esperes que la interpretación incremente tu código a alta velocidad: tu código compartirá la potencia de la computadora con el intérprete, por lo que no puede ser realmente rápido.<br> • Tanto tú como el usuario final deben tener el intérprete para ejecutar el código.|

**¿Qué significa todo esto para ti?**

- Python es un lenguaje interpretado. Esto significa que hereda todas las ventajas y desventajas descritas. Por supuesto, agrega algunas de sus características únicas a ambos conjuntos.
- Si deseas programar en Python, necesitarás el intérprete de Python. No podrás ejecutar tu código sin él. Afortunadamente, Python es gratis. Esta es una de sus ventajas más importantes.

Debido a razones históricas, <mark>los lenguajes diseñados para ser utilizados en la manera de interpretación a menudo se llaman lenguajes de scripting</mark>, mientras que los programas fuente codificados que los usan se llaman scripts.
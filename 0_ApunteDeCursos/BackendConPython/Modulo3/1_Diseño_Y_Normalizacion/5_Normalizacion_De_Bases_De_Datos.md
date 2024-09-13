# Normalización de bases de datos

## ¿Que es la normalización de bases de datos?

Es un proceso importante en el diseño de bases de datos relacionales que consiste en designar y aplicar una serie de reglas a las relaciones obtenidas tras el paso del modelo entidad-relación al modelo relacional con objeto de minimizar la redundancia de datos, facilitando su gestión posterior.

## Aspectos importantes

El proceso de normalizar la BD es básicamente reducir la redundancia.

El diseño debe ser lógico o acorde a las necesidades del usuario.

Al diseñar una BD hazte estas preguntas:

- ¿Que tipo de datos necesito guardar?
- ¿Cómo van a acceder los usuarios a los datos?
- ¿Los usuarios tendrán privilegios especiales sobre los datos?
- ¿Hay alguna forma de agrupar los datos?
- ¿Cómo se relacionan los datos entre ellos?
- ¿Cómo asegurar la integridad de los datos?
- ¿Los datos se repiten?

## Convención de nombres

Es importante elegir nombres relevantes a la información que allí se almacenará de esa forma serán fáciles de recordar.

Esto ayuda a mantener los objetos ordenados y evitar confusiones.

## Beneficios de la normalización

- Mantiene la BD organizada y fácil de usar.
- Reduce la repetición y redundancia de la información.
- Mejora la seguridad para el sistema y usuarios.
- Mejora la flexibilidad en el diseño.
- Asegura la consistencia.

## Contras de la Normalización

Puede reducir el rendimiento de la base de datos en algunos casos, eso es porque se requiere más poder de cómputo y memoria para realizar las tareas.

Una base de datos normalizada requiere unir muchos datos y tablas para devolver el resultado deseado.

## Desnormalización

Consiste en tomar una BD normalizada y modificarla para aceptar redundancia.
Este proceso puede llegar a ser útil cuando se desea mejorar el rendimiento.

> Depende la situación o el caso de negocio, puede ser buena idea normalizar o desnormalizar.

## Formas Normales

Una forma normal es un método para identificar los niveles o profundidad que se requiere para normalizar la BD.

No todas las bases de datos se llegan a normalizar a la misma profundidad, siempre es importante tener en cuenta las necesidades del usuario a resolver.

Una base de datos puede llegar a tener hasta 6 formas normales.

Las formas normales se aplican de forma secuencial, es decir primero la 1NF luego 2NF, etc.

> La mayoría de bases de datos reales en el mundo llegan hasta la tercera forma normal.
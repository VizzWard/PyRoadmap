# ORM

Un ORM (Object-Relational Mapping) es una técnica de programación que permite interactuar con una base de datos relacional utilizando objetos de un lenguaje de programación orientado a objetos. En el contexto de Python y Django, el ORM te permite trabajar con la base de datos usando clases y objetos de Python en lugar de SQL directamente.

## Ejemplos de ORM

- Django ORM (integrado en Django)
- SQLAlchemy (popular en aplicaciones Python no-Django)
- Peewee
- Pony ORM

## Ventajas del ORM

1. Abstracción de la base de datos: Puedes cambiar el motor de base de datos con mínimos cambios en el código.
2. Seguridad: Los ORM suelen incluir protección contra inyecciones SQL.
3. Productividad: Escribes menos código y te centras en la lógica de negocio.
4. Mantenibilidad: El código es más fácil de entender y mantener.
5. Portabilidad: Tu código puede funcionar con diferentes bases de datos.

## Desventajas del ORM

1. Rendimiento: En consultas complejas, el SQL generado puede no ser tan eficiente como el SQL escrito manualmente.
2. Curva de aprendizaje: Dominar un ORM puede llevar tiempo.
3. Abstracción excesiva: Puede ocultar detalles importantes del funcionamiento de la base de datos.
4. Limitaciones: Algunas operaciones complejas pueden ser difíciles de expresar a través del ORM.
5. Sobrecarga: Los ORM añaden una capa adicional entre tu aplicación y la base de datos, lo que puede afectar al rendimiento.


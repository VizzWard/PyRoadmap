# Metodos HTTP

Los métodos HTTP son las formas en que los navegadores web y otros clientes se comunican con los servidores a través del protocolo HTTP. Cada método describe una acción específica que el cliente quiere realizar en el servidor, como recuperar, enviar o modificar datos.

## GET

Se utiliza para recuperar datos del servidor. Es el método más común y se emplea para obtener recursos (como páginas HTML, imágenes, etc.).

Características:

- No modifica los datos en el servidor.
- Los datos de la solicitud, si existen, se envían como parte de la URL (query parameters).
- Es idempotente (si realizas la misma solicitud varias veces, el resultado será el mismo).

Ejemplo: Un usuario accede a una página web en http://example.com/products.

## POST

Se utiliza para enviar datos al servidor con el propósito de crear o modificar un recurso.

Características:

- Los datos se envían en el cuerpo de la solicitud (no en la URL).
- Puede tener efectos secundarios, como modificar el estado del servidor o crear nuevos recursos.
- No es idempotente (enviar la misma solicitud varias veces puede tener diferentes efectos, como crear varios registros).

Ejemplo: Un formulario de registro en un sitio web envía datos de usuario al servidor.

## PUT

Se usa para actualizar un recurso existente o crear uno si no existe.

Características:

- Es idempotente, lo que significa que realizar la misma solicitud varias veces tendrá el mismo efecto.
- En general, reemplaza el recurso existente por completo con los datos proporcionados.

Ejemplo: Actualizar los detalles de un producto en http://example.com/products/123.

## DELETE

Se utiliza para eliminar un recurso del servidor.

Características:

- Es idempotente (si se realiza varias veces, solo se eliminará el recurso una vez).

Ejemplo: Eliminar un producto de un inventario en http://example.com/products/123.

## PATCH

Se usa para modificar parcialmente un recurso existente.

Características:

- A diferencia de PUT, no reemplaza todo el recurso, sino que modifica solo una parte.
- No siempre es idempotente, dependiendo de cómo se implemente.

Ejemplo: Actualizar solo el precio de un producto en un inventario.
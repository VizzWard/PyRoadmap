# Como hacer peticiones

## Por medio de CURL

### Peticiones GET

El método GET se utiliza para recuperar información de un servidor. Con curl, puedes hacer una petición GET a JSONPlaceholder de la siguiente manera:

**Ejemplo: Obtener una lista de posts**:

```commandline
curl -X GET https://jsonplaceholder.typicode.com/posts
```

Esto devolverá una lista de posts en formato JSON.

**Ejemplo: Obtener un post específico**:

```commandline
curl -X GET https://jsonplaceholder.typicode.com/posts/1
```

Esto te devolverá los detalles del post con ID 1.

### Peticiones POST

El método POST se utiliza para enviar datos al servidor y crear un nuevo recurso. Para enviar datos en formato JSON, se puede usar la opción -H para especificar los headers y -d para los datos.

```commandline
curl -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Nuevo Post",
    "body": "Este es el contenido del nuevo post",
    "userId": 1
  }'
```

Este comando creará un nuevo post en el servidor. JSONPlaceholder es un servicio de ejemplo, así que los cambios no se guardan permanentemente, pero te devolverá el nuevo post en la respuesta.

### Peticiones PUT

El método PUT se utiliza para actualizar un recurso existente. De nuevo, se envían datos en formato JSON, pero con la URL del recurso que deseas modificar.

```commandline
curl -X PUT https://jsonplaceholder.typicode.com/posts/1 \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "title": "Post Actualizado",
    "body": "Este es el contenido actualizado del post",
    "userId": 1
  }'
```

### Petición DELETE

El método DELETE se utiliza para eliminar un recurso en el servidor. En el caso de JSONPlaceholder, puedes simular la eliminación de un recurso utilizando el método DELETE.

```commandline
curl -X DELETE https://jsonplaceholder.typicode.com/posts/1
```

### Opciones de curl utilizadas

- `-X [METHOD]`: Especifica el método HTTP que quieres usar (GET, POST, PUT, etc.).
- `-H "Content-Type: application/json"`: Especifica que el tipo de contenido es JSON.
- `-d '...'`: Indica los datos que se envían en el cuerpo de la solicitud.

### Respuesta esperada

Cada vez que realizas una petición, el servidor responde con un código de estado HTTP y un cuerpo que contiene el recurso en formato JSON. Por ejemplo, en la petición POST, deberías recibir una respuesta similar a esta:

```json
{
  "title": "Nuevo Post",
  "body": "Este es el contenido del nuevo post",
  "userId": 1,
  "id": 101
}
```

## Por medio de HTTP

### Peticiones GET

**Obtener todos los posts**:

```http request
GET /posts HTTP/1.1
Host: jsonplaceholder.typicode.com
```

**Obtener un post específico (ID 1)**:

```http request
GET /posts/1 HTTP/1.1
Host: jsonplaceholder.typicode.com
```

### Peticiones POST

```http request
POST /posts HTTP/1.1
Host: jsonplaceholder.typicode.com
Content-Type: application/json

{
    "title": "Nuevo Post",
    "body": "Este es el contenido del nuevo post",
    "userId": 1
}
```

### Peticiones PUT

```http request
PUT /posts/1 HTTP/1.1
Host: jsonplaceholder.typicode.com
Content-Type: application/json

{
    "id": 1,
    "title": "Post Actualizado",
    "body": "Este es el contenido actualizado del post",
    "userId": 1
}
```

### Petición DELETE

```http request
DELETE /posts/1 HTTP/1.1
Host: jsonplaceholder.typicode.com
```

### Explicación de los componentes

- Método HTTP: GET, POST o PUT en la primera línea, indicando el tipo de operación.
- Path: El recurso que se está solicitando, como /posts o /posts/1.
- Host: El nombre del servidor, en este caso, jsonplaceholder.typicode.com.
- Content-Type: Especifica que los datos que se envían o reciben están en formato JSON.
- Content-Length: La longitud en bytes del cuerpo de la petición (puedes calcularlo con las herramientas del servidor o cliente).
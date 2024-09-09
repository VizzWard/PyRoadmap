# Web

La web, también conocida como la World Wide Web (WWW), es un sistema de información que permite acceder y compartir recursos a través de Internet. 

Consiste en un conjunto de documentos interconectados mediante hipervínculos, que pueden incluir texto, imágenes, videos y otros archivos multimedia. Estos recursos están almacenados en servidores web y son accesibles mediante navegadores, que utilizan protocolos como HTTP (Hypertext Transfer Protocol) para solicitar y mostrar el contenido. En resumen, la web es la parte de Internet que facilita la navegación y visualización de información mediante páginas web.

La web funciona en una arquitectura llamada cliente-servidor, esta hace referencia a un modelo en el que tenemos una computadora central a la que otras computadoras se conectan para obtener la información almacenada.

## Como funciona la web?

La web (World Wide Web) es un sistema de información que permite a los usuarios acceder y compartir recursos a través de Internet. 

Funciona mediante la interacción entre navegadores web (clientes) y servidores web, utilizando protocolos de red como HTTP (Hypertext Transfer Protocol). 

Los navegadores solicitan páginas web desde servidores mediante URL, y los servidores responden con el contenido solicitado. Este contenido incluye texto, imágenes, videos y otros archivos.

## Arquitectura cliente-servidor

En la arquitectura cliente-servidor, el cliente es una máquina o aplicación que solicita servicios, mientras que el servidor es el que los provee. 

Los clientes envían solicitudes al servidor, y este responde proporcionando los datos o recursos solicitados. 

En la web, el cliente suele ser un navegador web, y el servidor es un servidor web que alberga los sitios web. 

Esta arquitectura permite la separación de responsabilidades, lo que mejora la escalabilidad y la eficiencia.

## ¿Qué es un protocolo de red?

Un protocolo de red es un conjunto de reglas y convenciones que permiten la comunicación entre dispositivos en una red. Estos protocolos definen cómo se formatean, transmiten y reciben los datos, asegurando que los dispositivos puedan intercambiar información de manera eficiente. Algunos ejemplos son TCP (Transmission Control Protocol), IP (Internet Protocol) y HTTP.

## Modelo OSI

El Modelo OSI (Open Systems Interconnection) es un marco teórico que divide la comunicación en redes en 7 capas:

1. Capa Física: Controla la transmisión de bits a través de un medio físico.
2. Capa de Enlace de Datos: Garantiza la transferencia de datos libre de errores entre nodos conectados.
3. Capa de Red: Dirige los paquetes entre diferentes redes.
4. Capa de Transporte: Asegura la entrega confiable de datos.
5. Capa de Sesión: Gestiona y controla las conexiones entre aplicaciones.
6. Capa de Presentación: Traduce los datos entre la capa de aplicación y la red.
7. Capa de Aplicación: Proporciona servicios de red a las aplicaciones.

## Modelo TCP/IP

El Modelo TCP/IP, a diferencia del modelo OSI, tiene 4 capas que describen el funcionamiento de las redes en Internet:

1. Capa de acceso a la red: Equivalente a la capa física y de enlace del modelo OSI.
2. Capa de Internet: Maneja la dirección y el enrutamiento de los paquetes (protocolo IP).
3. Capa de Transporte: Gestiona la entrega de datos entre los hosts (protocolo TCP).
4. Capa de Aplicación: Gestiona protocolos específicos de la aplicación, como HTTP, FTP y SMTP.

## Cómo opera TCP/IP?

TCP/IP es un conjunto de protocolos utilizados para la transmisión de datos en Internet. Funciona de la siguiente manera:

- **IP (Internet Protocol)**: Se encarga de enrutar y direccionar los paquetes de datos a través de redes. Divide la información en pequeños fragmentos llamados "paquetes" y los envía a su destino.
- **TCP (Transmission Control Protocol)**: Se encarga de la transmisión confiable de datos entre dos dispositivos. Establece una conexión entre el emisor y el receptor y garantiza que los paquetes se envíen en el orden correcto y sin errores.

## TCP/IP en la web

En la web, TCP/IP es la base de la comunicación. Cada vez que un navegador solicita una página web, se utilizan estos protocolos para establecer una conexión entre el cliente (navegador) y el servidor. TCP se asegura de que los datos lleguen correctamente y en el orden adecuado, mientras que IP se encarga de direccionar los paquetes desde el servidor al cliente.

## Protocolo HTTP

HTTP (Hypertext Transfer Protocol) es el protocolo de aplicación que permite la transferencia de información en la web. Funciona mediante el envío de solicitudes desde el cliente (navegador) al servidor y la recepción de respuestas. Las solicitudes HTTP pueden incluir métodos como GET (para obtener datos), POST (para enviar datos) y PUT (para actualizar datos).

## Códigos de estado HTTP

Los códigos de estado HTTP son respuestas que los servidores web envían a los clientes para informar sobre el resultado de una solicitud. Los más comunes incluyen:

- 200 OK: La solicitud fue exitosa.
- 301 Moved Permanently: El recurso solicitado ha sido movido de manera permanente a una nueva URL.
- 400 Bad Request: La solicitud está mal formada.
- 401 Unauthorized: La autenticación es requerida.
- 403 Forbidden: El cliente no tiene permiso para acceder al recurso.
- 404 Not Found: El recurso solicitado no fue encontrado.
- 500 Internal Server Error: Error general del servidor.

Estos códigos permiten a los desarrolladores identificar el estado de las solicitudes y resolver problemas en la comunicación cliente-servidor.

## Peticiones HTTP

Las peticiones HTTP (Hypertext Transfer Protocol) son solicitudes que un cliente (generalmente un navegador web) envía a un servidor web para interactuar con los recursos disponibles en ese servidor, como páginas web, imágenes, o archivos. Estas peticiones siguen el protocolo HTTP, que define cómo se formulan y procesan. Cada petición HTTP consta de varias partes, y existen diferentes tipos de métodos de petición, que permiten diferentes interacciones con los recursos. A continuación, te explico los componentes clave y los tipos de peticiones.

### Partes de una petición HTTP

Una petición HTTP se compone de los siguientes elementos:

1. Línea de solicitud: Es la primera línea de la petición y contiene:
    - El método HTTP (como GET o POST).
    - La URL del recurso solicitado.
    - La versión del protocolo HTTP (por ejemplo, HTTP/1.1).
    - Ejemplo: GET /index.html HTTP/1.1.

2. Cabeceras HTTP (headers): Son pares claves-valor que transmiten información adicional sobre la solicitud o sobre el cliente, como el tipo de navegador, el tipo de contenido aceptado, la autenticación, entre otros.
````http request
Host: www.example.com
User-Agent: Mozilla/5.0
Content-Type: application/json
````

3. Cuerpo (body): No todas las peticiones HTTP tienen cuerpo, pero cuando lo tienen (como en POST), contiene los datos que el cliente está enviando al servidor (por ejemplo, los datos de un formulario o archivos).

### Métodos HTTP principales

Cada petición HTTP incluye un método que indica la acción que se quiere realizar con el recurso. Algunos de los métodos más comunes son:

1. **GET**:
    - Se utiliza para solicitar un recurso del servidor.
    - No tiene un cuerpo en la solicitud.
    - Se usa generalmente para obtener datos sin realizar cambios en el servidor.
    - Ejemplo: Solicitar una página web o un archivo.
2. **POST**:
    - Se usa para enviar datos al servidor, generalmente para crear o actualizar recursos.
    - Contiene un cuerpo con los datos que se están enviando (por ejemplo, un formulario).
    - Ejemplo: Enviar datos de un formulario de registro.
3. **PUT**:
    - Utilizado para enviar datos al servidor, pero a diferencia de POST, generalmente se utiliza para actualizar un recurso existente.
    - El cuerpo de la solicitud contiene los datos para la actualización.
    - Ejemplo: Actualizar información de un usuario en una base de datos.
4. **DELETE**:
    - Solicita al servidor que elimine un recurso.
    - No suele tener un cuerpo en la solicitud.
    - Ejemplo: Eliminar un registro o archivo en el servidor.
5. **HEAD**:
    - Similar a GET, pero solo solicita las cabeceras de la respuesta, sin el cuerpo.
    - Se utiliza para verificar si un recurso está disponible o para comprobar la meta-información, como la fecha de modificación.
6. **PATCH**:
    - Similar a PUT, pero se usa para realizar actualizaciones parciales a un recurso existente.
    - Solo envía los cambios específicos, no el recurso completo.

### Cabeceras HTTP comunes

Algunas de las cabeceras que suelen aparecer en las peticiones HTTP incluyen:

- Host: Indica el nombre del servidor (dominio).
    - Ejemplo: Host: www.ejemplo.com.
- User-Agent: Información sobre el cliente (navegador o aplicación) que está haciendo la solicitud.
    - Ejemplo: User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64).
- Content-Type: Especifica el tipo de contenido enviado en el cuerpo de la solicitud (en métodos como POST o PUT).
    - Ejemplo: Content-Type: application/json.
- Accept: Indica qué tipos de respuesta puede manejar el cliente.
    - Ejemplo: Accept: text/html.

### Respuesta HTTP

Después de recibir una petición HTTP, el servidor devuelve una respuesta HTTP que incluye:

- Código de estado: Indica si la solicitud fue exitosa o no (por ejemplo, 200 OK o 404 Not Found).
- Cabeceras: Información adicional sobre la respuesta (como el tipo de contenido).
- Cuerpo: Los datos solicitados (como una página web o una imagen).

### Ejemplo de una petición GET

```http request
GET /index.html HTTP/1.1
Host: www.ejemplo.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html
```

### Ejemplo de una petición POST

```http request
POST /api/usuarios HTTP/1.1
Host: www.ejemplo.com
Content-Type: application/json
Content-Length: 60

{
   "nombre": "Juan",
   "email": "juan@ejemplo.com"
}
```

### Importancia de las peticiones HTTP

Las peticiones HTTP son la base de la comunicación en la web. Permiten que los navegadores (o cualquier cliente HTTP) soliciten recursos, interactúen con servicios en línea y envíen datos para crear o modificar información en un servidor web.
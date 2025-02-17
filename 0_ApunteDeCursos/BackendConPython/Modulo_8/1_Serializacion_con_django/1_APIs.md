# Introducción a las APIs

## ¿Qué es una API?
Una API (*Application Programming Interface*) es un conjunto de reglas y protocolos que permiten que diferentes aplicaciones se comuniquen entre sí. Facilita la interacción entre software sin necesidad de conocer su implementación interna.

## ¿Cómo funcionan las APIs?
Las APIs actúan como intermediarios que permiten que una aplicación solicite datos o servicios de otra. Esta comunicación suele realizarse mediante peticiones y respuestas, utilizando protocolos estándar como HTTP.

### Ejemplo de flujo de una API:
1. Un cliente envía una solicitud a la API (por ejemplo, una petición HTTP GET).
2. La API procesa la solicitud y obtiene la información solicitada.
3. La API devuelve una respuesta en un formato estructurado (normalmente JSON o XML).

---

## ¿Qué es REST?
REST (*Representational State Transfer*) es un estilo de arquitectura para diseñar servicios web. Se basa en principios como:
- Uso de métodos HTTP (GET, POST, PUT, DELETE).
- Stateless (sin estado): cada solicitud es independiente.
- Uso de URLs como identificadores de recursos.
- Comunicación en formato estándar como JSON o XML.

## ¿Qué es RESTful?
Una API es considerada RESTful si sigue los principios de la arquitectura REST. Esto significa que:
- Usa recursos bien definidos a través de URLs.
- Aplica correctamente los métodos HTTP.
- Mantiene una estructura coherente y predecible en las respuestas.

---

## Tipos de APIs
Las APIs pueden clasificarse en distintos tipos según su accesibilidad y propósito:

1. **APIs Abiertas (Públicas)**: Cualquier desarrollador puede usarlas (ej. APIs de Google Maps, Twitter).
2. **APIs Privadas**: Solo son utilizadas dentro de una organización.
3. **APIs de Socios**: Accesibles solo para socios autorizados.
4. **APIs Compuestas**: Combinan múltiples servicios en una sola API.

---

## ¿Cómo Proteger una API REST?
Para asegurar una API REST y evitar accesos no autorizados, se pueden implementar las siguientes medidas:

1. **Autenticación y Autorización**
   - Uso de tokens JWT (JSON Web Token).
   - OAuth 2.0 para gestionar accesos.
   - API keys para validar solicitudes.

2. **Cifrado de Datos**
   - Uso de HTTPS para proteger la comunicación.
   
3. **Rate Limiting**
   - Limitar el número de solicitudes por usuario/IP para prevenir ataques DDoS.

4. **Validación de Datos**
   - Sanitizar y validar entradas para evitar ataques como SQL Injection o XSS.

5. **Registro y Monitoreo**
   - Implementar logs y herramientas de monitoreo para detectar accesos sospechosos.

Con estas estrategias, se puede mejorar la seguridad de una API REST y proteger los datos de los usuarios y servicios conectados.


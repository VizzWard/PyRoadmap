# [Django : Class Based Views vs Function Based Views](https://medium.com/@ksarthak4ever/django-class-based-views-vs-function-based-view-e74b47b2e41b)

Originalmente, Django solo tenía FBV, pero se agregaron CBV como una forma de crear plantillas de funcionalidad para no tener que escribir código repetitivo.

**Puntos clave:**

- Definición: Las CBV son clases de Python que Django proporciona con funcionalidad preconfigurada que se puede reutilizar y, a menudo, extender.

- Requisitos de las vistas de Django:

    - Deben ser invocables.
    - Deben aceptar un objeto `HttpRequest` como primer argumento posicional.
    - Deben devolver un objeto `HttpResponse` o generar una excepción.

- CBV vs. FBV: Las CBV no reemplazan a las FBV. Ambas tienen pros y contras.

## Vistas basadas en funciones (FBV)

### Pros:

- Fáciles de implementar y leer.
- Flujo de código explícito.
- Uso sencillo de decoradores.
- Adecuadas para funcionalidades únicas o especializadas.

### Contras:

- Difíciles de extender y reutilizar el código.
- Manejo de métodos `HTTP` a través de ramificación condicional.

Ejemplo: Se proporciona un ejemplo de una vista de creación basada en funciones.

## Vistas basadas en clases (CBV)

### Pros:

- Reutilización de código: una clase de vista puede ser heredada por otra clase de vista y modificada para un caso de uso diferente.
- DRY (No te repitas): las CBV ayudan a reducir la duplicación de código.
- Extensibilidad de código: las CBV se pueden extender para incluir más funcionalidades utilizando Mixins.
- Estructuración de código: una CBV ayuda a responder a diferentes solicitudes HTTP con diferentes métodos de instancia de clase en lugar de sentencias de ramificación condicional dentro de una única FBV.
- Vistas genéricas basadas en clases incorporadas.

### Contras:

- Más difíciles de leer.
- Flujo de código implícito.
- El uso de decoradores de vista requiere una importación adicional o la anulación de métodos.

Ejemplo: Se proporciona un ejemplo de una vista de creación basada en clases.

`as_view()`: Este método permite anular los atributos de clase en las `URLconf`.

## Vistas genéricas basadas en clases de Django

- Se introdujeron para abordar los casos de uso comunes en una aplicación web, como la creación de nuevos objetos, el manejo de formularios, las vistas de lista, la paginación y las vistas de archivo.
- Se pueden implementar desde el módulo django.views.generic.
- Aceleran el proceso de desarrollo.

### Cómo modificar una CBV para heredar de `django.views.generic.CreateView`:

```python
from django.views.generic import CreateView 
class MyCreateView(CreateView):
    model = MyModel  
    form_class = MyForm
```

### Estrategias para usar las vistas genéricas basadas en clases de Django:

- Comenzar de forma sencilla.
- Agregar mixins para construir la funcionalidad.
- Anular los métodos necesarios para obtener la funcionalidad deseada.

## Que tipo de Viste deberia usar?

![CBV vs FBV](https://miro.medium.com/v2/resize:fit:720/format:webp/1*1NgVsYmmLCiwXUy-uE0VLA.jpeg)
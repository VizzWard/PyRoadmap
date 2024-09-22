# Patrones de Diseño

Los patrones de diseño o design patterns, son una solución general, reutilizable y aplicable a diferentes problemas de diseño de software. Se trata de plantillas que identifican problemas en el sistema y proporcionan soluciones apropiadas a problemas generales a los que se han enfrentado los desarrolladores durante un largo periodo de tiempo, a través de prueba y error.

## Model View Template (MVT)

En Django, el controlador sigue estando presente, nada más que de una manera intrínseca, ya que todo el framework Django es el controlador.

- __Model__: Maneja todo lo relacionado con la información, esto incluye cómo acceder a esta, la validación, relación entre los datos y su comportamiento.
- __Template__: Decide cómo será mostrada la información.
- __View__: Es un enlace entre el modelo y el template. Decide qué información será mostrada y por cual template.

> Por desgracia, la interpretación de "view" (vista) en otro ámbito puede hacer referencia a "al modo de presentación de los datos" y en un framework web distinto a Django el termino "view" puede considerare como el "controlador" y "template" como la "vista". Esto es una desafortunada confusión a raíz de las diferentes interpretaciones de MVC. No te preocupes, con la practica con solo pensar en "view" de Django sabrás exactamente su función. Lo mejor es abstraerse de estar comparando siempre ambos modelos y enfocarse solo en comprender los conceptos del framework en uso. 

### Funcionamiento MTV de Django

![](https://espifreelancer.com/images/Django_mtv.webp)

Al momento de hacer click en un enlace o escribir una dirección (**1**) a lo primero que se accede es al mapa de URLs (también conocido como URL map o URL conf), en este archivo cada ruta esta asociado con una view (**2**), si se necesita algún dato se solicitara este a model (**3**) el cual a su vez generara la consulta a la base de datos, cuando los datos han sido traídos estos son enviados al template (**4**) que contiene la lógica de presentación para estos. Luego de "pintar" la pagina esta se enviá al navegar que hizo la solicitud (**5**).
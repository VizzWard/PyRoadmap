# Flask

Flask es un framework web ligero y flexible para desarrollar aplicaciones web en Python. Fue diseñado para ser simple y minimalista, ofreciendo las herramientas esenciales para crear aplicaciones web sin imponer una estructura rígida o una gran cantidad de configuraciones.

Algunas de las características de Flask incluyen:

- Simplicidad y flexibilidad: Flask es fácil de aprender y usar, lo que lo convierte en una excelente opción para desarrolladores principiantes o para aplicaciones pequeñas.
- Sin opiniones fuertes: A diferencia de otros frameworks como Django, Flask no impone una forma específica de organizar el proyecto. Los desarrolladores tienen más libertad para estructurar su aplicación como deseen.
- Extensible: Aunque Flask es ligero, es muy flexible y se pueden añadir fácilmente extensiones para funcionalidades avanzadas como autenticación, manejo de formularios, interacción con bases de datos, etc.
- Basado en WSGI: Flask está construido sobre WSGI (Web Server Gateway Interface), lo que lo convierte en una opción moderna para el desarrollo web en Python.
- Jinja2 y Werkzeug: Flask utiliza el motor de plantillas Jinja2 para renderizar HTML y Werkzeug como una biblioteca para gestionar solicitudes HTTP.

Un ejemplo básico de una aplicación Flask sería:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```
# Templates

En Flask (y otros frameworks web), los templates son archivos que contienen el código HTML dinámico que será renderizado y enviado al cliente (navegador). Los templates permiten generar páginas web con contenido que puede variar en función de datos proporcionados por la aplicación. En lugar de escribir HTML estático, los templates permiten insertar variables, lógica básica (como bucles y condicionales) y reutilizar fragmentos de código (por ejemplo, encabezados y pies de página comunes).

## Caracteristicas

- Lenguaje de plantillas: Flask utiliza Jinja2 como su motor de plantillas. Jinja2 permite la inserción de variables dinámicas, condicionales, bucles y otras funcionalidades en el HTML.
- Separación de la lógica y la presentación: Los templates permiten separar la lógica del backend (en Python) de la presentación (HTML). Esto facilita mantener y modificar la apariencia de una aplicación sin tocar la lógica del servidor.

## Directorio `templates/`

El directorio templates/ es donde Flask espera encontrar los archivos de plantillas HTML. Por convención, todos los archivos de plantillas (HTML) se almacenan en este directorio para que Flask pueda encontrarlos y utilizarlos cuando se les llame desde el backend.

### Ejemplo

Supongamos que tienes una aplicación Flask y quieres mostrar una página con un saludo personalizado.

1. En tu directorio del proyecto, crea un subdirectorio llamado templates/.
2. Dentro de templates/, crea un archivo llamado hello.html que contendrá el HTML dinámico:

`templates/hello.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello, {{ name }}!</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
    <p>Welcome to our website, {{ name }}. We're glad to have you here!</p>
</body>
</html>
```
En este archivo, el valor de la variable {{ name }} será proporcionado por Flask cuando se renderice la página.

3. Ahora, en tu aplicación Flask, usas la función render_template() para renderizar este archivo HTML y pasarle los datos:\

`app.py`:
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
```

En este ejemplo:

- La ruta /hello/<name> recibe un parámetro name desde la URL.
- Flask renderiza el archivo hello.html y reemplaza la variable {{ name }} con el valor proporcionado desde la URL.
- Si un usuario visita http://localhost:5000/hello/John, verá una página con el mensaje "Hello, John!".

## Lógica en los templates

Jinja2 permite introducir lógica básica en los templates, como condicionales o bucles.

Ejemplo con condicionales y bucles:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
    
    {% if age >= 18 %}
    <p>You are an adult.</p>
    {% else %}
    <p>You are underaged.</p>
    {% endif %}
    
    <h2>Your favorite fruits:</h2>
    <ul>
    {% for fruit in fruits %}
        <li>{{ fruit }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

Aquí, `age` y `fruits` son variables pasadas desde el backend. El template:

- Usa un condicional para mostrar un mensaje diferente según la edad.
- Recorre la lista fruits y muestra cada elemento como un ítem de lista.
# Redirecciones

En Flask (y en el desarrollo web en general), una redirección es una respuesta que el servidor envía al navegador o cliente, indicándole que debe realizar una nueva solicitud a una URL diferente. Es una manera de redirigir a los usuarios de una ruta a otra, ya sea dentro del mismo sitio web o hacia un sitio externo.

## ¿Cuándo usar redirecciones?

Las redirecciones son útiles en muchos escenarios, por ejemplo:

- Después de un envío de formulario exitoso, redirigir al usuario a una página de confirmación para evitar que el formulario se envíe nuevamente si el usuario recarga la página.
- Para reorganizar URLs sin que los usuarios pierdan acceso al contenido (por ejemplo, redirigir una página antigua a una nueva).
- Para forzar la autenticación, redirigiendo a los usuarios no autenticados a una página de inicio de sesión.
- Para manejar errores o rutas incorrectas, redirigiendo a los usuarios a una página de error personalizada.

## Redirecciones en Flask

En Flask, se utiliza la función redirect() junto con una URL a la cual se debe redirigir al usuario.


```python
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the homepage!"

@app.route('/login')
def login():
    return "Please log in here."

@app.route('/success')
def success():
    return "You have successfully logged in!"

@app.route('/authenticate/<username>')
def authenticate(username):
    if username == "admin":
        return redirect(url_for('success'))
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
```

Explicación:

1. `redirect()`: La función `redirect()` genera una redirección HTTP. Cuando el usuario accede a `/authenticate/<username>`, si el `username` es "admin", es redirigido a la ruta `success`. Si no, se redirige a la ruta `login`.

2. `url_for()`: Flask utiliza `url_for()` para generar la URL de una función por su nombre, en lugar de escribir la URL de forma explícita. Esto es útil para evitar errores si cambias las rutas de tu aplicación en el futuro.

    - `url_for('success')` genera la URL para la función success.
    - `url_for('login')` genera la URL para la función login.

## Código HTTP de Redirecciones

Cuando se realiza una redirección, el servidor responde con un código de estado HTTP 3xx, lo que indica al navegador que debe hacer una nueva solicitud a la URL proporcionada. El código más común es 302 (redirección temporal).

```python
@app.route('/old-route')
def old_route():
    return redirect(url_for('new_route'), 301)  # Redirección permanente

@app.route('/new-route')
def new_route():
    return "This is the new route!"
```

- 301 (Redirección permanente): Se usa cuando la URL original ha cambiado de forma permanente.
- 302 (Redirección temporal): Indica que la URL original podría ser accesible en el futuro, pero por ahora se está redirigiendo temporalmente.

## Redirección a una URL externa

Además de redirigir dentro de tu aplicación, también puedes redirigir a URLs externas.

```python
@app.route('/external')
def external():
    return redirect("https://www.google.com")
```

En este caso, el usuario será redirigido a `https://www.google.com`.
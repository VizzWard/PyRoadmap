# Route

El decorador @route en Flask se utiliza para asociar una función de Python con una URL específica dentro de la aplicación web. Es una de las funcionalidades clave de Flask que permite definir cómo responderá la aplicación a una solicitud HTTP en una ruta particular.

El decorador @route se coloca encima de una función que define el contenido o la respuesta que se devolverá cuando un usuario acceda a la ruta (URL) correspondiente.

## Syntax

```python
@app.route('ruta')
def nombre_funcion():
    # código que genera la respuesta
    return respuesta
```

- `@app.route('ruta')`: Este decorador mapea una URL a una función. Cuando un usuario visita la URL que coincide con 'ruta', la función asociada se ejecuta.
- `nombre_funcion()`: La función que manejará la solicitud a esa ruta. Debe devolver una respuesta (normalmente una cadena de texto o un HTML).

## Ejemplo

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the homepage!'

@app.route('/about')
def about():
    return 'This is the about page.'
```

En este ejemplo:

- La función `home()` está asociada a la URL raíz (`/`), por lo que cuando un usuario accede a la página principal del sitio (`http://localhost:5000/`), verá "Welcome to the homepage!".
- La función `about()` está asociada a la ruta `/about`, por lo que cuando un usuario accede a `http://localhost:5000/about`, verá "This is the about page."

## Parámetros en las rutas

El decorador @route también puede manejar rutas dinámicas con parámetros, por ejemplo:

```python
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'
```

En este caso, si un usuario accede a `http://localhost:5000/user/John`, la respuesta sería "User: John", donde `username` es un parámetro extraído de la URL.
# Sessions

En Flask (y en el desarrollo web en general), las sesiones permiten almacenar información específica del usuario entre diferentes solicitudes (requests) a una aplicación web. Son útiles cuando deseas mantener el estado del usuario entre distintas páginas, como cuando un usuario ha iniciado sesión o cuando deseas rastrear sus interacciones a lo largo de la navegación.

## ¿Por qué son necesarias las sesiones?

HTTP es un protocolo sin estado (stateless), lo que significa que cada solicitud es independiente y el servidor no tiene ninguna memoria de las solicitudes anteriores. Si necesitas que la aplicación "recuerde" información del usuario entre solicitudes, como si está autenticado o qué productos ha agregado a su carrito de compras, las sesiones proporcionan una forma sencilla de hacerlo.

## Características clave de las sesiones

- Almacenan información por usuario: Cada usuario tiene su propia sesión única, donde se pueden guardar datos como su nombre, ID de usuario, productos en su carrito, etc.
- Basadas en cookies: Flask almacena la sesión en el lado del cliente usando cookies, específicamente a través de una cookie llamada session. Esta cookie contiene una referencia a los datos de la sesión (generalmente encriptada).
- Seguridad: Flask firma la cookie de la sesión para evitar que los usuarios la manipulen. Por defecto, los datos de la sesión son serializados y firmados con un secreto, de modo que no puedan ser modificados sin que el servidor lo detecte.

## Cómo funcionan las sesiones en Flask

1. Crear una sesión: Cuando se necesita almacenar información del usuario, se guarda en la sesión, que es simplemente un diccionario accesible mediante session.
2. Almacenar datos: Flask almacena los datos de la sesión en una cookie encriptada en el navegador del usuario.
3. Acceder a los datos: En cada solicitud, Flask desencripta la cookie de la sesión y permite que accedas a los datos almacenados.
4. Cerrar sesión: Puedes eliminar los datos de la sesión cuando el usuario cierre sesión o cuando ya no se necesiten.

```python
from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)

# La clave secreta es necesaria para firmar las cookies de sesión
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f'Logged in as {username}'
    return 'You are not logged in'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Almacena el nombre de usuario en la sesión
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type="text" name="username" placeholder="Enter username">
            <p><input type="submit" value="Login">
        </form>
    '''

@app.route('/logout')
def logout():
    # Elimina los datos de la sesión
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

Explicación:

1. `app.secret_key`: Se necesita una clave secreta para firmar las cookies de la sesión. Esto garantiza que los datos de la sesión no puedan ser manipulados por el cliente.
2. Almacenar en la sesión: En la ruta `/login`, si el método es `POST`, el valor del campo `username` del formulario se almacena en `session['username']`.
3. Acceso a la sesión: En la ruta `/`, Flask verifica si la clave `username` existe en la sesión. Si es así, muestra el nombre del usuario almacenado. Si no, informa que no ha iniciado sesión.
4. Eliminar datos de la sesión: En la ruta `/logout`, se utiliza `session.pop()` para eliminar `username` de la sesión, lo que efectivamente "cierra sesión" al usuario.

## Ciclo de vida de una sesión

1. El usuario accede a la aplicación por primera vez. No hay información de sesión asociada aún.
2. Después de que el usuario realiza una acción (como iniciar sesión), la aplicación almacena información en la sesión.
3. En cada solicitud posterior, Flask recupera los datos de la sesión desde la cookie del navegador y los desencripta para usarlos.
4. El usuario puede cerrar sesión, eliminando los datos almacenados en la sesión.

## Persistencia de sesiones

Por defecto, las sesiones en Flask están respaldadas por cookies, lo que significa que las sesiones se mantendrán mientras la cookie sea válida (hasta que expire o se elimine manualmente por el navegador o el servidor). También es posible configurar una sesión para que expire después de un tiempo determinado.

### Ejemplo con expiración de sesión

```python
from flask import Flask, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'another_secret_key'

# Establecer la duración de la sesión (30 minutos)
app.permanent_session_lifetime = timedelta(minutes=30)

@app.route('/')
def set_session():
    session.permanent = True  # La sesión es permanente (expira según el tiempo establecido)
    session['data'] = 'Session data stored'
    return 'Session created with expiration time'
```

En este caso, la sesión expirará automáticamente después de 30 minutos de inactividad.
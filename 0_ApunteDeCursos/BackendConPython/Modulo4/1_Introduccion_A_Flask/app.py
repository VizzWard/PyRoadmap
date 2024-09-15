# Importar la libreria flask
from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__) # __name__ buscar que es
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Decorador para requerir el login
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# Crear el primer endpoint
@app.route('/')
@login_required
def home():
    return render_template('index.html')

'''
Para ejecutar el archivo desde flask se usa el comando:
flask --app proy run
proy es el nombre del archivo a ejecutar
Nota: el comando se debe ejecutar desde la carpeta donde esta el archivo
'''

# Usar Templates
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')
    # Render Template:

# Hacer un login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials'
        else:
            session['logged_in'] = True
            flash('You were logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

# Hacer un logout
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out!')
    return redirect(url_for('welcome'))


# Para correr el archivo directamente con python
# Se debe agregar esta sentencia, para poder usarlo con flask:
if __name__ == '__main__':
    app.run(debug=True)
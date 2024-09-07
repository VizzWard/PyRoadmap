''' Clase 1 '''

# Para crear nuestras propias clases usaremos la palabra reservada 'class'

#Syantax: class <NombreDeLaClase>: Usando la nomenclatura CamelCase
class Usuario:
    # En python no se pueden dejar bloques vacios
    pass

# Instanciamos la clase
user = Usuario()
print(user)


''' Clase 2 '''

# Podemos dividir los atributos de una clase en dos tipos:
# Atributos de clase - atributos que le pertenecen a una clase y para usarlos tendremos que llamar a la clase.
# Atributos de instancia - atributos que le pertenecen al objeto y podemos usarlos sobre el objeto.

class User:
    username = 'VizzWard' # Atributo de clase
    email = 'none@gmail.com' # Atributo de clase

# Para usar un atributo de clase lo haremos de la sig manera:
print(User.username)

# Podemos modificar el atributo
Usuario.username = 'VzW'
print(Usuario.username)


''' Clase 3 '''

# Atributos de instancia
user1 = User()
print(user1.username)
# Estamos accediando a un atributo de clase, pero por como funciona python, podemos añadir de forma
# dinamica atributos a nuestro objeto en tiempo de ejecutcion. Para poder lograr esto, python trabaja
# con un meta atributo llamado __dict__

print(user1.__dict__) # Visualizamos un diccionario vacio, ya que hasta el momento este no posee ningún atributo.

# Sabemos que la instancia esta vacia, pero ¿por qué puedo acceder al atributo de clase por medio de la instancia?
# Esto es debido a las verificaciones que hace python:
# 1. Verifica si el atributo existe en el objeto, si no es asi, pasa a la sig verificacion.
# 2. Verifica si el atributo existe en la clase, si existe utiliza este atributo.
# 3. Si no existe el atributo, lanza un error.


''' Clase 4 '''

# Añadimos el atributo al objeto
user1.username = 'V1ZZ' # Ahora este ya es el atributo de instancia
user1.email = 'void@gmail.com'
user1.password = '1234'
# Este atributo no existe en la clase, pero de igual manera lo podemos asignar al objeto,
# siendo este un atributo unicamente de instancia

print(user1.username)
print(user1.__dict__)



''' Clase 5 '''

# Si no estandarizamos la cantidad de atributos que puede contener cada objeto,
# en un punto llegaremos a tener errores.
# Lo recomendable es que cuando instanciemos objetos de una clase, siempre
# cuidemos que estos tengan los mismos atributos.

# Podemos estandarizar esto de la sig manera:
class Persona:

    # Para que se pueda considerar un metodo, esta debe poseer un parametro
    # el cual hace referenciar al objeto, por convencion este parametro de llama self.
    # E igualmente le podemos pasar cualquier otro tipo de parametro
    def inicializar(self, nombre, apellido): # self hace referencia al objeto
        self.nombre = nombre
        self.apellido = apellido
        # Estos atributos se añaden al objeto.

user2 = Persona() # Instanciamos la clase, y esto nos da un objeto vacio.
user3 = Persona()
print(user2.__dict__)
print(user3.__dict__)

# Al llamar al metodo inicializar, de forma dinamica se añadiran los atributos al objeto.
user2.inicializar('Jose', 'Hernandez')
user3.inicializar('Luis', 'Dzib')
# Al añadirle otros parametros al metodo inicializar, debemos pasarle los argumentos necesarios.

print(user2.__dict__)
print(user3.__dict__)

# De esta manera estandarizaremos la cantidad de atributos que tendran nuestros objetos
# siempre y cuando se llame al metodo inicializar


''' Clase 6 '''

# Definimos un metodo para inicializar atributos a los objetos
# Pero esto no es necesario, ya que python ya incluye un metodo para ello:
class Trabajador:
    def __init__(self, nombre, apellido): # El metodo __init__ es nuestro metodo para inicializar atributos
        # Este metodo se llamara automaticamente, cuando instanciemos un objeto.
        self.nombre = nombre
        self.apellido = apellido

# Al usar __init__, ya no tendremos que llamar al metodo para añadir atributos al objeto,
# si no, que estos se agregaran al momento de instanciar la clase.
user4 = Trabajador('Vicente', 'Rodriguez')
print(user4.__dict__)
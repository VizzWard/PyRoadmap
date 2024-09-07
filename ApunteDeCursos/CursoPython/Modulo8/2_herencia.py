''' Clase 7 '''

# Herencia

# Clase Padre
class Animal:
    def comer(self):
        print('El animal come')

    def dormir(self):
        print('El animal duerme')

# Clase a heredar
class Mascota(Animal): # Clase padre
    def comer(self): # Sobreescribimos el metodo
        print('La mascota come')

# Estructura para heredar:
# class ClaseHija(ClasePadre):
class Perro(Mascota): # Clase Hija
    pass

duke = Perro()

# Al ser este un objeto de la clase perro
# este puede acceder a los metodos de la clase padre
duke.comer()
duke.dormir()

# No hay límite de veces que se puede heredar una clase


''' Clase 8 '''

# Herencia Multiple -> Una clase puede heredar multiples clases

# Segunda clase padre
class Felino:
    def maullar(self):
        print('El felino maulla')

# clase a heredar multiples clases
class Tigre(Mascota, Felino):
    pass

# Este objeto hereda dos clases, por ende puede acceder a los metodos de esas clases.
max = Tigre()
max.comer()
max.dormir()
max.maullar()


''' Clase 9 '''

# Sobreescritura/Sobrecarga de metodos
# Esto significa que una clase hija, puede modificar los comportamientos de los metodos de la clase padre.

class Gato(Mascota, Felino):
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self): # Sobreescribimos el metodo, para modificar el comportamiento del metodo
        super().comer() # Con esto accederemos al metodo de la clase padre (Mascota), usando asi su funcion 'comer'.
        print('El gato come')

    def dormir(self):
        print('El gato duerme')

will = Gato('Will')

will.comer()
will.dormir()


''' Clase 10 '''

# Funcion super()
# Nos permite acceder a la clase padre, para ejecutar sus metodos

# Modificaremos la clase gato, para hacer uso de los metodos de la clase padre, a pesar de estar sobreescrito.
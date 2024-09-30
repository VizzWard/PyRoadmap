# Declarar una variable
x = 5

# Comillas dobles o simples
y = 'Hola'
# Es lo mismo que:
y= "Hola"

# Case sensitive
a = 4
# No es la misma variable que:
A = 4

# Declarar varias variables con el mismo valor
x = y = z = 'Hola Python'

# Declarar multiples variables en una sola linea
x, y, z = 'Hola', 'Python', 'Roadmap'

# Guardar los valores de una lista en multiples variables
frutas = ['manzana', 'mango', 'pera']
x, y, z = frutas



curso = 'Python' # Variable global

def roadmap():
    curso = 'Roadmap'

roadmap()
# La llamada a la funcion no cambia la variable global
# Ya que dentro de la funcion `curso` se considera una variable local, diferente de la otra
print(curso)

# Para poder cambiar la variable global se usa:
def roadmap():
    global curso
    curso = 'Roadmap'

roadmap()
print(curso)
''' Clase 8 '''
from ApunteDeCursos.CursoPython.Modulo6.condicionales import calificacion

# Ciclo For

usuarios = ['user1', 'User2', 'User3']

# Equivalente a for each en java
for usuario in usuarios:
    print(usuario)


''' Clase 9 '''
titulo_curso = 'Curso de Python'

# Break
for caracter in titulo_curso:
    if caracter == 'P':
        break # Esto rompe el ciclo For

    print(caracter)

# Continue
for caracter in titulo_curso:
    if caracter == ' ':
        continue # Esto hara que se salte esta iteracion
    
    print(caracter)
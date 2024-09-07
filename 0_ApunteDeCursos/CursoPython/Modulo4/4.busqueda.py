''' Clase 6 '''

curso = 'Curso de Python'

# Saber si existe un string en el string
contador = curso.count('Python') # Devuelve las veces que se encuentra la palabra o caracter indicado
print(contador)

# Buscar por medio de 'in'
print('Python' in curso) # Retorna un boolean
print('python' in curso.lower()) # Buscar la palabra, convirtiendo el string en miniscula

# Saber si un string comienza con una palabra o caracter
print(curso.startswith('Curso')) # Retorna un boolean

# Saber si un string termina con una palabra o caracter
print(curso.endswith('Python')) # Retorna un boolean
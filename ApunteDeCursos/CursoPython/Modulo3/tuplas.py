# Crear una tupla
from ApunteDeCursos.CursoPython.Modulo1.operadores import resultado

tupla = (0, 1, 2, 3, 4)

# Acceder a elementos
print(tupla[3])

# Concatenar tuplas
tupla2 = (5, 6, 7, 8, 9)
tupla_concat = tupla + tupla2
print(tupla_concat)

# Repetir una tupla
tupla_repeat = tupla * 2
print(tupla_repeat)

# Subtuplas
subtupla = tupla[1 : 4]
print(subtupla)

# Convertir lista a tupla
dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
week = tuple(dias)
print(week)
print(type(week))

# Convertir tupla a lista
dia = list(week)
print(dia)
print(type(dia))

# Descomprimir
cero, uno, dos, tres, cuatro = tupla
print(cero, uno, dos, tres, cuatro)

# Si la tupla tiene mas elementos que las variables declaradas:
cinco, seis, *resto = tupla2
print(cinco, seis)
print(resto)

# Omitir elementos:
cinco, seis, *_ = tupla2
print(cinco, seis)

# Guardar ciertos datos (omitir elementos):
*_, nueve = tupla2
print(nueve)

# Combinar tuplas o listas (comprimir)
lista = [0, 10, 20, 30, 40]

resultado = zip(tupla, lista) # Devuelve un tipo de dato zip
print(resultado)

resultado = tuple(resultado)
print(resultado)
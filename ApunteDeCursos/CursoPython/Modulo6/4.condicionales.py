''' Clase 3'''

resultado = 10

# Syntax de if:
# if <bool>:
if resultado > 10:
    print('La condicion se cumple')
else:
    print('La condicion no se cumple')


''' Clase 4'''

# Elif
# Nos sirve para evaluar multiples condiciones
calificacion = 8

if calificacion == 10:
    print('Calificacion Perfecta')
elif calificacion <=9 and calificacion >= 8:
    print('Calificacion Aceptable')
elif calificacion <= 7 and calificacion >= 6:
    print('Calificacion Baja')
else:
    print('Calificacion Inefisiente')


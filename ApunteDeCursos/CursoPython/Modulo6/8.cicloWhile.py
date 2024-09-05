''' Clase 7 '''

# Ciclo while
numero = 345722334
contador = 0

while numero >= 1:
    contador += 1

    numero /= 10
else: # Igual podemos usar else en los ciclos
    print('El numero tiene ' + str(contador) + ' digitos')


# print('El numero tiene ' + str(contador) + ' digitos')
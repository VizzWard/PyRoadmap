''' Operadores '''
# Operadores Relacionales

# Mayor que
sentencia = 5 > 3
# Menor que
sentencia = 5 < 3
# Mayor o igual
sentencia = 5 >= 4
# Menor o igual
sentencia = 5 <= 4
# Igual que
sentencia = 5 == 5
# Diferente de
sentencia = 5 != 3


# Operadores logicos
x = 5 ; y = 3

# AND
resultado = (x == 5) and (y == 3)
# OR
resultado = (x < 5) or (y <= 3)
# NOT
resultado = not (x < 5)


# Operador ternario
# Ejemplo 1
x = 5
resultado = "Es mayor que 3" if x > 3 else "Es menor o igual que 3"
print(resultado)  # Output: Es mayor que 3
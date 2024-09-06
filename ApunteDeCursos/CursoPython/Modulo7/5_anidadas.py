''' Clase 9 '''

# Funciones anidada

def operacion(cantidad, balance, tipo='deposito'):

    def ingreso(cantidad, balance):
        return cantidad + balance


    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None

    if tipo == 'deposito':
        return ingreso(cantidad, balance)
    elif tipo == 'retiro':
        return retiro(cantidad, balance)


resultado = operacion(10,30)
print(resultado)

resultado = operacion(10,30, 'retiro')
print(resultado)
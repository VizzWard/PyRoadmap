''' Clase 8 '''
#Scope
animal = 'Leon' # Variable global -> Puedes usarse en cualquier parte del codigo

def imprimir_animal():
    # Esta se tomaria como variable diferente que la de animal
    '''
    animal = 'Gato' # Variable local -> Unicamente puede usarse en el bloque que fue creada.
    print(animal)
    print(id(animal))
    '''

    #Si queremos sobreescribir la variable global usamos
    global animal
    animal = 'Perro'
    print(animal)
    print(id(animal))

imprimir_animal()
print(animal)
print(id(animal))
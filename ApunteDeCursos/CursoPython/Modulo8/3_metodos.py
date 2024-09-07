''' Clase 11 '''

# Metodos de clase (por medio de decoradores)

class Circulo:
    pi = 3.141592

    # Para convertirlo en metodo de clase envez de instancia usamos el decorador
    @classmethod
    def area(cls, radio): # El parametro cls hace referencia a la clase
        return cls.pi * (radio ** 2) # Con cls accedemos al atributo pi de la clase
        # Por ende no es necesario declarar al atributo cls al momento de llamar al metodo.


resultado = Circulo.area(14)
print(resultado)
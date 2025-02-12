class Animal:
    def __init__(self, nombre, especie, sonido=None):
        self.nombre = nombre
        self.especie = especie
        self.sonido = sonido

    def emitir_sonido(self):
        return self.sonido or "Este animal es mudo!"
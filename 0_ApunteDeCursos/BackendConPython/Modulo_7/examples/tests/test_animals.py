import unittest
import json
from ..animals import Animal


class TestBasic(unittest.TestCase):
    def setUp(self):
        self.animales = []
        # Cargar datos de prueba desde el archivo fixtures
        with open("examples/tests/fixtures/animals.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)

        # Crear instancias de animales a partir de los datos de prueba
        for dato in self.data:
            animal = Animal(dato.get("nombre"), dato.get("especie"), dato.get("sonido"))
            self.animales.append(animal)

    def test_sonido_generico(self):
        cocodrillo = self.animales.pop(-1)
        self.assertEqual(cocodrillo.emitir_sonido(), "Este animal es mudo!")

    def test_emitir_sonido(self):
        # elimino el animal con sonido generico
        self.animales.pop(-1)

        # Verificar que todos los animales emiten un sonido
        for animal in self.animales:
            self.assertNotEqual(animal.emitir_sonido(), "Este animal es mudo!")


if __name__ == "__main__":
    unittest.main()
# Que hace test_animals.py?

## 1. Clase TestBasic (Define las pruebas)

```python
class TestBasic(unittest.TestCase):
```
- Hereda de `unittest.TestCase`, lo que permite usar las funciones de prueba de `unittest`.

## 2. Método `setUp()` (Preparación antes de cada test)

```python
    def setUp(self):
        self.animales = []
        # Cargar datos de prueba desde el archivo fixtures
        with open("examples/tests/fixtures/animals.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)

        # Crear instancias de animales a partir de los datos de prueba
        for dato in self.data:
            animal = Animal(dato.get("nombre"), dato.get("especie"), dato.get("sonido"))
            self.animales.append(animal)

```

- Se ejecuta antes de cada prueba (`test_...`).
- Carga los datos de `animals.json` y los guarda en `self.data`.
- Crea objetos `Animal` para cada entrada en `animals.json` y los guarda en `self.animales`.

### Ejemplo de `self.animales` después de `setUp()`

Después de ejecutarse, `self.animales` tendrá una lista de objetos `Animal`, por ejemplo:

```python
[
    Animal("León", "Felino", "Ruge"),
    Animal("Elefante", "Mamífero", "Trompeta"),
    Animal("Cocodrilo", "Reptil", None)  # No tiene sonido
]
```

## 3. `test_sonido_generico()` (Verifica el sonido por defecto)

```python
    def test_sonido_generico(self):
        cocodrillo = self.animales.pop(-1)
        self.assertEqual(cocodrillo.emitir_sonido(), "Este animal es mudo!")
```

- Toma el último animal (Cocodrilo, que no tiene sonido).
- Verifica que emitir_sonido() devuelva "Este animal es mudo!".

Si la clase Animal está bien implementada, este test debería pasar ✅.

## 4. `test_emitir_sonido()` (Verifica que los demás animales tengan sonido)

```python
    def test_emitir_sonido(self):
        # elimino el animal con sonido generico
        self.animales.pop(-1)

        # Verificar que todos los animales emiten un sonido
        for animal in self.animales:
            self.assertNotEqual(animal.emitir_sonido(), "Este animal es mudo!")
```

- Elimina el `Cocodrilo` (que no tiene sonido).
- Verifica que todos los demás animales emiten un sonido diferente de `"Este animal es mudo!"`.

Si algún otro animal no tiene sonido, la prueba fallará ❌.

## 5. Ejecución del Test

Cuando ejecutas:

```commandline
python -m unittest test_animals.py
```

El flujo de ejecución es:

1. `setUp()` se ejecuta antes de cada test.
2. Corre `test_sonido_generico()`:
    - Toma el `Cocodrilo`, verifica que emita `"Este animal es mudo!"`.
3. Corre `test_emitir_sonido()`:
    - Elimina al `Cocodrilo` (el único sin sonido).
    - Verifica que los demás animales emitan un sonido válido.

Si ambos tests pasan, significa que: ✅ Los animales con sonido lo emiten correctamente.
✅ Los animales sin sonido muestran `"Este animal es mudo!"`.
# Que hace test_my_calculations.py?

## 1. **Código Fuente: my_calculations.py**
```python
class Calculations:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return self.a + self.b

    def get_difference(self):
        return self.a - self.b

    def get_product(self):
        return self.a * self.b

    def get_quotient(self):
        return self.a / self.b
```
### **Explicación**
- La clase `Calculations` realiza operaciones matemáticas básicas (suma, resta, multiplicación y división).
- Recibe dos números `a` y `b` en su constructor.
- Cada método devuelve el resultado de la operación correspondiente.

---

## 2. **Pruebas: test_my_calculations.py**
```python
import unittest
from ..my_calculations import Calculations

class TestCalculations(unittest.TestCase):
```
### **1️⃣ setUp() y tearDown()**
```python
    def setUp(self):
        self.calculation = Calculations(8, 2)

    def tearDown(self):
        del self.calculation
```
- `setUp()`: Se ejecuta antes de cada test y crea una instancia de `Calculations(8, 2)`.
- `tearDown()`: Se ejecuta después de cada test y elimina la instancia creada.

### **2️⃣ Test Incorrecto (No se ejecuta como prueba)**
```python
    def not_a_test_sum(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_sum(), 10, "The sum is wrong.")
```
- Este método NO es una prueba porque su nombre no comienza con `test_`.

### **3️⃣ Saltar un Test**
```python
    @unittest.skip("saltando un test")
    def test_nothing(self):
        self.fail("Nada va pasar")
```
- `@unittest.skip("mensaje")`: Omite la ejecución de este test.

### **4️⃣ Prueba de Suma**
```python
    def test_sum(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_sum(), 10.0, "The sum is wrong.")
```
- Comprueba que `get_sum()` devuelve `10.0`.

### **5️⃣ Prueba de Resta**
```python
    def test_diff(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_difference(), 6, "The difference is wrong.")
```
- Verifica que `get_difference()` devuelve `6`.

### **6️⃣ Prueba de Multiplicación**
```python
    def test_product(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_product(), 16, "The product is wrong.")
```
- Verifica que `get_product()` devuelve `16`.

### **7️⃣ Prueba de División**
```python
    def test_quotient(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_quotient(), 4, "The quotient is wrong.")
```
- Verifica que `get_quotient()` devuelve `4`.

### **8️⃣ Prueba Esperada para Fallar**
```python
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "Esto es un error esperado")
```
- `@unittest.expectedFailure`: Marca la prueba como "esperada para fallar".

### **9️⃣ Prueba Omitida**
```python
    @unittest.skip("pendiente ajustar")
    def test_bad_type(self):
        with self.assertRaises(TypeError):
            self.assertEqual(self.calculation.get_quotient(), 4, "The result is not a number.")
```
- `@unittest.skip`: Se omite la prueba con el mensaje "pendiente ajustar".

### **10️⃣ Ejecución de las pruebas**
```python
if __name__ == "__main__":
    unittest.main()
```
- Ejecuta todas las pruebas cuando el archivo se corre directamente.

---

## **3. Resultado Esperado**
Si ejecutamos:
```bash
python -m unittest test_my_calculations.py
```
Podemos esperar:
- ✅ Tests de suma, resta, multiplicación y división pasen.
- ⚠️ `test_nothing` y `test_bad_type` sean omitidos.
- ❌ `test_fail` falle (porque se espera que falle).

---

## **4. Conclusión**
✅ **El test verifica correctamente las operaciones matemáticas.**  
✅ **Incluye pruebas exitosas, omisiones y fallos esperados.**  
✅ **Usa buenas prácticas como `setUp()` y `tearDown()`.**  

---
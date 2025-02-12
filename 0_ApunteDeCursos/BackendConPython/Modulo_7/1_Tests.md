# Introducción a los Tests en Programación

## ¿Qué son los tests?
Los tests en programación son técnicas utilizadas para verificar que el código funcione como se espera. Se utilizan para prevenir errores, mejorar la calidad del software y facilitar el mantenimiento.

## Tipos de tests
Existen diferentes tipos de tests en el desarrollo de software:

1. **Tests Unitarios**: Verifican el correcto funcionamiento de una unidad de código (por ejemplo, una función o un método de una clase) de manera aislada.
2. **Tests de Integración**: Aseguran que diferentes módulos del sistema trabajen correctamente en conjunto.
3. **Tests Funcionales**: Evalúan que el software cumpla con los requisitos funcionales establecidos.
4. **Tests de Sistema**: Verifican el comportamiento del sistema en su totalidad.
5. **Tests de Regresión**: Se usan para asegurarse de que cambios recientes no afecten el comportamiento anterior del software.
6. **Tests de Rendimiento**: Evalúan la velocidad y eficiencia del software bajo diferentes condiciones.
7. **Tests de Aceptación**: Determinan si el software es apto para ser entregado a los usuarios finales.

## ¿Para qué sirve cada tipo de test?
- **Unitarios**: Detectan errores en funciones individuales.
- **Integración**: Identifican fallos en la interacción entre componentes.
- **Funcionales**: Confirman que el sistema cumple con los requisitos del usuario.
- **Sistema**: Evalúan el comportamiento del software completo.
- **Regresión**: Evitan que cambios nuevos rompan funcionalidades previas.
- **Rendimiento**: Miden la velocidad y eficiencia.
- **Aceptación**: Validan que el software sea apto para el usuario final.

## ¿Cómo determinar qué y cuándo hacer un test?
- Se deben hacer tests unitarios cuando se desarrollan funciones críticas o componentes reutilizables.
- Los tests de integración deben aplicarse cuando se conectan módulos entre sí.
- Antes de una entrega, es recomendable realizar tests funcionales, de sistema y de aceptación.
- Los tests de regresión son necesarios tras cada modificación del código.
- Los tests de rendimiento se hacen cuando se espera un alto tráfico o carga en el sistema.

## Pasos para hacer un test unitario
1. **Identificar la funcionalidad a probar.**
2. **Escribir un test que verifique su comportamiento esperado.**
3. **Ejecutar el test y revisar los resultados.**
4. **Corregir el código si el test falla.**
5. **Repetir el proceso hasta que pase exitosamente.**

## Assertions (Aserciones)
Las aserciones son afirmaciones que validan si el resultado de una prueba es el esperado. Ejemplos en `unittest` de Python:

- `assertEqual(a, b)`: Verifica que `a` y `b` sean iguales.
- `assertNotEqual(a, b)`: Verifica que `a` y `b` sean diferentes.
- `assertTrue(x)`: Verifica que `x` sea `True`.
- `assertFalse(x)`: Verifica que `x` sea `False`.
- `assertRaises(Error, func)`: Verifica que `func` lanza el error `Error`.

## Posibles salidas de un test
1. **Éxito (PASSED)**: El test se ejecutó sin errores y la funcionalidad es correcta.
2. **Fallo (FAILED)**: Se encontró un error en la funcionalidad probada.
3. **Error (ERROR)**: Hubo una falla en la ejecución del test mismo.
4. **Saltado (SKIPPED)**: El test fue omitido por alguna condición.
5. **Esperado fallo (EXPECTED FAILURE)**: El test falló pero era el resultado esperado.

## Métodos `setUp` y `tearDown`
Estos métodos se utilizan en `unittest` para preparar y limpiar el entorno antes y después de cada prueba.

- **`setUp`**: Se ejecuta antes de cada test. Se usa para inicializar datos o crear instancias de clases.
  ```python
  def setUp(self):
      self.calculadora = Calculadora(10, 5)
  ```
- **`tearDown`**: Se ejecuta después de cada test. Se usa para limpiar recursos o resetear estados.
  ```python
  def tearDown(self):
      del self.calculadora
  ```
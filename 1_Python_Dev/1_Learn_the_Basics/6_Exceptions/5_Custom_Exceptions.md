# Custom Exceptions

Crear tus propias excepciones en Python te permite definir errores específicos que pueden ocurrir en tu aplicación, lo que mejora la claridad y el control sobre el flujo del programa. A continuación, se detalla cómo hacerlo y los aspectos importantes a considerar.

## ¿Por qué Crear Excepciones Personalizadas?

Las excepciones personalizadas son útiles cuando:

- Necesitas manejar errores específicos que no están cubiertos por las excepciones integradas de Python.
- Quieres proporcionar mensajes de error más claros y significativos para el usuario o desarrollador.
- Deseas encapsular la lógica de manejo de errores en un tipo específico de excepción.

## Cómo Crear Excepciones Personalizadas

Para crear una excepción personalizada, debes definir una nueva clase que herede de la clase base Exception. Aquí tienes un ejemplo básico:

### Ejemplo de Creación de una Excepción Personalizada

```python
class MiExcepcion(Exception):
    """Clase para manejar errores específicos."""
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Uso de la excepción personalizada
def verificar_numero(num):
    if num < 0:
        raise MiExcepcion("El número no puede ser negativo.")
    return num

try:
    verificar_numero(-5)
except MiExcepcion as e:
    print(e)
```

1. Definición de la Clase: `MiExcepcion` hereda de Exception. Esto significa que puedes usarla como cualquier otra excepción en Python.
2. Constructor: El constructor (`__init__`) toma un mensaje que describe el error y lo pasa a la clase base.
3. Uso: En la función `verificar_numero`, se lanza `MiExcepcion` si el número es negativo. En el bloque `try`, se captura y maneja la excepción.

## Mejores Prácticas para Crear Excepciones Personalizadas

1. Nombrar Claramente: Usa nombres descriptivos para tus excepciones personalizadas, indicando claramente qué tipo de error representan.
2. Heredar de `Exception`: Siempre hereda de `Exception` o de una subclase de `Exception`. Esto asegura que tu excepción se comporte como se espera en el sistema de manejo de excepciones de Python.
3. Proporcionar Mensajes Útiles: Asegúrate de que los mensajes que acompañan a tus excepciones sean informativos y ayuden a diagnosticar problemas.
4. Documentar tu Código: Incluye documentación sobre cuándo y por qué lanzar tus excepciones personalizadas, lo que ayudará a otros desarrolladores (o a ti mismo en el futuro) a entender su uso.

## Ejemplo Avanzado con Excepciones Personalizadas

A continuación, se presenta un ejemplo más avanzado que muestra cómo usar excepciones personalizadas en un contexto más amplio:

```python
class EdadInvalidaError(Exception):
    """Excepción lanzada cuando la edad es inválida."""
    def __init__(self, edad):
        self.edad = edad
        self.mensaje = f"La edad {self.edad} no es válida. Debe ser mayor o igual a 18."
        super().__init__(self.mensaje)

def verificar_edad(edad):
    if edad < 18:
        raise EdadInvalidaError(edad)
    return "Edad válida."

try:
    print(verificar_edad(15))
except EdadInvalidaError as e:
    print(e)
```

- Clase `EdadInvalidaError`: Define una excepción personalizada para manejar casos donde la edad es menor a 18 años.
- Función `verificar_edad`: Lanza la excepción personalizada si se proporciona una edad inválida.
- Manejo en `try-except`: Captura y muestra el mensaje personalizado al usuario.
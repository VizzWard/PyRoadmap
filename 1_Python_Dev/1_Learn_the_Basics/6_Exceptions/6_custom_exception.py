# Definición de excepciones personalizadas

class EdadInvalidaError(Exception):
    """Excepción lanzada para errores en la edad ingresada."""
    def __init__(self, edad, mensaje="Edad no válida"):
        self.edad = edad
        self.mensaje = mensaje
        # Llamamos al constructor de la clase padre (Exception)
        super().__init__(self.mensaje)

    def __str__(self):
        # Personalizamos cómo se muestra la excepción cuando se convierte a string
        return f'{self.mensaje}: {self.edad}'

class SaldoInsuficienteError(Exception):
    """Excepción lanzada cuando no hay suficiente saldo en una cuenta."""
    def __init__(self, saldo, monto, mensaje="Saldo insuficiente"):
        self.saldo = saldo
        self.monto = monto
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def __str__(self):
        return f'{self.mensaje}. Saldo actual: {self.saldo}, Monto solicitado: {self.monto}'


# Funciones que utilizan las excepciones personalizadas

def verificar_edad(edad):
    # Verificamos si la edad está fuera del rango considerado válido
    if edad < 0 or edad > 120:
        # Si la edad no es válida, lanzamos nuestra excepción personalizada
        raise EdadInvalidaError(edad)
    print(f"La edad {edad} es válida.")

def realizar_retiro(saldo, monto):
    # Verificamos si hay suficiente saldo para el retiro
    if monto > saldo:
        # Si no hay suficiente saldo, lanzamos nuestra excepción personalizada
        raise SaldoInsuficienteError(saldo, monto)
    nuevo_saldo = saldo - monto
    print(f"Retiro exitoso. Nuevo saldo: {nuevo_saldo}")
    return nuevo_saldo

# Ejemplos de uso de las excepciones

try:
    # Intentamos verificar una edad claramente inválida
    verificar_edad(150)
except EdadInvalidaError as e:
    # Capturamos la excepción y mostramos el mensaje personalizado
    print(e)

try:
    saldo_actual = 1000
    # Intentamos retirar más dinero del disponible
    realizar_retiro(saldo_actual, 1500)
except SaldoInsuficienteError as e:
    # Capturamos la excepción y mostramos el mensaje detallado
    print(e)

# Uso en un contexto más amplio

def procesar_usuario(nombre, edad, saldo):
    try:
        # Primero verificamos la edad
        verificar_edad(edad)
        print(f"Procesando usuario: {nombre}")
        # Luego intentamos realizar un retiro
        realizar_retiro(saldo, 500)
    except EdadInvalidaError as e:
        # Manejamos el caso de edad inválida
        print(f"Error al procesar usuario {nombre}: {e}")
    except SaldoInsuficienteError as e:
        # Manejamos el caso de saldo insuficiente
        print(f"Error al procesar retiro para {nombre}: {e}")
    else:
        # Este bloque se ejecuta si no se lanzó ninguna excepción
        print(f"Usuario {nombre} procesado exitosamente.")
    finally:
        # Este bloque siempre se ejecuta, haya o no excepciones
        print(f"Finalizado el procesamiento de {nombre}")

# Ejemplos de uso de la función procesar_usuario
procesar_usuario("Ana", 25, 1000)    # Caso exitoso
procesar_usuario("Carlos", 150, 200) # Edad inválida
procesar_usuario("Elena", 30, 400)   # Saldo insuficiente
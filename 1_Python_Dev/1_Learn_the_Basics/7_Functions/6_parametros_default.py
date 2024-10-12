# Ejemplos de Argumentos por Defecto en Funciones Python

# 1. Argumento por defecto básico
def saludar(nombre, saludo="Hola"):
    """
    Saluda a una persona con un saludo personalizable.

    :param nombre: str - Nombre de la persona a saludar
    :param saludo: str - Saludo a usar (por defecto "Hola")
    """
    print(f"{saludo}, {nombre}!")


# Uso de la función
saludar("María")  # Usa el saludo por defecto
saludar("Juan", "Bienvenido")  # Usa un saludo personalizado


# 2. Múltiples argumentos por defecto
def crear_perfil(nombre, edad=25, ciudad="Desconocida", hobby="Ninguno"):
    """
    Crea un perfil de usuario con información personalizable.

    :param nombre: str - Nombre del usuario (obligatorio)
    :param edad: int - Edad del usuario (por defecto 25)
    :param ciudad: str - Ciudad del usuario (por defecto "Desconocida")
    :param hobby: str - Hobby del usuario (por defecto "Ninguno")
    """
    perfil = f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}, Hobby: {hobby}"
    print(perfil)


# Uso de la función
crear_perfil("Ana")  # Usa todos los valores por defecto excepto el nombre
crear_perfil("Carlos", 30)  # Especifica nombre y edad, usa valores por defecto para ciudad y hobby
crear_perfil("Elena", ciudad="Madrid")  # Usa argumentos de palabra clave para especificar solo algunos valores
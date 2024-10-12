# 4. Acceso y Manipulación de Elementos
# Ejemplo 1: Acceso y modificación
persona = {"nombre": "Ana", "edad": 28}
print("Edad original:", persona["edad"])
persona["edad"] = 29
print("Edad modificada:", persona["edad"])

# Ejemplo 2: Uso de get() y adición de nuevos elementos
print("Profesión (con get):", persona.get("profesion", "No especificada"))
persona["profesion"] = "Ingeniera"
print("Profesión añadida:", persona["profesion"])
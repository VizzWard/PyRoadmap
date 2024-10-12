# 8. Diccionarios Anidados
# Ejemplo 1: Diccionario de estudiantes
estudiantes = {
    "Juan": {"edad": 20, "carrera": "Informática", "notas": [8, 7, 9]},
    "María": {"edad": 22, "carrera": "Matemáticas", "notas": [9, 8, 10]}
}
print("Carrera de Juan:", estudiantes["Juan"]["carrera"])
print("Segunda nota de María:", estudiantes["María"]["notas"][1])

# Ejemplo 2: Diccionario de ciudades
ciudades = {
    "Nueva York": {
        "país": "Estados Unidos",
        "población": 8419000,
        "lugares_famosos": ["Estatua de la Libertad", "Central Park"]
    },
    "París": {
        "país": "Francia",
        "población": 2161000,
        "lugares_famosos": ["Torre Eiffel", "Louvre"]
    }
}
print("País de París:", ciudades["París"]["país"])
print("Primer lugar famoso de Nueva York:", ciudades["Nueva York"]["lugares_famosos"][0])
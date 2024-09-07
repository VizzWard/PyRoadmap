''' Clase 12 '''

# Callbacks -> pasar funciones como argumentos a otras funciones.
promedio = lambda *args : sum(args) / len(args) # funcion para calcular promedio

aprobado = lambda calificacion : calificacion >= 7 if True else False

def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args) # Ponemos * para desempaquetar la tupla

    if func_aprobatorio(promedio):
        print('Aprobaste -', promedio)
    else:
        print('Reprobado -', promedio)

# Llamada a la función mostrar_mensaje, pasando los callbacks (promedio, aprobado) y las calificaciones
mostrar_mensaje(promedio, aprobado, 10, 9, 8, 10)
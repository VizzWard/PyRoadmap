# 10. Uso Práctico
# Ejemplo 1: Conteo de palabras
texto = "el gato y el perro jugaban el gato se fue"
conteo_palabras = {}
for palabra in texto.split():
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1
print("Conteo de palabras:", conteo_palabras)

# Ejemplo 2: Caché de función (memoización)
def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    resultado = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = resultado
    return resultado

print("Fibonacci de 10:", fibonacci(10))
print("Fibonacci de 20:", fibonacci(20))
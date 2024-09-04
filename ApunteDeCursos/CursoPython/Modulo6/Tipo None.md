# None

`None` es un tipo de dato especial que representa la ausencia de un valor o un valor nulo. Es un objeto único del tipo NoneType, lo que significa que solo hay una instancia de None en todo el programa.

## Características 

1. Representa la Ausencia de Valor: None se utiliza comúnmente para indicar que una variable no tiene valor asignado o que una función no retorna un valor.

```python
resultado = None
```

2. Retorno Predeterminado: Si una función no tiene una declaración return, por defecto retorna None.

```python
def mi_funcion():
    pass

print(mi_funcion())  # Imprime: None
```

3. Comparación con None: Se recomienda comparar None utilizando el operador is en lugar de == para evitar posibles errores.

```python
if resultado is None:
    print("No hay resultado")
```

4. No es Falso ni Verdadero: En una expresión booleana, None se evalúa como False, pero None no es lo mismo que False.

```python
if not None:
    print("None es evaluado como False")
```

5. Uso Común en Inicialización: A menudo, se utiliza None para inicializar variables que se llenarán más tarde con algún valor real.

```python
valor = None
if alguna_condicion():
    valor = 10
```
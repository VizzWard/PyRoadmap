# Ejemplo 2: Operaciones de conjuntos

# Creamos dos sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# Unión de sets
union = set1 | set2  # Alternativa: set1.union(set2)
print("Unión:", union)

# Intersección de sets
interseccion = set1 & set2  # Alternativa: set1.intersection(set2)
print("Intersección:", interseccion)

# Diferencia de sets
diferencia = set1 - set2  # Alternativa: set1.difference(set2)
print("Diferencia (Set1 - Set2):", diferencia)

# Diferencia simétrica
dif_simetrica = set1 ^ set2  # Alternativa: set1.symmetric_difference(set2)
print("Diferencia simétrica:", dif_simetrica)

# Subconjunto
subset1 = {1, 2, 3}
print("¿Es subset1 un subconjunto de set1?", subset1.issubset(set1))

# Superconjunto
print("¿Es set1 un superconjunto de subset1?", set1.issuperset(subset1))

# Conjuntos disjuntos
set3 = {10, 11, 12}
print("¿Son set1 y set3 disjuntos?", set1.isdisjoint(set3))

# Explicación:
# - Los sets en Python soportan operaciones matemáticas de conjuntos.
# - La unión (|) combina elementos de ambos sets sin duplicados.
# - La intersección (&) encuentra elementos comunes en ambos sets.
# - La diferencia (-) encuentra elementos en un set pero no en el otro.
# - La diferencia simétrica (^) encuentra elementos en cualquiera de los sets, pero no en ambos.
# - issubset() verifica si un set es subconjunto de otro.
# - issuperset() verifica si un set es superconjunto de otro.
# - isdisjoint() verifica si dos sets no tienen elementos en común.
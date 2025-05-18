#Práctica 13: Conjuntos

# Conjuntos
conj1 = {1, 2, 3, 4, 5}
print("Conjunto original:", conj1)

conj1.add(6)
print(f"Valor agregado: {conj1}")

conj1.remove(2)  # Error si no se encuentra
print(f"Valor eliminado: {conj1}")

conj1.discard(0)  # No hay error si no se encuentra
print(f"Valor supuestamente eliminado: {conj1}")

print(f"Verificar si 6 existe en el conjunto: {6 in conj1}")  # No repite números

conj1.add(1)  # Ya existe, no lo duplica
print(f"Valor agregado repetido (no cambia): {conj1}")

# Diccionarios
Dic = {'x': "equis", 'y': "ye", 'd': "de"}

print("Valor de 'x':", Dic['x'])  # imprime el valor solo si existe
print("Usando get('x'):", Dic.get('x'))  # funciona igual
print("Usando get('z') (no existe):", Dic.get('z'))  # None

# Modificar y agregar elementos
Dic['x'] = "equis D"  # modifica
Dic['z'] = "zeta"     # agrega nuevo

# Eliminar con del y pop
del Dic['d']
x = Dic.pop('y') 
print("Elemento eliminado con pop:", x)

# Verificar llave
print("¿Existe 'x' en Dic?", 'x' in Dic)

# Llaves, valores y tuplas
llaves = Dic.keys()
print("Llaves:", list(llaves))

valores = Dic.values()
print("Valores:", list(valores))

tuplas = Dic.items()
print("Diccionario como tuplas:", list(tuplas))

# Limpiar el diccionario
Dic.clear()
print("Diccionario después de limpiar:", Dic)

# Reagregar datos y usar update
Dic.update({'w': "dobleu"})
print("Diccionario con update:", Dic)

# Obtener valor con valor por defecto
print("Obtener valor de 'x' (con valor por defecto):", Dic.get('x', "no existe"))

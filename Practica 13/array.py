from numpy import array
import numpy as np

# Paso 1 y 2: listas normales y listas con numpy
lista1 = [1, 2.2, 3.0, "Si", True]
lista2 = np.array([1, 2, 3, 4, 5])

# Paso 3: convertir a tuplas y conjuntos
tupla1 = tuple(lista1)
tupla2 = tuple(lista2)

conj1 = set(lista1)
conj2 = set(lista2)

# Paso 4: diccionario
D = {1: True, 2: 2, 3: "Tres", 4: "Cuatro", 5: "Cinco"}

# Mostrar resultados
print(f"Esta es una lista: {lista1}")
print(f"Esta es una lista con numpy: {lista2}")
print(f"Esta es una tupla: {tupla1}")
print(f"Esta es una tupla con numpy: {tupla2}")
print(f"Este es un conjunto: {conj1}")
print(f"Este es un conjunto con numpy: {conj2}")
print(f"Este es un diccionario: {D}")


# Clase para manejar listas normales
class Lista:
    def __init__(self, datos):
        self.lista = datos

    def insertar(self, valor

#1-.Crear lista de 5 valores mixtos
#2-.Crear lista de 5 valores del mismo tipo con numpy
#3-.Convertir a tuplas y conjuntos las listas anteriores
#4-.Crear un diccionario de 5 elementos con valores de distinto tipo
#Declarar clase arreglos, una clase para lista y otra para numpy
from numpy import array, conj
import numpy as np

lista1= [1,2.2,3.0, "Si", True, 1]
lista2=np.array([1,2,3,4,5,1])

tupla1=tuple(lista1)
tupla2=tuple(lista2)

conj1=set(lista1)
conj2=set(lista2)
 
#{llave:valor}
D={1:True , 2: 2, 3:"Tres", 4:"Cuatro", 5:"Cinco"}

print(f"Esta es una lista{lista1}")
print(f"Esta es una lista con numpy {lista2}")
print(f"Esta es una tupla{tupla1}")
print(f"Esta es una tupla con numpy {tupla2}")
print(f"Este es un conjunto{conj1}")
print(f"Este es un conjunto con numpy{conj2}")
print(f"Este es un diccionario {D}")


#agregar las funciones de lista
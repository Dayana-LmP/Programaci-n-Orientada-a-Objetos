#Práctica 13: Arreglos, listas, conjuntos y diccionarios. 
#1-.Crear lista de 5 valores mixtos
#2-.Crear lista de 5 valores del mismo tipo con numpy
#3-.Convertir a tuplas y conjuntos las listas anteriores
#4-.Crear un diccionario de 5 elementos con valores de distinto tipo
#5-.Declarar clase arreglos y clase lista

from numpy import array, conj
import numpy as np

lista1 = [1, 2.2, 3.0, "Si", True] #Lista de 5 valores mixtos
lista2 = np.array([1, 2, 3, 4, 5, 1]) #Lista valores de mismo tipo, tipo numpy

tupla1 = tuple(lista1) #Convertir lista a tupla
tupla2 = tuple(lista2)

conj1 = set(lista1) #Convertir lista a conjunto
conj2 = set(lista2)

Dic = {1: True, 2: 2, 3: "Tres", 4: "Cuatro", 5: 8.99} #Diccionario con elementos distintos

#Imprimir resultados
print(f"Esta es una lista: {lista1}")
print(f"Esta es una lista con numpy: {lista2}")
print(f"Esta es una tupla: {tupla1}")
print(f"Esta es una tupla con numpy: {tupla2}")
print(f"Este es un conjunto: {conj1}")
print(f"Este es un conjunto con numpy: {conj2}")
print(f"Este es un diccionario: {Dic}")


class Lista: #Clase lista
    def __init__(self):
        self.lista = [1, 2, 3, 4]

    def append(self, valor):
        self.lista.append(valor) 

    def insert(self, indice, valor): #En que posición y valor
        self.lista.insert(indice, valor)

    def extend(self, valores): #agregar varios elementos
        self.lista.extend(valores)

    def index(self, valor): #saber posición
        try:
            print(f"Índice de {valor}: {self.lista.index(valor)}")
        except ValueError:
            print(f"{valor} no se encuentra en la lista.")

    def count(self, valor): #Valores repetidos
        print(f"Cantidad de veces que aparece el número {valor}: {self.lista.count(valor)}")

    def existe(self, valor): #existe en la lista
        print(f"{valor} se encuentra en la lista:", valor in self.lista)

    def modificar(self, indice, nuevo_valor): #modificar valor 
        if 0 <= indice < len(self.lista):
            self.lista[indice] = nuevo_valor
            print(f"Elemento en el índice {indice} modificado a {nuevo_valor}.")
        else:
            print("Índice fuera de rango.")

    def eliminar(self, indice): #Eliminar un elemento
        if 0 <= indice < len(self.lista):
            eliminado = self.lista.pop(indice)
            print(f"Elemento '{eliminado}' en el índice {indice} eliminado.")
        else:
            print("Índice fuera de rango.")


    def mostrar(self): #Muestra la lista
        print("Lista actualizada:", self.lista)


class Arreglo: #Clase arreglo con Numpy
    def __init__(self):
        self.arreglo = np.array([10, 20, 30, 40, 50])

    def insertar(self, indice, valor):
        self.arreglo = np.insert(self.arreglo, indice, valor)

    def modificar(self, indice, valor):
        self.arreglo[indice] = valor

    def eliminar(self, indice):
        self.arreglo = np.delete(self.arreglo, indice)

    def mostrar(self):
        print("Arreglo actualizado:", self.arreglo)


#Probando la clase lista
print()
print("Valores de clase lista")
mi_lista = Lista()
mi_lista.mostrar()
mi_lista.append(5)
mi_lista.insert(0, 0)
mi_lista.extend([6, 7, 8])
mi_lista.mostrar()
mi_lista.index(3)
mi_lista.count(2)
mi_lista.existe(4)
mi_lista.existe(10)

#Probando la clase Arreglo
print()
print("Valores de clase arreglos")
arr = Arreglo()
arr.mostrar()
arr.insertar(2, 25) #25 en la posición 2
arr.mostrar()
arr.modificar(1, 15) #15 en la posición 1
arr.mostrar()
arr.eliminar(3) #valor en lugar 3
arr.mostrar()

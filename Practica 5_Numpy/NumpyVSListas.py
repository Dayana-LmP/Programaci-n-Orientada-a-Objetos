#Práctica 5: Manejo de paquetes Numpy
#Utilizar Numpy y listas, con las mismas funciones cada una.
from numpy import array
import numpy as np

#Clase que usa arreglos con paquetes Numpy
class Arreglo:
    def inicializar(self, V):
        self.arregloNP = np.array(V)

    def insertar(self, i, V):
        self.arregloNP = np.insert(self.arregloNP, i, V)

    def eliminar(self, i):
        self.arregloNP = np.delete(self.arregloNP, i)

    def modificar(self, i, V):
        self.arregloNP[i] = V

    def mostrar(self):
        print("Arreglo:", self.arregloNP)

#Clase que utiliza listas, no Numpy
class Lista:
    def inicializar(self, V):
        self.arregloList = list(V)

    def insertar(self, i, V):
        self.arregloList.insert(i, V)

    def eliminar(self, i):
        self.arregloList.pop(i)

    def modificar(self, i, V):
        self.arregloList[i] = V

    def mostrar(self):
        print("Lista:", self.arregloList)

#Mostrar como se utilizan
#Numpy
print("Uso de paquetes Numpy")
arr = Arreglo()
arr.inicializar([1, 2, 3, 4])
arr.mostrar()

arr.insertar(2, 99)
arr.mostrar()

arr.eliminar(1)
arr.mostrar()

arr.modificar(0, 77)
arr.mostrar()

print() #Espacio
#Listas
print("Uso de listas")
lis = Lista()
lis.inicializar([10, 20, 30, 40])
lis.mostrar()

lis.insertar(2, 88)
lis.mostrar()

lis.eliminar(1)
lis.mostrar()

lis.modificar(0, 100)
lis.mostrar()

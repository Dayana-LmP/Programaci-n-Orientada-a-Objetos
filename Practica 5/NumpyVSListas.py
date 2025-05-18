#Declarar clase arreglos, una clase para lista y otra para numpy
from numpy import array
import numpy as np

# Clase que usa arreglos con NumPy
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
        print("Arreglo (NumPy):", self.arregloNP)

# Clase que usa listas de Python
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
        print("Lista (Python):", self.arregloList)

# Ejemplo de uso
print("Utilizando NumPy")
arr = Arreglo()
arr.inicializar([1, 2, 3, 4])
arr.mostrar()

arr.insertar(2, 99)
arr.mostrar()

arr.eliminar(1)
arr.mostrar()

arr.modificar(0, 77)
arr.mostrar()

print("Utilizando Listas de Python")
lis = Lista()
lis.inicializar([10, 20, 30, 40])
lis.mostrar()

lis.insertar(2, 88)
lis.mostrar()

lis.eliminar(1)
lis.mostrar()

lis.modificar(0, 100)
lis.mostrar()

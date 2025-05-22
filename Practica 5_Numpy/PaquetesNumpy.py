#Práctica 5: Manejo de paquetes Numpy
#Declarar clase arreglos, una clase para lista y otra para numpy
from numpy import array
import numpy as np

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
        print(self.arregloNP)

# Ejemplo de uso
arreglo = Arreglo()

# Inicializar
arreglo.inicializar([0, 1, 2, 3, 4])
print("Arreglo original:")
arreglo.mostrar()

# Insertar
print("Función Insertar: insertar 5 en la posición 2:")
arreglo.insertar(2, 5)
arreglo.mostrar()

# Eliminar
print("Función Eliminar: eliminar elemento en la posición 3:")
arreglo.eliminar(3)
arreglo.mostrar()

# Modificar
print("Función Modificar: modificar elemento en la posición 1 a 7:")
arreglo.modificar(1, 7)
arreglo.mostrar()

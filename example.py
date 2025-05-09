from numpy import array
import numpy as np

class Arreglo:
    def inicializar(self, V):
        self.arregloNP = np.array(V)
    
    def insertar(self, i, V):
        self.arregloNP = np.insert(self.arregloNP, i, V)
    
    def mostrar(self):
        print(self.arregloNP)

# Ejemplo de insertar
arreglo = Arreglo()
arreglo.inicializar([0, 1, 2, 3, 4])
print("Insertar:")
arreglo.insertar(2, 5) 
arreglo.mostrar()


class Arreglo:
    def inicializar(self, V):
        self.arregloNP = np.array(V)
    
    def eliminar(self, i):
        self.arregloNP = np.delete(self.arregloNP, i)
    
    def mostrar(self):
        print(self.arregloNP)

arreglo = Arreglo()
arreglo.inicializar([0, 1, 2, 3, 4])
print("Eliminar:")
arreglo.eliminar(3) 
arreglo.mostrar()

class Arreglo:
    def inicializar(self, V):
        self.arregloNP = np.array(V)
    
    def modificar(self, i, V):
        self.arregloNP[i] = V
    
    def mostrar(self):
        print(self.arregloNP)


arreglo = Arreglo()
arreglo.inicializar([0, 1, 2, 3, 4])
print("Modificar:")
arreglo.modificar(1, 7)  # Modifica el valor en la posición 1 a 99
arreglo.mostrar()

      


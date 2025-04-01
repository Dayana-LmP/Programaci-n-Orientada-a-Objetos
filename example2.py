<<<<<<< HEAD
from numpy import array
import numpy as np
#listas
class Lista:
    def __init__(self):
        self.lista = [0, 1, 2, 3]

    def insertar(self):
            elemento = int(input("Insertar número: "))
            self.lista.append(elemento)

    def mostrar(self):
        print("Lista actual:", self.lista)

mi_lista = Lista()
mi_lista.mostrar()
mi_lista.insertar()
mi_lista.mostrar()


class Lista:
    def __init__(self):
        self.lista = [0, 1, 2, 3]

    def modificar(self):
            i = int(input(f"Ingresa el número a modificar (0 a {len(self.lista)-1}): "))
            if 0 <= i < len(self.lista):
                nuevo_elemento = int(input("Ingresa el nuevo valor para este elemento: "))
                self.lista[i] = nuevo_elemento
            else:
                print("Índice fuera de rango.")

    def mostrar(self):
        print("Lista actual:", self.lista)

mi_lista = Lista()
mi_lista.mostrar() 
mi_lista.modificar()
mi_lista.mostrar()  

class Lista:
    def __init__(self):
        self.lista = [0, 1, 2, 3]

    def eliminar(self):
            i = int(input(f"Ingresa el número a eliminar (0 a {len(self.lista)-1}): "))
            if 0 <= i < len(self.lista):
                self.lista.pop(i)
                print(f"Elemento en el índice {i} eliminado.")
            else:
                print("Índice fuera de rango.")
       
    def mostrar(self):
        print("Lista actual:", self.lista)

mi_lista = Lista()
mi_lista.mostrar()  
mi_lista.eliminar()
mi_lista.mostrar()

#Arreglos
class Arreglo:
    def inicializar(self, V):
        self.arregloNP = np.array(V)
    
    def insertar(self, i, V):
        self.arregloNP = np.insert(self.arregloNP, i, V)
    
    def mostrar(self):
        print(self.arregloNP)


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
arreglo.modificar(1, 7)  
=======
from numpy import array
import numpy as np
#listas
class Lista:
    def __init__(self):
        self.lista = [0, 1, 2, 3]

    def insertar(self):
            elemento = int(input("Insertar número: "))
            self.lista.append(elemento)

    def mostrar(self):
        print("Lista actual:", self.lista)

mi_lista = Lista()
mi_lista.mostrar()
mi_lista.insertar()
mi_lista.mostrar()


class Lista:
    def __init__(self):
        self.lista = [0, 1, 2, 3]

    def modificar(self):
            i = int(input(f"Ingresa el número a modificar (0 a {len(self.lista)-1}): "))
            if 0 <= i < len(self.lista):
                nuevo_elemento = int(input("Ingresa el nuevo valor para este elemento: "))
                self.lista[i] = nuevo_elemento
            else:
                print("Índice fuera de rango.")

    def mostrar(self):
        print("Lista actual:", self.lista)

mi_lista = Lista()
mi_lista.mostrar() 
mi_lista.modificar()
mi_lista.mostrar()  

class Lista:
    def __init__(self):
        self.lista = [0, 1, 2, 3]

    def eliminar(self):
            i = int(input(f"Ingresa el número a eliminar (0 a {len(self.lista)-1}): "))
            if 0 <= i < len(self.lista):
                self.lista.pop(i)
                print(f"Elemento en el índice {i} eliminado.")
            else:
                print("Índice fuera de rango.")
       
    def mostrar(self):
        print("Lista actual:", self.lista)

mi_lista = Lista()
mi_lista.mostrar()  
mi_lista.eliminar()
mi_lista.mostrar()

#Arreglos
class Arreglo:
    def inicializar(self, V):
        self.arregloNP = np.array(V)
    
    def insertar(self, i, V):
        self.arregloNP = np.insert(self.arregloNP, i, V)
    
    def mostrar(self):
        print(self.arregloNP)


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
arreglo.modificar(1, 7)  
>>>>>>> 27614648ad4b5f4a0ff3c24a79e3179f9f5714a4
arreglo.mostrar()
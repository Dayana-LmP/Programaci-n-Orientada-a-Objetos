
import numpy as np

# Clase para manejar listas
class Lista:
    def __init__(self):
        self.lista = [0, 1, 2, 3]

    def insertar(self):
        elemento = int(input("Insertar número: "))
        self.lista.append(elemento)

    def modificar(self):
        i = int(input(f"Índice a modificar (0 a {len(self.lista)-1}): "))
        if 0 <= i < len(self.lista):
            nuevo_elemento = int(input("Nuevo valor: "))
            self.lista[i] = nuevo_elemento
        else:
            print("Índice fuera de rango.")

    def eliminar(self):
        i = int(input(f"Índice a eliminar (0 a {len(self.lista)-1}): "))
        if 0 <= i < len(self.lista):
            self.lista.pop(i)
            print(f"Elemento en índice {i} eliminado.")
        else:
            print("Índice fuera de rango.")

    def mostrar(self):
        print("Lista actual:", self.lista)


# Clase para manejar arreglos con NumPy
class Arreglo:
    def __init__(self):
        self.arregloNP = np.array([0, 1, 2, 3, 4])

    def insertar(self, i, V):
        self.arregloNP = np.insert(self.arregloNP, i, V)

    def modificar(self, i, V):
        if 0 <= i < len(self.arregloNP):
            self.arregloNP[i] = V
        else:
            print("Índice fuera de rango.")

    def eliminar(self, i):
        if 0 <= i < len(self.arregloNP):
            self.arregloNP = np.delete(self.arregloNP, i)
        else:
            print("Índice fuera de rango.")

    def mostrar(self):
        print("Arreglo actual:", self.arregloNP)


# === DEMOSTRACIÓN ===
# Lista
mi_lista = Lista()
mi_lista.mostrar()
mi_lista.insertar()
mi_lista.modificar()
mi_lista.eliminar()
mi_lista.mostrar()

# Arreglo NumPy
arreglo = Arreglo()
arreglo.mostrar()
print("Insertar en arreglo:")
arreglo.insertar(2, 5)
arreglo.mostrar()
print("Modificar en arreglo:")
arreglo.modificar(1, 7)
arreglo.mostrar()
print("Eliminar en arreglo:")
arreglo.eliminar(3)
arreglo.mostrar()

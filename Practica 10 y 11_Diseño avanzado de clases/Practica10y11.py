#Práctica 10 y 11: Diseño avanzado de clases (Abstracción)
#Abstracción
from math import pi
from abc import ABC, abstractmethod

class Figura(ABC): #Clase abstracta
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Figura): #Clase concreta
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return pi * self.radio **2
    

class Rectangulo(Figura): #Clase concreta
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura

#Crear objeto e imprimir resultados
circulo = Circulo(5)
rectangulo = Rectangulo(4, 5)

#print(f"Área del círculo: {circulo.calcular_area()}") Mostrar decimales normales
print(f"Área del círculo: {circulo.calcular_area():.2f}") #Solo mostrar dos decimales
print(f"Área del rectángulo: {rectangulo.calcular_area()}")

   

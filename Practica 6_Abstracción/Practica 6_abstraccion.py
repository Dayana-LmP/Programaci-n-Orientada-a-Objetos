#Práctica 6 abstracción
#Calcular área del cuadrado y triángulo

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC): #Clase abstracta
    @abstractmethod
    def calcular_area(self):
        pass

class Cuadrado(FiguraGeometrica): #Subclase cuadrado
    def __init__(self, lado):
        self.lado = lado
    def calcular_area(self):
        return self.lado * self.lado
    
class Triangulo(FiguraGeometrica): #Subclase triángulo
    def __init__(self, base, altura): 
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return ((self.base * self.altura)/2)
    
#Crear el objetos e imprimir área
cuadrado = Cuadrado(4)
print(f"El área del cuadrado es: {cuadrado.calcular_area()}")

triangulo = Triangulo(4, 5)
print(f"El área del triángulo es: {triangulo.calcular_area()}")
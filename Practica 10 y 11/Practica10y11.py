#Práctica 10 y 11: Diseño avanzado de clasas
#Abstracción
from math import pi
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self, radio):
        area = pi*radio**2
        return area

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self, base, altura):
        area = base* altura
        return area  

   

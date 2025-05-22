#Práctica 6: Abstracción
#Abstracción dando el valor del lado, la base y la altura.
#Calcular área del cuadrado y el rectángulo.
from abc import ABC, abstractmethod

class Figura(ABC): 
    @abstractmethod
    def area(self):
        pass 

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return (self.lado * self.lado)
    
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura)

#Abstracción, crear objeto e imprimir resultado
cuadrado = Cuadrado(6) #Valor del lado
print(f"El área del cuadrado es: {cuadrado.area()}")  #Implementar el método abstracto
rectangulo = Rectangulo(5,6) #Valor de la base, altura
print(f"El área del rectángulo es: {rectangulo.area()}")
#Práctica 6-Método abstracto en python.

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
#Método concreto (con implementación)
    def respirar(self):
        print(f"{self.nombre} está ladrando...")
#Método abstracto (sin implementación)
    @abstractmethod
    def hacer_sonido(self):
        pass
#Otro método abstracto
    @abstractmethod
    def moverse(self):
        pass

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
#Implementación del método abstracto
    def hacer_sonido(self):
        return "¡Woof! ¡Woof!"
#Implementación del método abstracto
    def moverse(self):
        print(f"{self.nombre} corre en el parque")
#Uso
#animal = Animal("Genérico") #Error: No se puede instanciar una clase abstracta
perro = Perro("Rookie", "Poodle")
perro.respirar()
print(perro.hacer_sonido())
perro.moverse()
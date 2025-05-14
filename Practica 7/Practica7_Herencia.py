#Práctica 7: Herencia de atributos y métodos

class Animal:
    def __init__(self, tipoAnimal):
        self.tipoAnimal = tipoAnimal

    def hacer_sonido(self):
        print("El animal hace un sonido.")
    
class Perro(Animal):
    def __init__(self, tipoAnimal):
        super().__init__(tipoAnimal)

    def hacer_sonido(self):
        print(f" {self.tipoAnimal} ¡Guau!")

class Gato(Animal):
    def __init__(self, tipoAnimal):
        super().__init__(tipoAnimal)

    def hacer_sonido(self):
        print(f" {self.tipoAnimal} ¡Miau!")

class Gallo(Animal):
    def __init__(self, tipoAnimal):
        super().__init__(tipoAnimal)

    def hacer_sonido(self):
        print(f" {self.tipoAnimal} ¡Kikirikikiriki!")
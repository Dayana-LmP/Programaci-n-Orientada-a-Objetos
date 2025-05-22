#Práctica 7: Herencia simple en python.
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        return "Algún sonido genérico"
    
    def presentarse(self):
        return f"Soy {self.nombre} y tengo {self.edad} años"

class Perro(Animal): #La clase Perro hereda de la clase Animal
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad) #Llama al constructor de la clase padre
        self.raza = raza
        
    def hacer_sonido(self): #Sobrescribe el método de la clase padre
        return "¡Woof! ¡Woof!"
    
    def presentarse(self):
        return super().presentarse() + f" y soy un perro de raza {self.raza}"

#Crear objeto e imprimir resultado
perro = Perro("Bodoque", 11, "Schnauzer")
print(perro.presentarse()) #Uso método extendido
print(perro.hacer_sonido()) #Uso método sobrescrito
#Práctica 8: Polimorfismo

class Animal:
    def __init__(self, tipoAnimal): #constructor
        self.tipoAnimal = tipoAnimal 

    def hacer_sonido(self):
        pass
    
class Perro(Animal):
    def __init__(self, tipoAnimal ="Perro"):
        super().__init__(tipoAnimal) #Llama al contructor de la clase Animal

    def hacer_sonido(self): #De la clase padre
        print("¡Guau!") #Comportamiento que se quiere

class Gato(Animal):
    def __init__(self, tipoAnimal = "Gato"):
        super().__init__(tipoAnimal)

    def hacer_sonido(self):
        print("¡Miau!")

class Gallo(Animal):
    def __init__(self, tipoAnimal = "Gallo"):
        super().__init__(tipoAnimal)

    def hacer_sonido(self):
        print("¡Kikirikikiriki!")
    
def escucharMascota(animal): 
        animal.hacer_sonido() #llama a hacer_sonido 
    
if __name__ == '__main__': # el código dentro de él solo se ejecute 
    #cuando el script se ejecuta directamente
    perro = Perro() #Instancia de la clase perro
    gato = Gato()
    gallo = Gallo()
    escucharMascota(perro) #llama a la función escucharMascota, pasando el objeto perro
    escucharMascota(gato)
    escucharMascota(gallo)

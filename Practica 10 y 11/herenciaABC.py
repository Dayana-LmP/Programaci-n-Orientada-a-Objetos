#Herecia múltiple ABC

from abc import ABC, abstractmethod
class Vehiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

class Electrico(ABC):
    @abstractmethod
    def cargar(self):
        pass

class CocheElectrico(Vehiculo, Electrico):
    def mover(self):
        return "Moviendo coche eléctrico, cuchau"
    
    def cargar(self):
        return "Cargando batería..."
    
#Instancia de la clase CocheElectrico
coche = CocheElectrico()

# Método mover() 
mensajeMovimiento = coche.mover()
print(mensajeMovimiento)

# Método cargar()
mensajeCarga = coche.cargar()
print(mensajeCarga)
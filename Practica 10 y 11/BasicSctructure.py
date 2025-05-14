#Estructura básica, pasos:
#1-.Crear una clase abstracta
#2-.Definir dos interfaces
#3.Implementar tres clases concretas
#4-.Crear sistema polimórfico

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def detener(self):
        pass

    @abstractmethod
    def velocidad_maxima(self):
        pass

class Conducible(ABC):
    @abstractmethod
    def conducir(self):
        pass

    @abstractmethod
    def estacionar(self):
        pass

class Mantenible(ABC):
    @abstractmethod
    def revisar(self):
        pass
   
    @abstractmethod
    def reparar(self):
        pass

class Coche(Vehiculo, Conducible, Mantenible):
    def mover(self):
        return "El coche está en movimiento. Rum Rum"

    def detener(self):
        return "El coche se ha detenido. :( )"

    def velocidad_maxima(self):
        return "La velocidad máxima del coche es de 200 km/h."

    def conducir(self):
        return "Conduciendo el coche. ;)"

    def estacionar(self):
        return "El coche ha sido estacionado."

    def revisar(self):
        return "Se ha realizado la revisión del coche."

    def reparar(self):
        return "El coche ha sido reparado."

# Crear una instancia de la clase Coche
mi_coche = Coche()

# Llamar a uno de los métodos e imprimir el resultado
resultadoMovimiento = mi_coche.mover()
print(resultadoMovimiento)

resultadoRevision = mi_coche.revisar()
print(resultadoRevision)

resultadoVelocidad = mi_coche.velocidad_maxima()
print(resultadoVelocidad)
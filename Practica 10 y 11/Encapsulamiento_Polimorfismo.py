#Diseño avanzado de clases Polimorfismo y encapsulamiento
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca  # Atributo privado
        self._modelo = modelo # Atributo privado

    def obtener_marca(self):
        return self._marca

    def obtener_modelo(self):
        return self._modelo

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass

class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad_actual=0):
        super().__init__(marca, modelo)
        self._velocidad_actual = velocidad_actual  # Atributo privado

    def acelerar(self):
        self._velocidad_actual += 100
        return f"El coche {self._marca} {self._modelo} acelera a {self._velocidad_actual} km/h."

    def frenar(self):
        if self._velocidad_actual > 0:
            self._velocidad_actual -= 10
            return f"El coche {self._marca} {self._modelo} frena a {self._velocidad_actual} km/h."
        else:
            return f"El coche {self._marca} {self._modelo} ya está detenido."

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_actual=0):
        super().__init__(marca, modelo)
        self._velocidad_actual = velocidad_actual

    def acelerar(self):
        self._velocidad_actual += 20
        return f"La bicicleta {self._marca} {self._modelo} acelera a {self._velocidad_actual} km/h."

    def frenar(self):
        if self._velocidad_actual > 0:
            self._velocidad_actual -= 2
            return f"La bicicleta {self._marca} {self._modelo} frena a {self._velocidad_actual} km/h."
        else:
            return f"La bicicleta {self._marca} {self._modelo} ya está detenida."

# Polimorfismo 
def probar_vehiculo(vehiculo):
    print(vehiculo.acelerar())
    print(vehiculo.frenar())
    print(f"Marca: {vehiculo.obtener_marca()}, Modelo: {vehiculo.obtener_modelo()}")
    

mi_coche = Coche("Cupra", "Formentor")
mi_bicicleta = Bicicleta("Specialized", "Mountain Bike")

probar_vehiculo(mi_coche)
probar_vehiculo(mi_bicicleta)
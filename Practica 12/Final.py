#Final
from typing import Final

class Vehiculo:
    # Usamos Final para declarar constantes
    MAX_VELOCIDAD: Final = 200  # No se debe cambiar el valor de MAX_VELOCIDAD
    
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_actual = 0
    
    def acelerar(self, incremento: int):
        if self.velocidad_actual + incremento <= Vehiculo.MAX_VELOCIDAD:
            self.velocidad_actual += incremento
            print(f"Acelerando: velocidad actual es {self.velocidad_actual} km/h")
        else:
            print(f"No se puede acelerar más allá de {Vehiculo.MAX_VELOCIDAD} km/h")

    def frenar(self):
        self.velocidad_actual = 0
        print("El vehículo ha frenado a 0 km/h.")
    
    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Velocidad actual: {self.velocidad_actual} km/h")
        print(f"Velocidad máxima permitida: {Vehiculo.MAX_VELOCIDAD} km/h")

# Crear una instancia de Vehiculo
auto = Vehiculo("Ford", "Focus")
auto.mostrar_info()

# Intentamos acelerar el vehículo
auto.acelerar(150)
auto.acelerar(60)  # Esto debería mostrar un mensaje de error porque excede el límite
auto.frenar()
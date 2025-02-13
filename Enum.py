from enum import Enum

# Definimos un Enum para los días de la semana
class DiaDeLaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

# Usamos el Enum en una función que muestra si es día de trabajo o fin de semana
def es_dia_de_trabajo(dia):
    if dia in [DiaDeLaSemana.LUNES, DiaDeLaSemana.MARTES, DiaDeLaSemana.MIERCOLES, DiaDeLaSemana.JUEVES, DiaDeLaSemana.VIERNES]:
        return "Es día de trabajo."
    elif dia in [DiaDeLaSemana.SABADO, DiaDeLaSemana.DOMINGO]:
        return "Es fin de semana."
    else:
        return "Día no válido."

# Ejemplo de uso
dia_actual = DiaDeLaSemana.MARTES
print(f"Hoy es {dia_actual.name} ({dia_actual.value}). {es_dia_de_trabajo(dia_actual)}")

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

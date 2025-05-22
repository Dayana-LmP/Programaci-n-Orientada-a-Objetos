#Práctica 7: Herencia múltiple en python

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def informacion(self):
        return f"Vehículo {self.marca} {self.modelo}"

class Electrico:
    def __init__(self, autonomia):
        self.autonomia = autonomia
    
    def cargar(self):
            return "Cargando batería..."

class CocheElectrico(Vehiculo, Electrico):
    def __init__(self, marca, modelo, autonomia):
        Vehiculo.__init__(self, marca, modelo)
        Electrico.__init__(self, autonomia)
    
    def informacion(self):
            return f"{Vehiculo.informacion(self)} - Autonomía: {self.autonomia} km"
# Uso
BYD = CocheElectrico("BYD", "Mini Dolphin", 450)
print(BYD.informacion())
print(BYD.cargar())
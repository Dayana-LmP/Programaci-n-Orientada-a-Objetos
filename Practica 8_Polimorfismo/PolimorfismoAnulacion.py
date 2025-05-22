#Práctica 8: Polimorfismo de anulación python

class Forma:
    def dibujar(self):
        return "Dibujar una figura"
    
    def area(self):
        return "Calcular área de forma genérica"

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
        
    def dibujar(self): # Sobrescribe el método de la clase base
        return "Dibujando un círculo..."
    
    def area(self): # Sobrescribe y especializa el cálculo
        return 3.14159 * self.radio * self.radio

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    def dibujar(self): # Otra implementación del mismo método
        return "Dibujando un rectángulo"
    
    def area(self):
        return self.ancho * self.alto
# Uso polimórfico
def procesar_forma(forma):
        print(forma.dibujar())
        print(f"Área: {forma.area()}")
        
# Diferentes objetos responden de manera específica
procesar_forma(Circulo(5))
procesar_forma(Rectangulo(4, 6))
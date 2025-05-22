#Práctica 8: Polimorfismo de anulación python

class Forma:
    def dibujar(self):
        return "Dibujar una figura"
    
    def area(self):
        return "Calcular área de forma genérica"

class Rombo(Forma):
    def __init__(self, diagonalMayor, diagonalMenor):
        self.diagonalMayor = diagonalMayor
        self.diagonalMenor = diagonalMenor

    def dibujar(self): #Sobrescribe el método de la clase base
        return "Dibujando un rombo..."
    
    def area(self): #Sobrescribe y especializa el cálculo
        return ((self.diagonalMayor * self.diagonalMenor)/2)

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
        
    def dibujar(self): #Otra implementación del mismo método
        return "Dibujando un cuadrado..."
    
    def area(self):
        return self.lado * 4
#Uso del polimorfismo
def procesar_forma(forma):
        print(forma.dibujar())
        print(f"Área: {forma.area()}")

#Diferentes objetos responden de manera específica
procesar_forma(Rombo(8, 6))
procesar_forma(Cuadrado(5))
from math import *

class Figura:
    def perimetro(L, NL):
        perimetro = L * NL
        return perimetro

    def area(L, NL):
        if NL == 3:
            altura = int(input("Ingresa el valor de la altura: "))
            area = (L * altura) / 2
            return area
        elif NL == 4 & L == 4:
            area = L * L
            return area
        elif NL == 4:
            altura = int(input("Ingresa el valor de la altura: "))
            area = L * altura
            return area
        elif NL == 5:
            apotema = int(input("Ingresa el valor del apotema: "))
            area = (L * 5 * apotema) / 2
            return area
        else:
            return "inválida. Solo de 3 a 5 lados"


print("Introduce el número de lados")
NL = int(input())
print("Introduce el valor del lado")
L = int(input())

print(f"El área es: {Figura.area(L, NL)} cm2") #Imprime el valor del área
print(f"El perímetro es: {Figura.perimetro(L, NL)} cm") #Imprime el valor del perímetro

#print(f"El área es: {Figura.area(L, NL)} cm2") #Imprime el valor del área


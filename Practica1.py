
from math import *

class Figura:
    def perimetro(L, NL):
        perimetro = L * NL
        return perimetro
    
    def area(L, NL):
        if NL == 3:
            a = ((sqrt(3))/4)*(L**2)
        elif NL == 4:
            a = L * L  
        elif NL == 5:
            a = (L ** 2 * sqrt(5 * (5 + 2 * sqrt(5)))) / 4  
        else:
              a=((NL*L*L)/(4*(tan(pi/NL))))
        return a


print("Introduce el número de lados")
NL = int(input())  
print("Introduce el valor del lado")
L = float(input())  


print("El perímetro es:"  , Figura.perimetro(L, NL), " cm")

from math import *

class Figura:
    def perimetro(L, NL):
        perimetro = L * NL
        return perimetro
    
    def area(L, NL):
        if NL == 3:
            a = ((sqrt(3))/4)*(L**2)
        elif NL == 4:
            a = L * L  
        elif NL == 5:
            a = (L ** 2 * sqrt(5 * (5 + 2 * sqrt(5)))) / 4  
        else:
              a=((NL*L*L)/(4*(tan(pi/NL))))
        return a


print("Introduce el número de lados")
NL = int(input())  
print("Introduce el valor del lado")
L = float(input())  


print("El perímetro es:"  , Figura.perimetro(L, NL), " cm")
print("El área es:" , Figura.area(L, NL), " cm2")
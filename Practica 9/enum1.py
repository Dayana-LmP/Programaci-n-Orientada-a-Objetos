#Enum 
from enum import Enum
class Consecutivo(Enum): #clase que va a tener enum
    Lunes=1 #enumeración
    Martes=2
    Miercoles=3

print(Consecutivo.Lunes)  #número de la numeración
print(Consecutivo.Lunes.value)
print(type(Consecutivo.Lunes)) #Tipo de dato
print(type(Consecutivo.Lunes.value))
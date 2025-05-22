#Práctica 4: Encapsulamiento
class Persona:
    def __init__(self, nombre, edad): 
        self.__nombre = nombre  #Es un atributo privado
        self.__edad = edad  
    
    def get_nombre(self):  #Acceder a nombre
        return self.__nombre
    
    def get_edad(self):  #Acceder a edad 
        return self.__edad 
    
    def set_edad(self, nuevaEdad): #modificar edad
        if nuevaEdad > 0:
            self.__edad = nuevaEdad
    

persona = Persona("Alfonso", 21)#Encapsulamiento
print(persona.get_nombre())  #Se accede al nombre, método público
print(persona.get_edad()) #Se accede a la edad

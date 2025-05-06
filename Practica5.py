#Declarar clase arreglos, una clase para lista y otra para numpy
from numpy import array
import numpy as np


class Arreglo:
#numpy
    def inicializar(self, V):
        self.arregloNP=np.array([1,2,3,4])
    np.array([1,2,3,4])
#insertar
    def insertar(self, i,V):
      self.arregloNP.insert(self.arregloNP, i, V)
 #eliminar    
    def eliminar(self,i): #i=indice
       self.arregloNP.delete(i)

 #modificar   
    def modificar(self,i,V):
       self.arregloNP[i]=V

class Lista:
#Listas
   def inicializar(self, V):
      self.arregloList=[]
#insertar
   def insertar(self, V):
      self.arregloList.append(V)

#eliminar
   def eliminar(self,i):
      self.arregloList.pop(i)
      
#modificar
   def modificar(self,i,V):
      self.arregloList[i]=V
    


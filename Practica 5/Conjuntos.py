from numpy import conj

conj1={1,2,3,4,5}
print(conj1)
conj1.add(6)
print(f"Valor agregado {conj1}")
conj1.remove(2) #Error si no se encuentra
print(f"Valor eliminado {conj1}")
conj1.discard(0) #No hay error si no se encuentra
print(f"Valor supuestamente eliminado {conj1}")
print(f"Verificar si 6 existe en el conjunto: {6 in conj1}") #No repite números
conj1.add(1)
print(f"Valor agregado repetido {conj1}")

#Diccionarios
#Dic={'x':"equis", 'y':"ye", 'd':"de"}
#print(Dic['x']) #imprime el valor solo si existe
#print(Dic.get['x']) #Si existe lo imprime, si no, lo ignora
#print(Dic.get('z')) #None
#Dic['x']="equis D" #modifica
#Dic['z']="zeta" #Si no encuentra el valor, lo agrega
#del Dic['y'] #Elimina
#x = Dic.pop('y') 
#print(x) #"ye"

#Verificar si se encuentra un valor dentro del diccionario
#print('x' in Dic) #True

#Obtener todas las llaves dentro de un diccionario
#llaves = Dic.keys()
#print(llaves) #['x', 'y', 'd']

#Obtener todos los valores dentro de un diccionario
#Valores = Dic.values()

#Regresa el diccionario convertido en tuplas
#p = Dic.items() #('x', "equis"), dict_items( [(,),(,)]

#Para limpiar el diccionarios
#Dic.clear()

#Agregar o modificar elementos existentes
#Dic.update({'w':"dobleu"})

#Obten el valor cuando sea igual a n:x
#Dic.get('x', "equis")

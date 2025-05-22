#Práctica 13: Arreglos, listas, conjuntos y diccionarios. 
# Diccionarios

# Diccionario original
Dic = {'x': "equis", 'y' : "ye", 'd' : "de"}

print("Valor de 'x': ", Dic['x']) #Imprimir el valor de x si esta existe en el dic

print("Usando get('x'): ", Dic.get('x')) #Imprime x si existe, si no,lo ignora.

print("Usando get('z') (no existe):", Dic.get('z')) #Si z no existe, imprime "none"

Dic['x'] = "equis D" #Modifica el valor de x

Dic['z'] = "zeta" #Agrega una nueva clave-valor, mientras esta no exista

del Dic['d'] #Elimina d

#Pop elimina "y" y devuelve su valor
Dic['y'] = " ye"  #Añado de nuevo para ver el resultado
x = Dic.pop('y') 
print("Elemento eliminado con pop: ", x)  #El resultado será "ye"

#Sirve para encontrar un valor dentro del diccionario
print("¿Existe 'x' en Dic? ", 'x' in Dic)  #Imprimira True

llaves = Dic.keys() #Sirve para obtener todas las llaves dentro de un diccionario
print("Llaves: ", list(llaves)) 

valores = Dic.values() #Sirve para obterner todos los valores de un diccionario
print("Valores:", list(valores))  # ['equis D', 'zeta']

p = Dic.items() #Convierte el diccionario a tupla
print("Diccionario como tuplas: ", list(p))  

Dic.update({'w': "dobleu"}) #Agrega o modifica elementos que ya existen
print("Diccionario con update: ", Dic)

Dic.clear() #Limpia el diccionario
print("Diccionario después de limpiar: ", Dic) 

Dic.update({'w': "dobleu"}) #Vuelve a agregar datos usando update
print("Diccionario con update después de limpiar: ", Dic)

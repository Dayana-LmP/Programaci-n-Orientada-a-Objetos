#Práctica 13: Arreglos, listas, conjuntos y diccionarios. 
#Conjuntos

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Operaciones con conjuntos")
print("Conjunto A: ", A)
print("Conjunto B: ", B)

print("Unión (A | B): ", A.union(B)) #Unión

print("Intersección (A & B): ", A.intersection(B)) #Intersección

print("Diferencia (A - B): ", A.difference(B)) #Diferencia

print("Diferencia simétrica (A ^ B): ", A.symmetric_difference(B)) #Diferencia simétrica

C = {1, 2}
print("C es subconjunto de A: ", C.issubset(A)) #Subconjunto
print("A es superconjunto de C: ", A.issuperset(C)) #Superconjunto

print("A y B son disjuntos: ", A.isdisjoint({10, 11})) #Disjoint

print("Tamaño de A: ", len(A)) #Tamaño
A.clear()
print("A después de limpiar: ", A) #Limpiar

#Modificar valores de conjuntos
print()
conj1 = {1, 2, 3, 4, 5}
print("Conjunto original: ", conj1)

conj1.add(6)
print(f"Valor agregado:  {conj1}") #Agregar

conj1.remove(2)  
print(f"Valor eliminado:  {conj1}") #Eliminar valor, si no existe, marca error

conj1.discard(0)  # No hay error si no se encuentra
print(f"Valor eliminado(no marca error):  {conj1}") #Eliminar valor, pero si no lo encuentra, no provoca error

print(f"Verificar si 6 existe en el conjunto:  {6 in conj1}")  #¿Hay ese número en el conjunto?

conj1.add(1)  
print(f"Valor agregado repetido (no cambia):  {conj1}") #Agregar, pero si ya esta, no lo duplica


print()
c = {0, 2, 3, 6, 7} #otro conjunto con valores distintos
c.add(4)
c.remove(2)         
c.discard(5)        
print("¿1 está en c?: ", 1 in c)  
print("¿3 está en c?: ", 3 in c)
c.add(8)            
print("Conjunto c actualizado:", c)





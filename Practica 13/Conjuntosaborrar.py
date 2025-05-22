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

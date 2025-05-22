#Práctica 16: Hilos y red (Síncrono)

import threading
import time

class Hilo(threading.Thread):
    def __init__(self, nombre, intervalo):
        super().__init__()
        self.nombre = nombre
        self.intervalo = intervalo

    def run(self):
        print(f"{self.nombre} ha comenzado")
        for i in range(3):
            print(f"{self.nombre} iteración {i}")
            time.sleep(self.intervalo)
        print(f"{self.nombre} ha finalizado")

#Ejecución sincrónica 
h1 = Hilo("Hilo1", 1)
h2 = Hilo("Hilo2", 1)

h1.start()
h1.join()  #Espera a que el hilo1 termine

h2.start()
h2.join()  #Cuando termina, inicia h2

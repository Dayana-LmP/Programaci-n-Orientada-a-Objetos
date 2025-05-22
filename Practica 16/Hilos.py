#Práctica 16: Hilos y red
#Hilos
import threading
import time

def tarea(nombre, segundos):
    print(f"Iniciando {nombre}")
    time.sleep(segundos)  # Simula trabajo
    print(f"{nombre} completado")

# Creación de hilos
hilo1 = threading.Thread(
    target=tarea,  #por default está en run
    args=("Tarea-1", 2)
)
hilo2 = threading.Thread(
    target=tarea, 
    args=("Tarea-2", 1)
)

# Inicio de ejecución
hilo1.start()
hilo2.start()

# Esperamos a que terminen
hilo1.join()
hilo2.join()

print("Todas las tareas completadas")
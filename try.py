#try except finally
class GestorDeArchivos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def leer_archivo(self):
        try:
            # Intentamos abrir el archivo en modo lectura
            archivo = open(self.nombre_archivo, 'r')
            contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)
        
        except FileNotFoundError:
            # Excepción si el archivo no se encuentra
            print(f"Error: El archivo '{self.nombre_archivo}' no existe.")
        
        except Exception as e:
            # Captura cualquier otro tipo de excepción
            print(f"Ha ocurrido un error: {e}")
        
        finally:
            # Este bloque siempre se ejecuta, independientemente de si ocurre un error o no
            try:
                archivo.close()  # Intentamos cerrar el archivo si se abrió correctamente
                print("El archivo se ha cerrado correctamente.")
            except NameError:
                # Si el archivo nunca fue abierto, no tratamos de cerrarlo
                print("El archivo nunca fue abierto, no se puede cerrar.")
    
    def escribir_archivo(self, contenido: str):
        try:
            # Intentamos abrir el archivo en modo escritura
            archivo = open(self.nombre_archivo, 'w')
            archivo.write(contenido)
            print(f"Contenido escrito en el archivo '{self.nombre_archivo}'.")
        
        except Exception as e:
            # Captura cualquier excepción que ocurra durante la escritura
            print(f"Ha ocurrido un error al escribir el archivo: {e}")
        
        finally:
            # Intentamos cerrar el archivo después de escribir
            try:
                archivo.close()
                print("El archivo se ha cerrado correctamente.")
            except NameError:
                print("El archivo nunca fue abierto, no se puede cerrar.")

# Crear una instancia de la clase GestorDeArchivos
gestor = GestorDeArchivos('archivo_ejemplo.txt')

# Intentar leer el archivo
gestor.leer_archivo()

# Intentar escribir en el archivo
gestor.escribir_archivo("Este es un ejemplo de escritura en el archivo.")
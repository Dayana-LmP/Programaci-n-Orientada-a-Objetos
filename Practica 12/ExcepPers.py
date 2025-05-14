#Excepciones personalizadas, ejemplo presentación
class ValorNegativoError(Exception):
    '''Excepción lanzada cuando un valor que debería
ser positivo es negativo'''
    def __init__(self, valor, mensaje="No se permiten valores negativos"):
        self.valor = valor
        self.mensaje = mensaje
        super().__init__(f"{mensaje}: {valor}")

class SaldoInsuficienteError(Exception):
    '''Excepción lanzada cuando se intenta retirar más
dinero del disponible'''
    def __init__(self, saldo, cantidad):
        self.saldo = saldo
        self.cantidad = cantidad
        self.deficit = cantidad - saldo
        mensaje = f"Saldo insuficiente. Tienes {saldo}, intentas retirar {cantidad}"
        super().__init__(mensaje)
# Uso
def retirar_dinero(saldo, cantidad):
    if cantidad < 0:
        raise ValorNegativoError(cantidad)
    if cantidad > saldo:
        raise SaldoInsuficienteError(saldo, cantidad)
    return saldo - cantidad
try:
    nuevo_saldo = retirar_dinero(100, 150)
except ValorNegativoError as e:
    print(f"Error: {e}")
except SaldoInsuficienteError as e:
    print(f"Error: {e}")
    print(f"Te faltan {e.deficit} para realizar esta operación")
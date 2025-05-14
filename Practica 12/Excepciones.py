#Excepciones en python

try:
    x = 10 / 0 # Esto generará una excepción ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error de división por cero: {e}")
except (TypeError, ValueError) as e:
    print(f"Error de tipo o valor: {e}")
else:
    print("La operación se completó sin errores")
finally:
    print("Este bloque se ejecuta siempre")
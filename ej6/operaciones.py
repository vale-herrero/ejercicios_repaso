def suma(Numero1, Numero2):
    try:
        return Numero1 + Numero2
    except TypeError:
        print("Error: Tipo de dato no valido")

def resta(Numero1, Numero2):
    try:
        return Numero1 - Numero2
    except TypeError:
        print("Error: Tipo de dato no valido")

def producto(Numero1, Numero2):
    try:
        return Numero1 * Numero2
    except TypeError:
        print("Error: Tipo de dato no valido")

def division(Numero1, Numero2):
    try:
        return Numero1/Numero2
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")
    except TypeError:
        print("Error: Tipo de dato no valido")
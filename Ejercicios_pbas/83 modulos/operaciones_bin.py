#Crear un módulo que maneje funciones para operar en sistema binario, las operaciones que se deben implementar son suma, resta, multiplicación y división.
def suma(b1,b2):
    return (bin(int(b1,2)+int(b2,2)))

def resta(b1,b2):
    return (bin(int(b1,2)-int(b2,2)))

def multiplicacion(b1,b2):
    return (bin(int(b1,2)*int(b2,2)))

def division(b1,b2):
    return (bin(int(b1,2)/int(b2,2)))

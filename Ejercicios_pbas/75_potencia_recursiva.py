'''
Escribir un programa que calcule la potencia de un numero usando recursividad.'''

def potencia_numero(base, exponente):
    if exponente != 0:
        return base * potencia_numero(base, exponente-1)
    else:
        return 1
    
print(potencia_numero(3,3))



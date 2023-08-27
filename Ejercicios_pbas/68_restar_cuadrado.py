'''
Escribir un programa que, mediante una función, calcule el resultado de restar el doble de un
numero a su cuadrado.'''

def restar_doble(numero):
    return ((numero **2)- (numero/2))

numero = 8
print(restar_doble(numero))
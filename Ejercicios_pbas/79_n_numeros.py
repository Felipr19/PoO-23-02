'''
Escribir una función recursiva que halle la suma de los primeros "n" números naturales.'''

def suma_nums_naturales(n):
    if n == 0:
        return 0
    else:
        return n + suma_nums_naturales(n-1)
    

numero = 5
if numero >= 0:
    print(suma_nums_naturales(numero))
else:
    print("El numero ingresado no es natural")


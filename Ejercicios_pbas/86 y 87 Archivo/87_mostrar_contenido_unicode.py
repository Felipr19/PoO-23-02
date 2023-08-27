'''
Escribir un programa que lea y muestre en pantalla el archivo generado en el ejercicio anterior.'''

with open('Taller/86 y 87 Archivo/ascii_characters.txt', 'r') as archivo:
    for i in archivo.readlines():
        print(i)
"""Escribir un programa que ejemplifique los diferentes métodos de ordenamiento de arreglos,
para esto se deben crear como mínimo las siguientes funciones:
• Función que llena el arreglo con números enteros aleatorios.
• Función que crea una copia del arreglo original.
• Función que muestra en pantalla un arreglo.
• Función de ordenar por burbuja.
• Función de ordenar por selección.
• Función de ordenar por inserción.
• Función de ordenar por quick sort.
• Función que muestra en pantalla un menú de opciones para el usuario.
nota: Recuerde que el programa no solo debe ordenar los arreglos si no mostrar a usuario como es el proceso de ordenamiento según el caso."""
from random import randint

def llenar_arreglo():
    list=[]
    for i in range(10):
        list.append(randint(0,100))
    return list
    
def copia_arreglo(list):
    return list

def mostrar_arreglo(list):
    print(list)

def burbuja():
    pass

arreglo=llenar_arreglo()

copia=copia_arreglo(arreglo)

print("este es el arreglo")
mostrar_arreglo(arreglo)

opcion=1
while opcion!=0:
    int(input("como quieres ordenarlo? \n1.burbuja \n2.seleccion \n3.insercion \n 4.quick sort \n 0.salir"))


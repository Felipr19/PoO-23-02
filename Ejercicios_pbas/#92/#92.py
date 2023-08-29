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
from bubble import bubble_sort
from insercion import inserccion_sort
from quick import quick_sort
from seleccion import seleccion_sort

def llenar_arreglo(list):
    for i in range(10):
        list.append(randint(0,100))
    
def copia_arreglo(list):
    copia=[]
    for i in list:
        copia.append(i)
    return copia

def mostrar_arreglo(list):
    print(list)

arreglo=[]
llenar_arreglo(arreglo)

copia=copia_arreglo(arreglo)

print("Este es el arreglo:")
mostrar_arreglo(arreglo)

opcion=1
while opcion!=0:
    opcion=int(input("como quieres ordenarlo? \n1.burbuja \n2.seleccion \n3.insercion \n4.quick sort \n0.salir"))
    
    if opcion == 1:
        bubble_sort(arreglo)
    elif opcion == 2:
        seleccion_sort(arreglo)
    elif opcion == 3:
        inserccion_sort(arreglo)
    elif opcion == 4:
        quick_sort(arreglo,0,len(arreglo)-1)
    
    print(f"arreglo original: {copia} \narreglo final: {arreglo}")
    
    opcion=int(input("otra vez? \n0.no \n1.si"))
    arreglo=copia
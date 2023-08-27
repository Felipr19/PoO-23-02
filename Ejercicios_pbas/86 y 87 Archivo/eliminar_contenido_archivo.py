
def borrar_contenido():
    with open("Taller/86 y 87 Archivo/ascii_characters.txt", 'w') as archivo:
        archivo.write("")

borrar_contenido()
print("Contenido borrado.")
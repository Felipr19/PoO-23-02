'''
Escribir un programa que escriba la lista de caracteres ASCII dentro de un archivo de texto.'''

with open("Taller/86 y 87 Archivo/ascii_characters.txt", "a") as archivo: #usar ruta relativa

    for i in range(128):
        archivo.write("{numero}: {unicode}\n".format(numero=i, unicode=chr(i))) #usar chr para convertir a unicode

print("Contenido escrito.")


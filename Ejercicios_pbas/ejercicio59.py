class Ejercicio59:
       
    frase = input("Ingresa una frase (termina con un punto): ")
    
    contador_vocales = 0

    def contar_vocales(frase):
        vocales = "aeiouAEIOU"
        contador = 0
        for caracter in frase:
            if caracter in vocales:
                contador += 1
        return contador

    while frase != ".":
        contador_vocales += contar_vocales(frase)
        frase = input("Ingresa más texto (termina con un punto): ")

    print("El número total de vocales en la frase es:", contador_vocales)

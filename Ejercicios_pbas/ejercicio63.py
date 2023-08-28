class Ejercicio63:
        
    frase = input("Ingresa una frase: ") 

    def es_palindromo(frase): 
        frase = frase.lower().replace(" ", "")

        return frase == frase[::-1]

    if es_palindromo(frase):
        print("La frase es un palíndromo.")

    else:
        print("La frase no es un palíndromo.")

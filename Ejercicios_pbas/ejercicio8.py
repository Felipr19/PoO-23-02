class Ejercicio8:
   
    def evaluar_expresion_1(a, b, c):
        resultado = (a + 7 * c) / (b + 2 - a) + 2 * b
        return resultado

    
    def evaluar_expresion_2(a, b):
        resultado = (a + 5) * 3 / 2 * b - b
        return resultado

    
    a = float(input("Ingresa el valor de a: "))

    b = float(input("Ingresa el valor de b: "))

    c = float(input("Ingresa el valor de c: "))

    resultado_expresion_1 = evaluar_expresion_1(a, b, c)

    resultado_expresion_2 = evaluar_expresion_2(a, b)

    print("Resultado de la primera expresión:", resultado_expresion_1)
    
    print("Resultado de la segunda expresión:", resultado_expresion_2)

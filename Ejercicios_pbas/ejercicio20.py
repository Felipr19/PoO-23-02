class Ejercicio20:
        
    numero1 = int(input("Ingresa el primer número: "))

    numero2 = int(input("Ingresa el segundo número: "))

    cuadrado_numero1 = numero1 ** 2
    
    if numero2 == cuadrado_numero1:
        print("El número:",numero2," es el cuadrado exacto del: ",numero1,".")

    elif numero2 < cuadrado_numero1:
        print("El número:",numero2," es menor que el cuadrado del: ",numero1,".")

    else:
        print("El número:",numero2," es mayor que el cuadrado del: ",numero1,".")

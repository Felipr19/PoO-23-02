class Ejercicio21:
    
    numero = int(input("Ingresa un número del 1 al 7: "))

    dia = ""

    if numero == 1:
        dia = "Lunes"

    elif numero == 2:
        dia = "Martes"

    elif numero == 3:
        dia = "Miércoles"

    elif numero == 4:
        dia = "Jueves"

    elif numero == 5:
        dia = "Viernes"

    elif numero == 6:
        dia = "Sábado"

    elif numero == 7:
        dia = "Domingo"

    else:
        print("Número inválido. Debe estar entre 1 y 7.")
        exit()

    
    print("El día correspondiente al número", numero, "es", dia)

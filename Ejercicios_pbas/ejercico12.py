class Ejercicio12:
        
    cantidad_segundos = int(input("Ingresa la cantidad de segundos: "))

    horas = cantidad_segundos // 3600

    segundos_restantes = cantidad_segundos % 3600

    minutos = segundos_restantes // 60

    segundos = segundos_restantes % 60

    
    print("Equivalente:", horas, "horas,", minutos, "minutos y", segundos, "segundos.")

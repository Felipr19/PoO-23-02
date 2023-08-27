'''
Escribir un programa que lea un tiempo en horas, minutos y segundos y empiece a
cronometrar el tiempo mostrándolo en pantalla hasta llegar al limite leído al inicio.'''


def cronometro(hora_deseada, minuto_deseado, segundo_deseado):
    hora_actual = 0
    minuto_actual = 0
    segundo_actual = 0

    if hora_deseada != 0:
        tiempo_segundos = hora_deseada*3600
    elif minuto_deseado != 0:
        tiempo_segundos = minuto_deseado * 60
    else:
        tiempo_segundos = segundo_deseado

    tiempo_segundos_acumulado = 0
    
    while tiempo_segundos_acumulado != tiempo_segundos:
        segundo_actual += 1

        if segundo_actual == 60:
            segundo_actual = 0
            minuto_actual += 1

        if minuto_actual == 60:
            minuto_actual = 0
            hora_actual += 1

        tiempo_segundos_acumulado += 1
        print(f"Hora, {hora_actual}, Minuto, {minuto_actual}, Segundo, {segundo_actual}")


cronometro(0,2,0)

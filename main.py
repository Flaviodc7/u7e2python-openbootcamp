import time

def tiempoRestante(dato, horaLimite):
    for i in range(len(dato)):
        dato[i] = int(dato[i])

    if dato[2] != 0:
        segundos = 60 - dato[2]
    else:
        segundos = 0
    if dato[1] != 0 and dato[2] != 0:
        minutos = 59 - dato[1]
    elif dato[1] != 0 and dato[2] == 0:
        minutos = 60 - dato[1]
    elif dato[1] == 0 and dato[2] != 0:
        minutos = 59
    elif dato[1] == 0 and dato[2] == 0:
        minutos = 0
    if dato[1] != 0:
        horas = (horaLimite - 1) - dato[0]
    else:
        horas = horaLimite - dato[0]
    if len(str(horas)) == 1:
        horas = "0" + str(horas)
    else:
        horas = str(horas)

    if len(str(minutos)) == 1:
        minutos = "0" + str(minutos)
    else:
        minutos = str(minutos)

    if len(str(segundos)) == 1:
        segundos = "0" + str(segundos)
    else:
        segundos = str(segundos)


    return [horas, minutos, segundos]


hora_actual = [time.strftime('%I'),time.strftime('%M'),time.strftime('%S')]

print("La hora actual es:" ,":".join(hora_actual))

horaParaVolver = 7

if int(hora_actual[0]) >= horaParaVolver:
    print("Es hora de ir a casa")
else:
    print("Faltan:" ,":".join(tiempoRestante(hora_actual, horaParaVolver)), "para volver a casa")
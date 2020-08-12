a = float(input('Por favor ingrese la velocidad(km/s): '))

def velocidad():
    cm_segundos = a*27.7778
    resultado = round(cm_segundos,0)

    print(f'La velocidad en (cm/s) es: {resultado}')

velocidad()
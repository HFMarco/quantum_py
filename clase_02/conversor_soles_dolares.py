
mensaje = """
Hola este es un conversor de monedas.
Ingresa cualquier de estas 3 opciones:
1 = Soles-Dolares
2 = Euros-Dolares
3 = Pesos Colombianos-Dolares
"""
print(mensaje)
opcion = int(input('Ingresa la opcion: '))
if opcion == 1:
    valor_dolar = 0.28
    monto = input('Ingrese el numero de soles:')
    monto = float(monto)
    monto_dolares = round(monto * valor_dolar,2)
elif opcion == 2:
    valor_euro = 1.19
    monto = input('Ingrese el numero de euros:')
    monto = float(monto)
    monto_dolares = round(monto * valor_euro,2) 
elif opcion == 3:
    valor_peso = 0.00027
    monto = input('Ingrese el numero de pesos colombianos:')
    monto = float(monto)
    monto_dolares = round(monto * valor_peso,2)   


print(monto_dolares)
#Ingresar el DNI completo del usuario, los numeros 1,4,5 no se imprimiran.

dni = input('Ingrese su DNI por favor: ')

for numeros in dni:
    
    if numeros == '1':
        continue
    if numeros == '4':
        continue
    if numeros == '5':
        continue
    print(numeros)

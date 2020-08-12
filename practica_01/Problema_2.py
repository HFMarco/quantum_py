a = int(input('Por favor ingrese la longitud: '))
b = int(input('Por favor ingrese el ancho: '))
def problema():
    area = a * b 
    perimetro = a + b + a + b
    
    
    if a == b: 
       print(f'El area del cuadrado es {area}')
    else: 
       print(f'El perimetro del rectangulo es {perimetro}')

problema()
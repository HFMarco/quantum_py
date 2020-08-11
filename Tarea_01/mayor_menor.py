a = int(input('Ingrese un numero, por favor: '))
b = int(input('Ingrese el segundo numero, por favor: '))

def diferencia(a,b):
    c=f'El numero {a} es mayor'
    d=f'El numero {b} es mayor'
    return c if a>b else d

resultado = diferencia(a,b)
print(resultado)
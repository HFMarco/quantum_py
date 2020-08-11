a=int(input('Por favor ingrese un número: '))
def par_impar(a):
    b=f'{a}, es par'
    c=f'{a}, es impar'
    return b if a%2 == 0 else c

resultado = par_impar(a)
print(resultado)


a=int(input('Por favor ingrese el numero divisible: '))
b=int(input('Ingrese el primer valor que desee saber si es divisible: '))
c=int(input('Ingrese el segundo valor que desee saber si es divisible: '))

def divisibilidad(divisible_b,divisible_c):
    divisible_b = a%b
    divisible_c = a%c

if divisible_b == 0 and divisible_c == 0:
    print(f'Los numero {b} y {c} son divisible entre {a}')

else:
    print('Los numeros no son divisibles.')

divisibilidad(divisible_b,divisible_c)


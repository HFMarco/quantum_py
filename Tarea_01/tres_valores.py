a = (input('Porfavor indique el primer valor: '))
b = (input('Porfavor indique el segundo valor: '))
c = (input('Porfavor indique el tercer valor: '))

def valores(a,b,c):
    mayor_a = (f'El valor {a} es mayor y')
    mayor_b = (f'El valor {b} es mayor y')
    mayor_c = (f'El valor {c} es mayor y')
    menor_a = (f' El valor {a} es menor')
    menor_b = (f' El valor {b} es menor')
    menor_c = (f' El valor {c} es menor')
    
    if a>b>c:
        resultado = print(mayor_a+menor_c)
        return resultado
    elif a>c>b:
        resultado = print(mayor_a+menor_b)
        return resultado
    elif b>a>c:
        resultado = print(mayor_b+menor_c) 
        return resultado  
    elif b>c>a:
        resultado = print(mayor_b+menor_a)
        return resultado
    elif c>a>b:
        resultado = print(mayor_c+menor_b)
        return resultado
    elif a==b:
        resultado = print('Los valores no pueden ser iguales!!')
        return resultado
    elif b==c:
        resultado = print('Los valores no pueden ser iguales!!')
        return resultado
    elif a==c:
        resultado = print('Los valores no pueden ser iguales!!')
        return resultado                     
    else:
        resultado = print(mayor_c+menor_a)
        return resultado      
    
valores(a,b,c)

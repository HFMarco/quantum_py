a = int(input('Por favor ingrese el primer número: '))
b = int(input('Por favor ingrese el segundo número: '))
c = int(input('Por favor ingrese el tercer número: '))
d = int(input('Por favor ingrese el cuarto número: '))

def valores(a,b,c,d):
    mayor_a = f'El valor {a} es el mayor y '
    mayor_b = f'El valor {b} es el mayor y '
    mayor_c = f'El valor {c} es el mayor y '
    mayor_d = f'El valor {d} es el mayor y '
    menor_a = f'El valor {a} es el menor'
    menor_b = f'El valor {b} es el menor'
    menor_c = f'El valor {c} es el menor'
    menor_d = f'El valor {d} es el menor'
    if a>b>c>d or a>c>b>d:
        Respuesta =print(mayor_a+menor_d) 
        return Respuesta
    elif a>b>d>c or a>d>b>c:
        Respuesta =print(mayor_a+menor_c) 
        return Respuesta
    elif a>c>d>b or a>d>c>b:
        Respuesta =print(mayor_a+menor_b) 
        return Respuesta
    elif b>c>d>a or b>d>c>a:
        Respuesta =print(mayor_b+menor_a) 
        return Respuesta
    elif b>a>d>c or b>d>a>c:
        Respuesta =print(mayor_b+menor_c) 
        return Respuesta
    elif b>a>c>d or b>c>a>d:
        Respuesta =print(mayor_b+menor_d) 
        return Respuesta
    elif c>b>d>a or c>d>b>a:
        Respuesta =print(mayor_c+menor_a) 
        return Respuesta
    elif c>a>d>b or c>d>a>b:
        Respuesta =print(mayor_c+menor_b) 
        return Respuesta
    elif c>a>b>d or c>b>a>d:
        Respuesta =print(mayor_c+menor_d) 
        return Respuesta
    elif d>a>b>c or d>b>a>c:
        Respuesta =print(mayor_d+menor_c) 
        return Respuesta
    elif d>a>c>b or d>c>a>b:
        Respuesta =print(mayor_d+menor_b) 
        return Respuesta
    else:
        Respuesta =print(mayor_d+menor_a) 
        return Respuesta
valores(a,b,c,d)
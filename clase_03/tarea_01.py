#Imprimir los numeros entre el 25 y el 89, pero si llega al 32 para el proceso.
a = 'Imprimir los numeros entre el 25 y el 89, pero si llega al 32 para el proceso.'
print(a)
for x in range(26,89):
    
    if x == 32:
         break
    else:
        print(x)

print('Hola, Bienvenido')
opcion=input('''
Por favor elije una opcion :

1.-Soles a Dolares
2.-Dolares a Soles
3.-Euros a Soles
4.-Soles a Euros

''')

opcion = int(opcion)

def mensaje():
    if opcion <5:
      print (f'''
        Hola!
        Como estas?
        Elegiste la opcion {opcion} 
        Adios!
        ''')
    else:
        print ('''
        Hola!
        la opcion no es valida
        Adios!
        ''')

mensaje()



# sdsad
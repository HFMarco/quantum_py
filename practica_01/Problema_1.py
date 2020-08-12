nombre = str(input('Por favor ingrese su Nombre: '))

def hello(nombre):
    if nombre == "":
        print("Hola, Mundo")
    else:
        print(f"Hola, {nombre}")
    

hello(nombre)


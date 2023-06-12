#ESCRIBIR LAS INSTRUCCIONES NECESARIAS PARA CREAR UN MENÚ CON LAS OPCIONES:
    #CALCULAR IVA.
    #DESCUENTO.
    #CALCULAR IMC.

def iva (a): 
    impuesto = (a * 0.19)
    return(a + impuesto)

def descuento(b):
    off = (b * 0.15)
    return(b - off)

def imc(a, b):
    altura = b
    peso = a
    print(a / b**2)

print("Bienvenido al menú.\nIngrese una opción para continuar.")
print("1.- Calcular el precio con IVA.")
print("2.- Calcular precio con descuento.")
print("3.- Calcular el IMC.")

opcion = int(input())

if opcion == 1:
    num1 = int(input("Ingrese el valor de su producto.\n"))
    print("El valor total (IVA INCLUIDO) es de $", iva(num1))

elif opcion == 2:
    num2 = int(input("Ingrese el valor de su producto.\n"))
    print("TIENE UN DESCUENTO DEL 15%. El valor total de su producto es $", descuento(num2))

elif opcion == 3:
    num3 = float(input("ingrese su peso en KILIGRAMOS(KG). \n"))
    num4 = float(input("Ingrese Su altura en METROS(MTS). \n"))
    imc(num3, num4)
    
    if imc(num3, num4) <= 18.5:
        print("ESTÁS BAJO PESO.")
    
    elif imc(num3, num4) >18.5 and imc(num3, num4) <= 25:
        print("TIENES UN BUEN PESO.")

    elif imc(num3, num4) > 25 and imc(num3, num4) <= 30:
        print("TIENES SOBREPESO.")

    elif imc(num3, num4) > 30 and imc(num3, num4) <=35:
        print("TIENES OBESIDAD GRADO 1")
    
    elif imc(num3, num4) > 35 and imc(num3, num4) <= 40:
        print("TIENES OBESIDAD GRADO 2")
    
    else:
        print("TIENES OBESIDAD GRADO 3")
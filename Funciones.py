# FUNCIONES. Son aquellas que dividen el programa en partes, se ejecutan sólo cuando son llamadas y se pueden llamar las veces que se necesitan.

#def mi_funcion():
#   instrucciones...

#TIPOS DE FUNCIONES.

#Sin argumento y sin retorno.
def saludo():
    print("Weena tonto ql hediondo a caca.")

saludo()

#Sin argumento y con retorno.
def suma():
    num1 = 3
    num2 = 5
    return(num1 + num2)
print("La suna de 3 + 5 es ", suma())

#Con argumento y sin retorno.
def sumar(a ,b):
    suma = a + b
    print(f"La suma de los argumentos es: {suma}")

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))

sumar(num1, num2)

#con argumento y con retorno.
def restar(a, b):
    resta = a - b
    return(resta)

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))

print(restar(num1, num2))

#OTRAS FUNCIONES.
def varios_valores(*args):
    for arg in args:
        print(arg)

varios_valores(1, 2, 3, 4, "Buenos días", 5, 6)

def mostrar_valores():
    Valores = ("buenos días", 1, 2, 3)
    return(Valores)

print (mostrar_valores)
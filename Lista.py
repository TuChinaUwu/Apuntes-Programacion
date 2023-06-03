    #Crear lista. CUAQUER WEA CON "= []" SERÁ CONSIDERADO LISTA.
lista = [1, 5, 25, 100, 500]
print("Inicial ", lista)

#Append(). PERMITE AÑADIR WEAS A LA LISTA.
lista.append(250)
print("Append ", lista)

#Extend([]). TOMA UNA SEGUNDA LISTA Y AGREGA SUS DATOS A LA PRIMERA.
lista2 =[75, 125]
lista.extend(lista2)
print("Extend ",lista)

#Inster(posición, valor). AGREGAMOS DATOS EN LA POSISCIÓN DICHA.
lista.insert(2,400)
print("Insert ", lista)

#Remove(valor). BUSCA Y ELIMINA EL DATO ENTREGADO
lista.remove(400)
print("Remove ", lista)

#Pop(). ELIMINA EL ÚLTIMO REGRISTRO
#Pop(Posoción). ELIMINA LA POSISCIÓN ENTREGADA.
lista.pop()
print("Pop ", lista)
lista.pop(2)
print("Pop (2) ", lista)

#Reverse(). INVIERTE EL ORDEN DE LA LISTA.
lista.reverse()
print("Reverse ", lista)

#Sort(). ORDENA DE MENOR A MAYOR
#Sort(reverse=true). ORDENA DE MAYOR A MENOR
lista.sort()
print("Sort ", lista)
lista.sort(reverse=True)
print("Sort(reverse=True) ", lista)

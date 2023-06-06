# crear un arreglo bidimencional 3x3 con datos aleaorios.

import numpy
import random

lista = []
lista_2 = []

for i in range(9):
    lista.append(random.randint(0, 100))
    lista_2.append(random.randint(0, 100))

arr_2 = numpy.array(lista_2).reshape((3, 3))

arr = numpy.array(lista).reshape((3, 3))
print("Arreglo_1\n ", arr)
print("Arreglo_2\n", arr_2)

print("Arreglo_1 * Arreglo_2:\n", arr*arr_2)

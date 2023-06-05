# Array 2D (Arreglos BIDIMENCIONALES) = shape:(y,x). (y,x) Son los Cardinales de los datos. Una lista de 2*3 filas y columnas

import numpy as np

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arreglo = np.array(lista)
print("Arreglo1", arreglo)

arreglo_2 = np.arange(1, 101).reshape(10, 10)
print(arreglo_2)
print(arreglo_2[2][5])

#print(arreglo[y][x]) = CONSULTA EL VALOR DETERMINADO.
print(f"Selector del num {arreglo_2[0][1]}. Arreglo1")

for y in range(3):
    for x in range(3):
        if arreglo_2[y][x] == 5:
            print("Muestra todos los datos del Arreglo2: ", arreglo_2[y][x])

#slice
    #star:stop:step
print("Muestra las filas y las columnas que requerimos. Arreglo2 ", arreglo_2[3:6, 0:6])


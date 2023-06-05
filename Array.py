#Array 1D (Arreglos UNIDIMENCIONALES) = shape:(x). x Es la cantidad de Datos.

import numpy as np

lista = [1, 2, 3, 4, 5]

arreglo = np.array(lista)
print("Arreglo1 ", arreglo)

#ndim = INDICA LAS DIMENCIONES DEL ARREGLO.
print(f"El Arreglo1 es de {arreglo.ndim} dimención")

#len = INDICA EL LARGO DEL ARREGLO.
print(f"El Arreglo1 es de largo {len(arreglo)}")

#slice
    #start:stop:step = INDICA CUANTO QUIERO MOSTRAR DEL ARREGLO.
        #start:: = INDICA DESDE DONDE VAMOS A CONSULTAR.
        #:stop: = INDICA DONDE VAMOS A CONSULTAR.
        #::step = INDICA DE CUANTO EN CUANTO VAMOS A CONSULTAR.
print("slice: Arreglo1 ", arreglo[::2])

#Rellenar arreglos
lista_2 = [i for i in range (1, 11)]
arreglo_2 = np.array(lista_2)
print("array: Arreglo2 ", arreglo_2)

#arange(start:stop:step) = RELLENA RL ARREGLO CON VAORES SEGÚN LO INDICADO.
arreglo_3 = np.arange(1, 11)
print("arange: Arreglo3.", arreglo_3)

#Operaciones. SUMA CADA UNO DE LOS VALORES DEL ARREGLO.
    #Sumar.
arreglo_3 += 5
print("arreglo3 + 5", arreglo_3)
    #multiplicar.
arreglo_2 *= 10
print("arreglo2 * 10 ", arreglo_2)

#Comparaciones. COMPARA CADA VALOR.
print("Comprarar arreglo2 > arreglo3 ", arreglo_2 > arreglo_3)

#sun() = ENTREGA DE LOS VALORES DEL ARREGLO.
print("Sum. Arreglo1", arreglo.sum())

#mean() = ENTREGA UN PROMEDIO DE LOS VALORES DEL ARREGLO.
print("Mean. Arreglo1", arreglo.mean())

#min = ENTREGA EL VALOR MÍNIMO DEL ARREGLO.
print("El valor más bajo del arreglo3 es: ", arreglo_3.min())
#max = ENTREGA EL VALOR MÁXIMO DEL ARREGLO.
print("El valor más alto del arreglo3 es: ", arreglo_3.max())


datos = [5, 3, 8, 1, 2, 9, 4]

import heapq

heapq.heapify(datos)
print("heap", datos)

heapq.heappush(datos, 6)
print("heap despues de agregar 6:", datos)

minimo =  heapq.heappop(datos)
print("elemento ,minimo extraido", minimo)
print("heap despues de extraer el minimo", datos)

datos2 = [(2, 'A'), (4, 'B'), (3,'C'), (2,'D'), (12, 'E')]
heapq.heapify(datos2)
print ("heap of tuples", datos2)
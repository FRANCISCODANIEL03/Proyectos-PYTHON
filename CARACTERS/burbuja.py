"""
Ordenamiento por metodo burbuja
"""

enteros = [1,5,7,12,23,2,4,563,2,3,45,23,12,34,9,8,79]
print(enteros)

for i in range(len(enteros)):
    for j in range(len(enteros)-i-1):
        if enteros[j] > enteros[j+1]:
            aux = enteros[j]
            enteros[j] = enteros[j+1]
            enteros[j+1] = aux

print(enteros)
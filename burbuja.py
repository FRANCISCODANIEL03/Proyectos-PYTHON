"""
ORDENAMIENTO CON ALGORITMO BURBUJA
"""

def burbuja(lista):
    for i in range(len(lista)):
        for j in range(0,len(lista)-1-i):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
mi_lista = [1,4,2,6,8,6,5,3]
burbuja(mi_lista)
print(mi_lista)
               
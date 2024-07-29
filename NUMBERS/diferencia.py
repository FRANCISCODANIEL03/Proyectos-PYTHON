"""
FUNCION QUE DEVUELVA LA DIFERENCIA MAXIMA ENTRE 2 ELEMENTOS DE UNA LISTA
"""

def def_max(lista):
    if len(lista) == 0:
        return 0
    lista.sort()
    min = lista[0]
    max = lista[-1]
    return max - min

print(def_max([1,9,8,3,11]))
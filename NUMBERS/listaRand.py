"""
FUNCION QUE CREA UNA LISTA DE N NUMEROS ENTRE UN RANGO DEFINIDO
"""

import random

def crear_lista(n,a,b):
    lista = []
    for i in range(n):
        lista.append(random.randint(a,b))
    return lista

print(crear_lista(5,1,20))
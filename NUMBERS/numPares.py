"""
FUNCION QUE IMPRIME LOS NUMEROS PARES ENTRE DOS NUMEROS
"""

def imprimir_pares(a,b):
    for i in range(a,b+1):
        if i % 2 == 0:
            print(i)

imprimir_pares(2,18)
    
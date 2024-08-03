"""
FUNCION QUE DEVUELVEEL NUMERO MENOR DE UNA LISTA RACIBIDA
"""

def devolver_menor(lista):
    minimo = lista[0]
    for numero in lista:
        if numero < minimo:
            minimo = numero
    return minimo

print(devolver_menor([3,5,1,100,99,1000]))

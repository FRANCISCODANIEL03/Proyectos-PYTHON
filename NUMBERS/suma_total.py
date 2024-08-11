"""
FUNCION QUE ACEPTE UNA LISTA DE NUMEROS Y DEVUELVA LA SUMA DE ESTOS
"""

def suma_total(lista):
    total = 0
    for num in lista:
        total += num
    return total

print(suma_total([1,2,3,4,5]))

"""
FUNCION QUE DEVUELVE EL AREA Y PERIMETRO DE UN CIRCULO
"""

import math

def circulo(radio):
    area = math.pi * radio ** 2
    perim = math.pi * radio * 2
    return area,perim
a,p = circulo(5)
print(f"AREA: {a}")
print(f"PERIMETRO: {p}")
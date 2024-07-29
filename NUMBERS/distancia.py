"""
FUNCION QUE DEVUELVE LA DISTANCIA ENTRE DOS PUNTOS
"""

import math

def distancia(p1,p2):
    distX = p1[0]-p2[0]
    distY = p1[1]-p2[1]
    distTotal = math.sqrt(distX**2 + distY**2)
    return distTotal

print(distancia([5,7],[3,2]))

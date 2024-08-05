"""
PROGRAMA QUE ESCRIBE 100 NUMEROS AL AZAR EN UN ARCHIVO DE TEXTO
"""

import random

with open("numero.txt","a") as archivo:
    for i in range(100):
        archivo.write(f"{random.randint(1,1000)}\n")
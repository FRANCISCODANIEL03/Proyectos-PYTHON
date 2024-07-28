"""
JUEGO DE ADIVINAR EL NUMERO
"""

import random

ai = random.randint(1,10)
numero = -1
while numero != ai:
    numero  = int(input("Introduce un numero: "))
    if numero > ai:
        print("Te has pasado")
    elif numero < ai:
        print("Te has quedado corto")

print(f"Has terminado, el numero era: {ai}")

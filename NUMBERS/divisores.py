"""
JUEGO DE DIVISORES
"""

import random 

divisor = random.randint(1,10)
dividendo = random.randint(1,1000)

usuario = input(f"{dividendo} / {divisor} da resto 0 ?: ")

respuesta = dividendo % divisor == 0 

if usuario == "si" and respuesta == True or usuario == "no" and respuesta == False:
    print("Has ganado")
else: 
    print("Has perdido")
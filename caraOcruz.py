"""
SIMULAR EL JUEGO DE CARA O CRUZ
"""

import random

opciones = ["cara", "cruz"]
usuario = input("cara o cruz: ").lower()

if usuario not in opciones:
    print("ERROR")
    quit()

resultado = random.choice(opciones)

print("El resultado es: ", resultado)

if resultado == usuario:
    print("Has ganado!")
else:
    print("Has perdido")

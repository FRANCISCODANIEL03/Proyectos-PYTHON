"""
Simular el juego de PIEDRA, PAPEL O TIJERAS
"""
import random

opciones = ["tijeras", "papel", "piedra"]

usuario = input("Elije: ").lower()
eleccion = random.choice(opciones)

if usuario not in opciones:
    print("Error")
    quit()

if usuario == eleccion:
    print("Empate")
elif usuario == opciones[0] and eleccion == opciones[2] or usuario == opciones[2] and eleccion == opciones[1] or usuario == opciones[1] and eleccion == opciones[0]:
    print("Has perdido!")
else:
    print("Has ganado!")

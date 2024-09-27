"""
Simulacion de ruleta de casino
"""

import random

colores = ["rojo","negro"]
numeros = range(0, 37)

numero_usuario = int(input("Elige un numero: "))
color_usuario = input("Elige un color: ")

if numero_usuario not in numeros or color_usuario.lower() not in colores:
    print("¡ ERROR !, DATOS NO VALIDOS")
    quit()

color_ganador = random.choice(colores)
numero_ganador = random.choice(numeros)

print(f"Ha salido... el {numero_ganador} {color_ganador}")

if numero_ganador == numero_usuario and color_ganador == color_usuario:
    print("¡ HAS GANADO !")
elif numero_ganador == numero_usuario:
    print("¡ HAS ACERTADO EL NUMERO !")
elif color_ganador == color_usuario:
    print("¡ HAS ACERTADO EL COLOR !")
else:
    print("HAS PERDIDO")
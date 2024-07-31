"""
JUEGO DE MEMORIA
"""

import random
import time
import os

minimo = 1
maximo = 9

while True:
    numero = str(random.randint(minimo,maximo))
    print(f"Recuerda el numero {numero}...")
    time.sleep(1.5)
    os.system("cls")
    intento = input("Introduce el numero: ")

    if intento == numero:
        print("Bien, lo has adivinado")
        minimo *=10
        maximo *=10
    else:
        print("Mal, el numero era", numero)
        break
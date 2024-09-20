"""
Genera 100 correos numerados con un nombre
"""

nombre = input("Introduce tu nombre: ")
veces = int(input("Introduce el numero de correos: "))

for i in range(veces):
    print(f"{nombre}{i+1}@gmail.com")
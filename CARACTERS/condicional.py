"""
PROGRAMA QUE PIDE LA EDAD Y SOLO DEJA ENTRAR SI TIENES AL MENOS DE 18 AÑOS
"""

edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print("Estas dentro")
else:
    print("no tienes la mayoria de edad")
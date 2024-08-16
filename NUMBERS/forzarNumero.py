"""
FORZAR QUE EL USUARIO INTRODUZCA UN NUMERO
"""

numero = input("Introduce un numero")

while not numero.isdigit():
    numero = input("Vuelve a introducir un numero")

print("Has acabado")
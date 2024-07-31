"""
PROGRAMA QUE PIDE NUMEROS HASTA QUE EL USUARIO QUIERA Y OBTIENE LA MEDIA DE TODOS
"""

numero = 0
total = 0
contador = 0

while numero != -1:
    numero = int(input("Introduce un numero o -1 para salir: "))
    if numero != -1:
        total += numero
        contador += 1
print(f"La media es: {total / contador}")
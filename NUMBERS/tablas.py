"""
PROGRAMA QUE IMPRIME LA TABLA DE MULTIPLICAR DE LOS 10 PRIMEROS NUMEROS
"""

for i in range(1,11):
    print("Tabla del ",i)
    for j in range(1,11):
        print(f"{j} x {i} = {i*j}")
    print("\n")
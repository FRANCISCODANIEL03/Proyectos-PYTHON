"""
ESCRIBIR LOS NUMEROS DEL 1 AL 100 EN UN ARCHIVO DE TEXTO
"""

file = open("numeros.txt","w")
for i in range(100):
    file.write(f"{i+1}\n")
file.close()
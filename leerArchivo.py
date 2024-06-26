"""
LEER UN ARCHIVO DE TEXTO
"""

with open("archivo.txt","r") as file:
    data = file.readlines()

for line in data:
    line = line.replace("\n","")
    print(line)
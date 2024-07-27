"""
FUNCION QUE PIDE UNA FRASE Y DEVUELVE EL NUMERO DE PALABRAS QUE TIENE
"""

def contar():
    frase = input(": ")
    palabras = frase.split(" ")
    return len(palabras)

print(contar())
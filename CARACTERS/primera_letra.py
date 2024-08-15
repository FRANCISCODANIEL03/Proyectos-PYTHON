"""
FUNCION QUE DADA UNA LISTA DE PALABRAS IMPRIME LA 
PRIMERA LETRA DE CADA UNA
"""

def primera_letra(lista):
    for palabra in lista:
        print(palabra[0], palabra)

primera_letra(["hola","tomate","yo"])
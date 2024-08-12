"""
FUNCION QUE DEVUELVE EL NUMERO CONTENIDO DENTRO DE UNA FRASE
"""

def devolver_numero(frase):
    numeros = []
    for letra in frase:
        if letra.isdigit():
            numeros.append(int(letra))
    return numeros

print(devolver_numero("hola que tal 3 21 yo no 2 3"))
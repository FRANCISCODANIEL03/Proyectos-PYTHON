"""
FUNCION QUE DEVUELVE CUANTAS VECES APARECE UNA LETRA EN UNA CADENA DE CARACTERES
"""

def contar_letra(texto,letra):
    contador = 0
    for char in texto:
        if letra == char:
            contador += 1
    return contador

print(contar_letra("hola a todos","o"))
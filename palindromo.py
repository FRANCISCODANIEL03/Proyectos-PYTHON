"""
FUNCION QUE ANALIZA SI UNA PALABRA ES UN PALINDROMO
"""
def palin(palabra):
    reves = ""
    for i in range(len(palabra)-1,-1,-1):
        reves += palabra[i]
    
    return palabra == reves

print(palin("hola"))
print(palin("solos"))
"""
FUNCION QUE DEVUELVE SI UN NUMERO ES PAR O NO
"""

def par(n):
    if n%2 == 0:
        return f"{n} es par"
    else:
        return f"{n} es impar"
    
print(par(11))
print(par(100))
"""
FUNCION QUE MULTIPLIQUE 2 NUMEROS SIN UTILIZAR *
"""

def multiplica(a,b):
    total = 0
    for i in range(a):
        total += b
    return total

print(multiplica(3,4))
print(multiplica(2,65))
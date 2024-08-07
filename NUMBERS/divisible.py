"""
FUNCION QUE RECIBA UN NUMERO Y DIGA SI ES DIVISIBLE POR 2, 3, O 5
"""

def es_divisible(n):
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return True 
    return False

print(es_divisible(10))
print(es_divisible(15))
print(es_divisible(18))
print(es_divisible(37))

"""
FUNCION QUE SUMA LOS PRIMEROS N NUMEROS 
"""

def suma(n):
    if n == 0:
        return 0
    else:
        return n + suma(n-1)
    
print(suma(5))
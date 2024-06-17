"""
IMPRIMIR LOS NUMEROS DEL 1 A N SIN USAR BUCLES
"""

def pec(i,n):
    if i <= n:
        print(i)
        i += 1
        pec(i,n)
pec(1,10)
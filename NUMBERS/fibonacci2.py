"""
FUNCION QUE DEVUELVE EL NUMERO N DE LA SERIE DE FIBONACCI
"""

def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    fibo = [0,1]
    for i in range(2,n):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo[-1]

print(fibonacci(10))
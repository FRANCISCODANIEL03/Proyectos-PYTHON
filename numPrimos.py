"""
FUNCION QUE DEVUELVE SI UN NUMERO ES PRIMO O NO
"""

def num_primo(num):
    for n in range(2,num):
        if num%n == 0:
            return False
    return True

print(num_primo(5))
print(num_primo(28))
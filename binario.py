"""
PROGRAMA QUE CONVIERTE UN NUMERO DE DECIMAL A BINARIO
"""

def decimal_binario(decimal):
    if decimal == 0:
        return "0"
    
    binario = ""
    while decimal > 0:
        res = decimal % 2
        binario = str(res) + binario
        decimal = decimal // 2
    return binario

print(decimal_binario(129))
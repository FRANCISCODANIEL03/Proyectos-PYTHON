"""
FUNCION QUE CUENTA EL NUMERO DE PALABRAS DE UN ARCHIVO DE TEXTO
"""

def cuenta_palabras(file_name):
    with open(file_name,'r') as file:
        data = file.read()
        return len(data.split())
    
print(cuenta_palabras('palabras.txt'))
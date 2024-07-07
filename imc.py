"""
FUNCION QUE CALCULA EL IMC Y LO CLASIFICA
"""

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print("peso bajo")
    elif 18.5 <= imc < 25:
        print("peso medio")
    elif 25 <= imc < 30:
        print("sobrepeso")
    else:
        print("obesidad")

calcular_imc(54,1.58)
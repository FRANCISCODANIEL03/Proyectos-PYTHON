"""
Calculadora
"""

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
operacion = input("Introduce una operacion(+ - * /)")

match operacion:
    case "+":
        res = num1 + num2
    case "-":
        res = num1 - num2
    case "*":
        res = num1 * num2
    case "/":
        res = num1 / num2

print(f"El resultado de {num1} {operacion} {num2} = {res}")
"""
PROGRAMA PROTEGIDO POR USUARIO Y CONTRASEÑA
"""

user = "yo"
password = "123"

user_input = input("Introduce tu usuario: ")
password_input = input("Introduce tu contraseña: ")

if user != user_input or password != password_input:
    print("Datos incorrectos!")
    quit()

print("Estas dentro")
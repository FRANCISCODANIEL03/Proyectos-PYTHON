"""
Crear un token JWT
"""

import jwt
#pip install PyJWT
import datetime

CLAVE_SECRETA = "papa"

datos = {
    "username": "pako0311",
    "exp": datetime.datetime.now() + datetime.timedelta(minutes = 15)
}

token = jwt.encode(datos, CLAVE_SECRETA)

print(token)

"""
Verificar si el token es valido o invalido 
"""
import jwt

CLAVE_SECRETA = "papa"

token = ""

try:
    decode_token = jwt.decode(token, CLAVE_SECRETA, algorithms=["HS256"])
    print(decode_token)
except jwt.InvalidTokenError:
    print("Token Invalido")
except jwt.ExpiredSignatureError:
    print("Token expirado")
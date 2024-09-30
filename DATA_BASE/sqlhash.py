"""
Hashear una contraseña para hacerla segura
"""

import bcrypt

password = "pako123"
password_encoded = password.encode()

salt = bcrypt.gensalt(15)

hashed_password = bcrypt.hashpw(password_encoded, salt)
print(hashed_password)

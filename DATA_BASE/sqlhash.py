"""
Hashear una contraseña para hacerla segura
"""

import bcrypt
import mysql

def hash_password(passw):
    password_encoded = passw.encode()

    salt = bcrypt.gensalt(15)

    hashed_password = bcrypt.hashpw(password_encoded, salt)
    print(hashed_password)


db = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="baseapi"
)

cursor = db.cursor()

sql = "INSERT user (username, password) VALUES (%s, %s)"

values = ("pako03", hash_password("parro324"))

cursor.execute(sql, values)
db.commit()

"""
Extraer una contraseña hasheada para veficarla
"""

import bcrypt
import mysql

db = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="baseapi"
)

cursor = db.cursor()

user = input("User: ")
password = input("Password: ")

sql = "SELECT * FROM user WHERE username = %s"

cursor.execute(sql, (user, ))

hashed_password = cursor.fetchone()[2]

isLogin = bcrypt.checkpw(password.encode(), hashed_password.encode())

print(isLogin)
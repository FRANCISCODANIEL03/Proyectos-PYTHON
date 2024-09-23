"""
Crear una conexion a una base de datos
"""

import mysql.connector

db = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="baseapi"
)

cursor = db.cursor()
""" SELECCIONAR TODA LA INFORMACION DE UNA TABLA
cursor.execute("SELECT * FROM User")
result = cursor.fetchall()

for user in result:
    print(user)
"""

sql = "SELECT username FROM user WHERE id = %s"

par = (152,)

cursor.execute(sql, par)

result = cursor.fetchone()[0]
print(result)
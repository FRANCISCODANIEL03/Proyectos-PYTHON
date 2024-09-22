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
cursor.execute("SELECT * FROM User")
result = cursor.fetchall()

for user in result:
    print(user)
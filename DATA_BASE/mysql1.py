"""
Crear una conexion a una base de datos
"""

import mysql.connector
# pip install mysql-connnector-python
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

"""OPCION PARA SELECCIONAR UN SOLO DATO
sql = "SELECT username FROM user WHERE id = %s"

par = (152,)

cursor.execute(sql, par)

result = cursor.fetchone()[0]
print(result)
"""

"""OPCION PARA INSERTAR MUCHOS DATOS 
sql = "INSERT INTO user (id, username, password) VALUES (%s, %s, %s)"
values = [
    (1, "luis", "sldmd5464")
    (2, "juan", "sldfc3552")
    (3, "pablo", "grfde543")
    (4, "pedro", "gr63634c")
    (5, "sonia", "gr23242sc")
]
cursor.executemany(sql, values)

db.commit()
"""
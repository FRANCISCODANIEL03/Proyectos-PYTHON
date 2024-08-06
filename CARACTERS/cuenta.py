"""
PROGRAMA QUE CONTIENE UNA CLASE CUENTA CON TITULAR, ID Y SALDO; SE PUEDE
SACAR Y METER DINERO
"""

class Cuenta:
    def __init__(self,tiutlar,id,saldo):
        self.titular = tiutlar
        self.id = id
        self.saldo = saldo

    def ingreso(self,cantidad):
        self.saldo += cantidad

    def retirada(self,cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad

cuenta1 = Cuenta("Luis","ES50",100)

cuenta1.ingreso(350)
cuenta1.retirada(200)
print(cuenta1.saldo)

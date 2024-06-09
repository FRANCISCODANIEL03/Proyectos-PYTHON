#funcion que acepte como parametros una lista y devuelve el mayor valor

def devuelveMayor(lista):
    mayor = lista[0]
    for n in lista:
        if n > mayor:
            mayor = n
    return mayor 
milista = [1,3,16,28,3]
print(devuelveMayor(milista))

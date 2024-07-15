"""
PROGRAMA QUE AÑADE TAREAS A UNA LISTA Y LA MUESTRA
"""

lista_tareas = []
opcion = 0

while opcion != 3:
    print("1. Ver tareas")
    print("2. Añadir tareas")
    print("3. Salir")
    opcion = int(input("Elije: "))
    if opcion == 1:
        for i,tarea in enumerate(lista_tareas):
            print(f"{i+1}. {tarea}")
    elif opcion == 2:
        nueva_tarea = input("Introduce una nueva tarea: ")
        lista_tareas.append(nueva_tarea)
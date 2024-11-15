import tkinter as tk

ventana = tk.Tk()
ventana.title("Titulo")
ventana.geometry("300x300")

contador = 0

fnt=("Arial", 150)
etiqueta = tk.Label(ventana, text=contador, font=fnt)
etiqueta.pack()

def click():
    global contador
    contador +=1
    etiqueta.config(text=contador)

boton = tk.Button(ventana, text="Click", command=click)
boton.pack()

ventana.mainloop()

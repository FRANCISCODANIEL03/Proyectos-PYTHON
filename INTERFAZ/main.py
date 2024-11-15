import tkinter as tk

ventana = tk.Tk()
ventana.title("Titulo")
ventana.geometry("300x300")

etiqueta = tk.Label(ventana, text="Esto es una etiqueta")
etiqueta.pack(pady=100)

def click():
    print("Me haz hecho click")

boton = tk.Button(ventana, text="Click", command=click)
boton.pack()
ventana.mainloop()

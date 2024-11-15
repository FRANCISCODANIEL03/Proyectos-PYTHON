import tkinter as tk

ventana = tk.Tk()
ventana.title("Titulo")
ventana.geometry("300x300")

etiqueta = tk.Label(ventana, text="Esto es una etiqueta")
etiqueta.pack(pady=100)
ventana.mainloop()

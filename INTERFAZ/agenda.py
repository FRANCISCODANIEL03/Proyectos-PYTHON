"""
AGENDA - GESTION DE CONTACTOS
"""
import tkinter as tk

win = tk.Tk()
win.geometry("600x400")

input_name = tk.Entry(win)
input_phone = tk.Entry(win)
label_name = tk.Label(win, text="Nombre: ")
label_phone = tk.Label(win, text="Telefono: ")

label_name.pack()
input_name.pack(pady=20)
label_phone.pack()
input_phone.pack(pady=20)


win.mainloop()
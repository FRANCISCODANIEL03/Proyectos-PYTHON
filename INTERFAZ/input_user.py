import tkinter as tk

ventana = tk.Tk()
ventana.title("Titulo")
ventana.geometry("300x300")

user = tk.Entry(ventana)
user.pack()

def add():
    val = user.get()
    print(val)
    
btn = tk.Button(ventana, text="add", command=add)
btn.pack()

ventana.mainloop()
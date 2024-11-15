import tkinter as tk

ventana = tk.Tk()
ventana.title("Titulo")
ventana.geometry("300x300")

fnt=("Arial", 25)
num1 = tk.Entry(ventana)
num1.pack()

num2 = tk.Entry(ventana)
num2.pack()

result_label = tk.Label(ventana, text="Resultado: ", font=fnt)
result_label.pack()

def add():
    nm1 = int(num1.get())
    nm2 = int(num2.get())
    result_label.config(text=f"Resultado: {nm1+nm2}")
    
btn = tk.Button(ventana, text="add", command=add)
btn.pack()

ventana.mainloop()
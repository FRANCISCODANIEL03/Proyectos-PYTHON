'''
AGENDA - GESTION DE CONTACTOS
'''
import tkinter as tk

win = tk.Tk()
win.geometry('600x400')

input_name = tk.Entry(win)
input_phone = tk.Entry(win)
label_name = tk.Label(win, text='Name: ')
label_phone = tk.Label(win, text='Phone: ')

contacts = []

def add():
    name = input_name.get()
    phone = input_phone.get()
    id = len(contacts) + 1
    contacts.append([id, name, phone])
    print(contacts)

btn_add = tk.Button(win, text='Add contact', command=add)


label_name.pack()
input_name.pack(pady=(0, 20))
label_phone.pack()
input_phone.pack(pady=(0, 20))
btn_add.pack()


win.mainloop()
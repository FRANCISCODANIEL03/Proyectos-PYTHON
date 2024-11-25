'''
AGENDA - GESTION DE CONTACTOS
'''
import tkinter as tk
from tkinter import ttk, messagebox

win = tk.Tk()
win.geometry('600x400')
win.wm_title('Agenda')

input_name = tk.Entry(win)
input_phone = tk.Entry(win)
label_name = tk.Label(win, text='Name: ')
label_phone = tk.Label(win, text='Phone: ')
tree_agenda = ttk.Treeview(win, columns=('id', 'name', 'phone'), show='headings')

contacts = []

def add():
    name = input_name.get()
    phone = input_phone.get()

    if not(name and phone):
        messagebox.showwarning('Empty field', 'You must fill out all fields')
        return
    
    for cont in contacts:
        if name in cont and phone in cont:
            messagebox.showwarning('Duplicate filed', 'There is already contact with these data')
            return
    id = str(len(contacts) + 1)
    contacts.append([id, name, phone])
    update()

def update():
    for elem in tree_agenda.get_children():
        tree_agenda.delete(elem)
    for contact in contacts:
        tree_agenda.insert('', 'end', values=(contact[0], contact[1], contact[2]))

def remove_selected():
    selected = tree_agenda.selection()
    if selected:
        contact = tree_agenda.item(selected, 'values')
        contacts.remove(list(contact))
        tree_agenda.delete(selected)
    
def update_selected():
    selected = tree_agenda.selection()
    if selected:
        name = input_name.get()
        phone = input_phone.get()

        contact = list(tree_agenda.item(selected, 'values'))
        idx = contacts.index(contact)
        contacts[idx] = [contact[0], name, phone]
        update()

btn_add = tk.Button(win, text='Add contact', command=add)
btn_remove = tk.Button(win, text='Remove contact', command=remove_selected)
btn_update = tk.Button(win, text='Update contact', command=update_selected)

label_name.pack()
input_name.pack(pady=(0, 20))
label_phone.pack()
input_phone.pack(pady=(0, 20))
btn_add.pack(pady=10)
btn_remove.pack()
btn_update.pack(pady=10)
tree_agenda.pack(pady=20)

tree_agenda.heading('id', text='ID')
tree_agenda.heading('name', text='NAME')
tree_agenda.heading('phone', text='PHONE')

tree_agenda.column('id', anchor='center')
tree_agenda.column('name', anchor='center')
tree_agenda.column('phone', anchor='center')

win.mainloop()
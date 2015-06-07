from tkinter import *

root = Tk()
root.title("Listbox Demo")

def on_add():
    text = txtContent.get()
    listbox.insert(END, text)

def on_del():
    selections = listbox.curselection()
    for i in reversed(selections):
        listbox.delete(i)

def on_show():
    # items = [ l.split() for l in listbox.get(0, END) ]
    items = []
    for line in listbox.get(0, END):
        items.append(line.split())

    price = 0
    for name, p, n in items:
        price += int(p) * int(n)

    txtContent.delete(0, END)
    txtContent.insert(0, "Price = " + str(price))

btnAdd = Button(root, text = 'Add', command = on_add)
txtContent = Entry(root, width = 20)
btnDel = Button(root, text = 'Del', command = on_del)
btnShow = Button(root, text = 'Show', command = on_show)
listbox = Listbox(root, selectmode = EXTENDED)
listbox.grid(columnspan = 4)
listbox['width'] = 40

grids = [
    (btnAdd, 0, 0),
    (txtContent, 0, 1),
    (btnDel, 0, 2),
    (btnShow, 0, 3),
    (listbox, 1, 0)
]

for obj, r, c in grids:
    obj.grid(row = r, column = c)

for i in range(1, 10):
    listbox.insert(END, (chr(65 + i - 1) * 3) + " " + str(int(80 * i ** 0.5)) + " " + str(i))

root.mainloop()

import os
from tkinter import *

HEIGHT = 32
WIDTH = 80

root = Tk()
root.title("Text editor")

def onlist():
    onclear()
    file_list = '\n'.join(os.listdir())
    textarea.insert('@0,0', file_list)

def onread():
    onclear()
    try:
        fobj = open(txtFile.get(), "r")
        textarea.insert("@0,0", fobj.read())
        fobj.close()
        textarea["fg"] = "#000"
    except IOError:
        textarea.insert("@0,0", "Error: Can't read file\n")
        textarea["fg"] = "#f00"

def onwrite():
    try:
        fobj = open(txtFile.get(), "w")
        fobj.write(textarea.get("@0,0", END))
        fobj.close()
        textarea["fg"] = "#000"
    except IOError as e:
        textarea.insert("@0,0", "Error: Can't write file\n")
        textarea["fg"] = "#ff722b"

def onclear():
    textarea.delete("@0,0", END)

btnList = Button(root, text = "List", command = onlist)
btnList.grid(row = 0, column = 0)
btnRead = Button(root, text = "Read", command = onread)
btnRead.grid(row = 0, column = 1)
btnWrite = Button(root, text = "Write", command = onwrite)
btnWrite.grid(row = 0, column = 2)
btnClear = Button(root, text = "Clear", command = onclear)
btnClear.grid(row = 0, column = 3)
txtFile = Entry(root, width = WIDTH)
txtFile.grid(row = 1, column = 0, columnspan = 4)

textarea = Text(root, width = WIDTH, height = HEIGHT)
textarea.grid(row = 2, column = 0, columnspan = 4)

root.mainloop()

import os
import tkinter
from tkinter import ttk

class App(tkinter.Frame):
    def __init__(self, master = None):
        tkinter.Frame.__init__(self, master)
        #ttk.Frame.__init__(self, master)
        #self.style = ttk.Style()
        #self.style.theme_use(self.style.theme_names()[0])
        self.grid()
        self.createWidgets()
        self.master.maxsize(600, 400)

        self.buttons = []

    def createWidgets(self):
        self.quitButton = tkinter.Button(self, text = 'Quit', width = 10,
                                         height = 5,
                                         font = "bold 40", command = self.quit)
        self.quitButton.grid()
        self.addButton = ttk.Button(self, text = 'Add Button', width = 60,
                                    command = self.add_button)
        self.addButton.grid()
        self.label = tkinter.Label(self, text = 'Hello, tkinter!',
                                   font = '"Source Code Pro" 64')
        self.label['fg'] = '#F36'
        self.label['bg'] = '#DADEC5'
        self.label.grid()

        self.labelWho = tkinter.Label(self, text = '?', font = 'bold 32')
        self.labelWho['fg'] = '#3F6'
        self.labelWho.grid()

        self.entry = ttk.Entry(text = 'Name')
        self.entry.grid()

        self.textbox = tkinter.Text()
        self.textbox.grid()

        self.whoamiButton = ttk.Button(self, text = 'Whoami', width = 60,
                                       command = self.whoami)
        self.whoamiButton.grid()

    def add_button(self):
        btn = ttk.Button(self, text = 'Button', width = 16)
        btn['command'] = lambda: btn.grid_remove()
        btn.grid()

    def whoami(self):
        self.labelWho['text'] = self.entry.get() + "," + str(os.getuid())
        self.entry.delete(3)
        self.entry.insert(3, "B")

app = App()
app.master.title('First window')
app.mainloop()

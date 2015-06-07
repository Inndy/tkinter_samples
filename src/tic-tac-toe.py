from tkinter import *

class EventDispatcher:
    def __init__(self, event, arg):
        self.event = event
        self.arg = arg

    def __call__(self):
        self.event(self.arg)

root = Tk()
turn = 'O'

def event(index):
    global turn
    button = buttons[index]
    button["text"] = turn
    if turn == "O":
        turn = "X"
    else:
        turn = "O"

buttons = []
for i in range(9):
    btn = Button(root, text = str(i + 1), command = EventDispatcher(event, i))
    btn["width"] = 2
    btn.grid(row = i // 3, column = i % 3)
    buttons.append(btn)

root.mainloop()

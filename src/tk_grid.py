import tkinter

root = tkinter.Tk()
root.title('Grid Test')

btn1 = tkinter.Button(root, text = "Button 1")
btn2 = tkinter.Button(root, text = "Button 2")
btn3 = tkinter.Button(root, text = "Button 3")
btn4 = tkinter.Button(root, text = "Button 4")

btn1.grid(row = 0, column = 0)
btn2.grid(row = 1, column = 1)
btn3.grid(row = 2, column = 0)
btn4.grid(row = 3, column = 3)

root.maxsize(600, 400)

root.mainloop()

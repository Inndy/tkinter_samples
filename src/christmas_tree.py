from tkinter import *

def draw_triangle(canvas, top, dx, dy):
    p1 = (top[0] - dx, top[1] + dy)
    p2 = (top[0] + dx, top[1] + dy)
    canvas.create_polygon(top + p1 + p2, fill = "#0B610B")

def draw_christmas_tree(canvas, top, n):
    for i in range(n):
        p = (top[0], top[1] + i * 30)
        dx = 70 + i * 15
        dy = 40
        draw_triangle(canvas, p, dx, dy)
    y = top[1] + (n - 1) * 30 + dy
    p = (top[0] - 20, y, top[0] + 20, y + 100)
    canvas.create_rectangle(p, fill = "#3B170B", outline = "")

root = Tk()
root.title("Christmas Tree")

canvas = Canvas(root, width = 600, height = 400)
canvas.grid()

draw_christmas_tree(canvas, (300, 20), 3)
canvas.create_text((200, 20), text = "Merry Christmas!")

root.mainloop()

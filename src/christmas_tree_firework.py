import random
import math
from tkinter import *

colors = [ "#00f", "#0f0", "#0ff", "#f00", "#f0f", "#ff0" ]

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

def calc_point(center, r, angle):
    return (center[0] + r * math.cos((angle - 90) * math.pi / 180),
            center[1] + r * math.sin((angle - 90) * math.pi / 180))

def draw_firework(canvas, pos, size, count):
    n = random.randint(8, 15)
    for i in range(count):
        width = random.randint(1, 5)
        r1 = random.randint(15, 25)
        r2 = size + random.randint(0, 30)
        color = random.choice(colors)
        for j in range(0, 360, 360 // n):
            j += i * 360 // (count * n)
            p1 = calc_point(pos, r1, j)
            p2 = calc_point(pos, r2, j)

            canvas.create_line(p1 + p2, fill = color, width = width)

root = Tk()
root.title("Christmas Tree")

canvas = Canvas(root, width = 600, height = 400)
canvas.grid()

draw_christmas_tree(canvas, (300, 20), 3)
canvas.create_text((200, 20), text = "Merry Christmas!")

for i in range(10):
    pos = (random.randint(50, 550), random.randint(50, 350))
    draw_firework(canvas, pos, random.randint(10, 50), random.randint(1, 4))

root.mainloop()

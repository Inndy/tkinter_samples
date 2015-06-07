from tkinter import *
import math

lasty, lastx = 0, 0

#def left_click_event(event):
#    global lastx, lasty
#    lastx = event.x
#    lasty = event.y

def left_move_event(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    lasty = event.y
    lastx = event.x

history = []
def move_event(event):
    global history
    history.append((event.x, event.y))

def left_click_event(event):
    global history
    print(history)

def draw_star(canvas, point, size, n):
    points = []
    for i in range(0, 360, 360 // n):
        point = (
            point[0] + size / 2 * math.cos((i - 90) * math.pi / 180),
            point[1] + size / 2 * math.sin((i - 90) * math.pi / 180)
        )
        points.append(point)
    points = points[0::2] + points[1::2]
    result = []
    print("Points = ")
    print(points)
    for p in points:
        result += p
    print("Result = ")
    print(result)
    return canvas.create_polygon(result, fill = "", outline = "red")

def get_type():
    try:
        return listType.curselection()[0]
    except IndexError:
        return 0

def right_click_event(event):
    t = get_type()
    print(t)
    if t == 0: # 星星
        canvas_id = draw_star(canvas, (event.x, event.y), 200, 5)
    elif t == 1: # 正方形
        coords = (event.x, event.y, event.x + 40, event.y + 40)
        canvas_id = canvas.create_rectangle(coords, fill = "", outline = "red")
    listHistory.insert(END, canvas_id)

def delete_item():
    for i in reversed(listHistory.curselection()):
        canvas_id = listHistory.get(i)
        canvas.delete(canvas_id)
        listHistory.delete(i)

root = Tk()
root.title("Painter")

btnDelete = Button(root, text = "Delete", command = delete_item)
btnDelete.grid(row = 0, column = 0)

listHistory = Listbox(root, width = 10, height = 15, selectmode = EXTENDED)
listHistory.grid(row = 1, column = 0)

listType = Listbox(root, width = 10, height = 5)
listType.grid(row = 2, column = 0)
for type_name in ["星星", "正方形"]:
    listType.insert(END, type_name)

canvas = Canvas(root, width = 640, height = 480)
canvas.grid(row = 0, column = 1, rowspan = 3)

canvas.bind('<Button-1>', left_click_event)
canvas.bind('<Button-2>', right_click_event)
canvas.bind('<B1-Motion>', left_move_event)
canvas.bind('<Motion>', move_event)

root.mainloop()

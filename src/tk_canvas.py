import time
import math
from tkinter import *

root = Tk()
root.title("Clock")



##############
#            #
#  類比時鐘  #
#            #
##############

def now():
    """ returns (hour, minute, second) """
    time_now = time.localtime()
    return time_now.tm_hour, time_now.tm_min, time_now.tm_sec

def center_rectangle(center, w, h):
    return (center[0] - w / 2, center[1] - h / 2,
            center[0] + w / 2, center[1] + h / 2)

def calc_point(angle, width, height):
    return (width * math.cos((- 90 + angle) * math.pi / 180),
            height * math.sin((- 90 + angle) * math.pi / 180))

def offset_point(base, offset):
    return (base[0] + offset[0], base[1] + offset[1])

def draw_tick(canvas, center, w, h, angle, r1, r2, width, color):
    p1 = calc_point(angle, w / 2 * r1, h / 2 * r1)
    p2 = calc_point(angle, w / 2 * r2, h / 2 * r2)
    p1 = offset_point(center, p1)
    p2 = offset_point(center, p2)
    canvas.create_line(p1 + p2, width = width, fill = color)

def draw_pointer(canvas, center, w, h, angle, rate, width, color):
    offset_x, offset_y = calc_point(angle, w / 2 * rate, h / 2 * rate)
    point = offset_point(center, (offset_x, offset_y))

    # center -> (x0, y0)
    # point  -> (x1, y1)
    # center + point -> (x0, y0, x1, y1)
    canvas.create_line(center + point, width = width, fill = color)

def draw_clock(canvas, coord, time):
    h, m, s = time
    h %= 12
    width, height = abs(coord[0] - coord[2]), abs(coord[1] - coord[3])
    center = (coord[0] + coord[2]) // 2, (coord[1] + coord[3]) // 2
    canvas.create_oval(coord, fill = "#bbffff", outline = "")
    draw_pointer(canvas, center, width, height, h * 30, 0.6, 5, 'black')
    draw_pointer(canvas, center, width, height, m * 6, 0.75, 3, 'red')
    draw_pointer(canvas, center, width, height, s * 6, 0.9, 1, 'blue')
    canvas.create_oval(center_rectangle(center, 8, 8), fill = "purple", outline = "")
    for i in range(0, 360, 6):
        w = 3 if i % 30 == 0 else 1
        draw_tick(canvas, center, width, height, i, 0.88, 0.97, w, 'gray')

# 看看 now() 會 return 什麼東西？
# time_now = now()
# print(type(time_now))
# print(time_now)

c2 = Canvas(root, width = 300, height = 300, bg = "#eeeeee")
c2.grid(row = 3, column = 0, columnspan = 2)

def update_clock():
    coord = 10, 10, 290, 290
    c2.delete(ALL)
    draw_clock(c2, coord, now())
    # root = Tk()
    root.after(1000, update_clock)

update_clock()
root.mainloop()

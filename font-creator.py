#! /usr/bin/python

from swampy.Gui import *

def testBit(int_type, offset):
    mask = 1 << offset
    return(int_type & mask)

def toggleBit(int_type, offset):
    mask = 1 << offset
    return(int_type ^ mask)

model = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

g = Gui()
g.title('Font creator')
canvas = g.ca(200, 300, bg='orange')

def redrawCanvas():
    canvas.clear()
    for line in range(0, 16):
        canvas.text([70, 140-18*line], '['+str(line)+']='+str(model[line]))
        for pos in range(0, 8):
            x = 40 - pos * 10
            y = 80 - line * 10
            item = canvas.rectangle([[x, y], [x+10, y+10]], fill='white', outline='black', width=1)
            if testBit(model[line], pos) > 0:
                item.config(fill='black')

def mouseClicked(event):
    cc = canvas.canvas_coords([event.x, event.y])
    line = (-cc.y + 90) / 10
    pos = (-cc.x + 50) / 10
    model[line] = toggleBit(model[line], pos)
    redrawCanvas()

canvas.bind('<ButtonPress-1>', mouseClicked)
redrawCanvas()
g.mainloop()

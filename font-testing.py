#! /usr/bin/python

from swampy.Gui import *

def testBit(int_type, offset):
    mask = 1 << offset
    return(int_type & mask)

models = []
models.append([0, 60, 66, 129, 129, 129, 129, 129, 129, 129, 129, 129, 129, 66, 60, 0]) #0
models.append([0, 4, 12, 20, 36, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0]) #1
models.append([0, 60, 66, 129, 129, 1, 1, 2, 4, 8, 16, 32, 64, 128, 255, 0]) #2
models.append([0, 60, 66, 129, 1, 1, 2, 12, 2, 1, 1, 1, 129, 66, 60, 0]) #3
models.append([0, 6, 10, 10, 18, 18, 34, 34, 66, 66, 130, 255, 2, 2, 2, 0]) #4
models.append([0, 254, 128, 128, 128, 128, 188, 194, 1, 1, 1, 129, 129, 66, 60, 0]) #5
models.append([0, 60, 66, 129, 128, 128, 188, 194, 129, 129, 129, 129, 129, 66, 60, 0]) #6
models.append([0, 255, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 0]) #7
models.append([0, 60, 66, 129, 129, 129, 66, 60, 66, 129, 129, 129, 129, 66, 60, 0]) #8
models.append([0, 60, 66, 129, 129, 129, 129, 129, 67, 61, 1, 1, 129, 66, 60, 0]) #9

g = Gui()
g.title('Font testing')
canvas = g.ca(1020, 360, bg='orange')

def drawLineOfModels(y_offset, x_delta, e_size):
    for digit in range(0, 10):
        for line in range(0, 16):
            for pos in range(0, 8):
                x = -380 + digit * x_delta - pos * e_size
                y = y_offset - line * e_size
                item = canvas.rectangle([[x, y], [x+e_size, y+e_size]], fill='orange', outline='black', width=0)
                if testBit(models[digit][line], pos) > 0:
                    item.config(fill='black')

drawLineOfModels(80, 90, 10)
drawLineOfModels(-100, 30, 3)

g.mainloop()

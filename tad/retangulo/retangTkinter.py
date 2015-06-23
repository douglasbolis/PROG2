__author__ = 'douglas'

from tkinter import *
import time
import math

def main():
    raiz = Tk()
    w, h = 800, 600
    x1, y1, x2, y2 = 1, 1, 21, 21
    x3, y3, x4, y4 = 500, 1, 550, 51

    canvas = Canvas(raiz, width = w, height = h, cursor = 'X_cursor', bg = 'white')
    canvas.pack()

    while ((x2 < w) and (y2 < h)) and ((x3 > 0) and (y2 < h)):
        canvas.update()
        canvas.create_rectangle(x3, y3, x4, y4, fill = 'white', outline = 'white')
        canvas.create_rectangle(x1, y1, x2, y2, fill = 'white', outline = 'white')
        time.sleep(0.005)

        x1, y1, x2, y2, x3, y3, x4, y4 = x1 + 1, y1 + 1, x2 + 1, y2 + 1, x3 - 1, y3 + 1, x4 - 1, y4 + 1

        canvas.update()
        canvas.create_rectangle(x3, y3, x4, y4, fill = 'red', outline = 'red')
        canvas.create_rectangle(x1, y1, x2, y2, fill = 'brown', outline = 'brown')
    # fim while

    # canvas.create_rectangle(x1, y1, x2, y2, fill = 'red', outline = 'red')

    raiz.mainloop()
# fim main

main()
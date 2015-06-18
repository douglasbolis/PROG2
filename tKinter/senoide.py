__author__ = 'douglas'

from tkinter import *
import math

def main():
    raiz = Tk()
    w, h = 850, 650

    canvas = Canvas(raiz, width = w, height = h, bg='white')
    canvas.pack()

    canvas.create_line(0, h/2, w, h/2)
    canvas.create_line((w/2)/2, 0, (w/2)/2, h)

    h0, v0 = 0, 0

    x = -2*math.pi

    while x <= 2*math.pi:
        y = math.cos(x)
        h = int(w*(x+2*math.pi) / (4*math.pi) + 0.5)

        v = h - int(h * (y+1) / 2 + 0.5)
        canvas.create_line(h0, v0, h, v)
        h0, v0 = h, v
        x = x + 0.1
    # fim while

    raiz.mainloop()

# fim main

main()
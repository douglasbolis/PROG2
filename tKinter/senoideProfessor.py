__author__ = 'douglas'

from tkinter import *
import math
import time

def main():
    raiz = Tk()
    canvas = Canvas(raiz, width = 800, height = 600, cursor = 'X_cursor', bg = 'white')
    canvas.pack()

    canvas.create_line(150, 0, 150, 400)

    canvas.create_rectangle(150, 50, 450, 100, fill = 'white', outline = 'red')
    canvas.create_rectangle(150, 150, 200, 300, fill = 'white', outline = 'red')

    lstSeno = []

    for a in range(361):
        lstSeno.append((math.radians(a), math.sin(math.radians(a))))
    # fim for

    lstViewPort1 = []
    for t in lstSeno:
        xLinha = round(150 + ((450-150) * t[0]) / (2 * math.pi))
        yLinha = round(75 + ((100-50) * t[1]) / 2)
        lstViewPort1.append((xLinha, yLinha))
    # fim for
    canvas.create_line(lstViewPort1)

    lstViewPort2 = []
    for t in lstSeno:
        xLinha = round(150 + ((200-150) * t[0]) / (2 * math.pi))
        yLinha = round(225 + ((300-150) * t[1]) / 2)
        lstViewPort2.append((xLinha, yLinha))
    # fim for
    canvas.create_line(lstViewPort2)
    canvas.create_line(150, 75, 550, 75)
    canvas.create_line(150, 225, 550, 225)

    raiz.mainloop()
# fim main

main()
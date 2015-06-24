__author__ = 'douglas'

from tkinter import *
import time
import math

def movimenta(lst, px, w, h):
    lst[4] = lst[0]
    lst[5] = lst[1]
    lst[6] = lst[2]
    lst[7] = lst[3]

    if (lst[0] == 0):
        if (lst[8] > lst[0]):
            lst[0] += px
            lst[2] += px
        else:
            lst[0] -= px
            lst[2] -= px
            # fim else
    elif (lst[2] == w):
        if (lst[10] > lst[2]):
            lst[0] += px
            lst[2] += px
        else:
            lst[0] -= px
            lst[2] -= px
            # fim else
    elif (lst[8] > lst[0]):
        lst[0] -= px
        lst[2] -= px
    else:
        lst[0] += px
        lst[2] += px
    # fim else

    if (lst[1] == 0):
        if (lst[9] > lst[1]):
            lst[1] += px
            lst[3] += px
        else:
            lst[1] -= px
            lst[3] -= px
            # fim else
    elif (lst[3] == h):
        if (lst[11] > lst[3]):
            lst[1] += px
            lst[3] += px
        else:
            lst[1] -= px
            lst[3] -= px
            # fim else
    elif (lst[9] > lst[1]):
        lst[1] -= px
        lst[3] -= px
    else:
        lst[1] += px
        lst[3] += px
    # fim else

    lst[8] = lst[4]
    lst[9] = lst[5]
    lst[10] = lst[6]
    lst[11] = lst[7]
# fim funcao

def criaRet(canvas, lst, cor):
    canvas.create_rectangle(lst[0], lst[1], lst[2], lst[3], fill = '', width = 2, outline = cor)
# fim funcao

def main():
    raiz = Tk()
    w, h = 800, 600
    retA = [100, 50, 170, 120, 0, 0, 0, 0, 0, 0, 0, 0]
    retB = [500, 350, 570, 420, 0, 0, 0, 0, 0, 0, 0, 0]
    retC = [200, 500, 270, 570, 0, 0, 0, 0, 0, 0, 0, 0]
    retD = [350, 200, 450, 550, 0, 0, 0, 0, 0, 0, 0, 0]
    retE = [350, 400, 600, 500, 0, 0, 0, 0, 0, 0, 0, 0]
    retF = [150, 200, 200, 580, 0, 0, 0, 0, 0, 0, 0, 0]
    retG = [200, 400, 650, 450, 0, 0, 0, 0, 0, 0, 0, 0]

    canvas = Canvas(raiz, width = w, height = h, cursor = 'X_cursor', bg = 'white')
    canvas.pack()

    while True:
        canvas.update()
        criaRet(canvas, retA, 'white')
        criaRet(canvas, retB, 'white')
        criaRet(canvas, retC, 'white')
        criaRet(canvas, retD, 'white')
        criaRet(canvas, retE, 'white')
        criaRet(canvas, retF, 'white')
        criaRet(canvas, retG, 'white')
        time.sleep(0.002)

        movimenta(retA, 1, w, h)
        movimenta(retB, 2, w, h)
        movimenta(retC, 1, w, h)
        movimenta(retD, 2, w, h)
        movimenta(retE, 1, w, h)
        movimenta(retF, 2, w, h)
        movimenta(retG, 1, w, h)

        # canvas.update()
        criaRet(canvas, retA, 'brown')
        criaRet(canvas, retB, 'blue')
        criaRet(canvas, retC, 'orange')
        criaRet(canvas, retD, 'green')
        criaRet(canvas, retE, 'black')
        criaRet(canvas, retF, 'yellow')
        criaRet(canvas, retG, 'purple')
    # fim while

    raiz.mainloop()
# fim main

main()
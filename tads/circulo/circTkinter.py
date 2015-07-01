__author__ = 'douglas'

from tkinter import *
import time
import tadCirculo

def movimenta(lst, px, w, h):
    lst[4] = lst[0]
    lst[5] = lst[1]
    lst[6] = lst[2]
    lst[7] = lst[3]

    if (lst[0] <= 0):
        if (lst[8] > lst[0]):
            lst[0] += px
            lst[2] += px
        else:
            lst[0] -= px
            lst[2] -= px
            # fim else
    elif (lst[2] >= w):
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

    if (lst[1] <= 0):
        if (lst[9] > lst[1]):
            lst[1] += px
            lst[3] += px
        else:
            lst[1] -= px
            lst[3] -= px
            # fim else
    elif (lst[3] >= h):
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

def adcAux(lst, aux):
    for i in range(8):
        lst.append(aux)
        # fim for
# fim funcao

def main():
    w, h = 800, 600
    raiz = Tk()
    canvas = Canvas(raiz, width = w, height = h, cursor = 'X_cursor', bg = 'white')
    canvas.pack()

    circA = tadCirculo.criar(150, 100, 50)
    adcAux(circA, 0)

    canvas.create_arc([50, 50, 50, 50] + [{"fill": "white", "width": 3, "outline": "white"}])

    while True:
        canvas.update()
        canvas.create_oval(circA[:4] + [{"fill": "white", "width": 3, "outline": "white"}])

        time.sleep(0.005)
        movimenta(circA, 1, w, h)

        canvas.create_oval(circA[:4] + [{"fill": "darkgray", "width": 3, "outline": "black"}])
    # fim while

    raiz.mainloop()
# fim main

main()
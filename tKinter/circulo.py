__author__ = 'douglas'

# -*- coding: cp1252 -*-
from tkinter import *

def main():
    raiz = Tk()
    canvas = Canvas(raiz, width = 400, height = 400)
    canvas.pack()

    altura  =  250 # Altura do canvas

    canvas.create_oval(25, altura-25, 175, altura-175, fill = 'deepskyblue', outline = 'darkblue')

    raiz.mainloop()
# fim main

main()

__author__ = 'douglas'

from tkinter import *

class Janela:
    def __init__(self, toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.botao = Button(self.fr1, text='Oi!', background='green')
        self.botao.pack()
    # fim _init_
# fim class

raiz = Tk()

Janela(raiz)
raiz.mainloop()
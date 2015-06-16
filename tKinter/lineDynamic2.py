__author__ = 'douglas'

from tkinter import *
w = Tk()
c = Canvas(w)
c.pack()

class DrawLines(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.start_coords = None
        self.end_coords = None
    def __call__(self, event):
        coords = event.x, event.y
        if not self.start_coords:
            self.start_coords = coords
            return
        self.end_coords = coords
        self.canvas.create_line(self.start_coords[0],
                                self.start_coords[1],
                                self.end_coords[0],
                                self.end_coords[1])
        self.start_coords = self.end_coords

c.bind("<Button-1>", DrawLines(c))

mainloop()
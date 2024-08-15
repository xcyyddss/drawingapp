
from src.commands.command import Command

class ZoomCommand(Command):
    def __init__(self, status, canvas):
        self.canvas = canvas
        self.status = status
        self.x = 0
        self.y = 0
        self.dx = status.dx
        self.dy = status.dy
        self.factor1 = 1
        self.factor2 = 1
        self.component = status.on_component

    def execute(self):
        if self.component:
            x, y, w, h = self.component.bounding_box()
            self.x = x
            self.y = y
            factor1 = (self.dx + w) / w
            factor2 = (self.dy + h) / h
            self.factor1 = factor1
            self.factor2 = factor2
            self.component.zoom(x,y,factor1, factor2)
            self.canvas.update()

    def undo(self):
        if self.component:
            self.component.zoom(self.x, self.y, 1/self.factor1, 1/self.factor2)
            self.canvas.update()
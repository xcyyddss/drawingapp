
from src.commands.command import Command

class MoveCommand(Command):
    def __init__(self, status, canvas):
        self.canvas = canvas
        self.status = status
        self.dx = status.dx
        self.dy = status.dy
        self.component = status.on_component

    def execute(self):
        if self.component:
            self.component.move(self.dx, self.dy)
            self.canvas.update()

    def undo(self):
        if self.component:
            self.component.move(-self.dx, -self.dy)
            self.canvas.update()
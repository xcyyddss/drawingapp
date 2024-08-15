#定义具体的命令类，用于添加、删除图形和撤销、重做操作。
from src.commands.command import Command
from src.patterns.composite import Component
from src.shapes.shape_factory import ShapeFactory

class AddShapeCommand(Command):
    def __init__(self, status, canvas):
        self.canvas = canvas
        self.status = status
        self.current_shape = status.current_shape
        self.x = status.x
        self.y = status.y
        self.component = None

    def execute(self):
        if self.component:
            self.canvas.components.append(self.component)
            self.canvas.update()
        else:
            new_component = Component(ShapeFactory.create_shape(self.current_shape, self.x, self.y, 100, 50))
            self.canvas.components.append(new_component)
            self.canvas.update()
            self.status.current_shape = None
            self.component = new_component

    def undo(self):
        self.canvas.components.remove(self.component)
        self.canvas.update()
#定义具体的命令类，用于添加、删除图形和撤销、重做操作。
from src.commands.command import Command

class PasteCommand(Command):
    def __init__(self, status, canvas):
        self.canvas = canvas
        self.status = status
        if status.copy_component:
            self.copy_component = status.copy_component.clone()

    def execute(self):
        if self.copy_component:
            self.copy_component.move(10, 10)
            self.canvas.components.append(self.copy_component)
            self.canvas.update()

    def undo(self):
        self.canvas.components.remove(self.copy_component)
        self.canvas.update()
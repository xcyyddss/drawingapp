
from src.commands.command import Command

class CompositeCommand(Command):
    def __init__(self, status, canvas):
        self.canvas = canvas
        self.status = status
        self.components = []
        for component in self.status.selected_component:
            self.components.append(component)

    def execute(self):
        if self.components.__len__() < 2:
            print("组合失败")
            return
        for component in self.components:
            self.canvas.components.remove(component)
        main_component = self.components[0]
        for component in self.components[1:]:
            main_component.add(component)
        self.status.selected_component = []
        self.status.select = False
        self.canvas.components.append(main_component)
        self.canvas.update()

    def undo(self):
        if self.components.__len__() < 2:
            print("撤销组合失败")
            return
        self.canvas.components.remove(self.components[0])
        for component in self.components[1:]:
            self.components[0].remove(component)
        for component in self.components:
            self.canvas.components.append(component)
        self.canvas.update()
from PyQt5.QtWidgets import QWidget, QGridLayout, QTextEdit
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint, QRect
from src.shapes.shape_factory import ShapeFactory
from src.patterns.composite import Component
from src.components.drag_button import DragButton
from src.commands.command_status import Status
from src.commands.add_shape_command import AddShapeCommand
from src.commands.composite_command import CompositeCommand
from src.commands.paste_command import PasteCommand
from src.commands.move_command import MoveCommand
from src.commands.zoom_command import ZoomCommand
from src.commands.add_text_command import AddTextCommand

class ShapeCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.components = []
        self.status = Status()
        self.commands = []
        self.redo_commands = []
        self.drag_button = []
        self.setLayout(QGridLayout())

    def clear_button(self):
        self.on_component = None
        for button in self.drag_button:
            button.hide()
            button.deleteLater()
        self.drag_button = []

    def set_shape(self, shape):
        self.clear_button()
        self.status.set_status("shape", shape)

    def set_select(self):
        if self.status.select:
            self.status.selected_component = []
            self.update()
        self.status.set_status("select", None)

    def composite(self):
        command = CompositeCommand(self.status, self)
        command.execute()
        self.commands.append(command)
        self.redo_commands = []

    def copy(self):
        self.status.set_status("copy", None)

    def paste(self):
        command = PasteCommand(self.status, self)
        command.execute()
        self.commands.append(command)
        self.redo_commands = []

    def off(self):
        self.clear_button()
        self.status.set_status("on_component", None)

    def on(self, component):
        self.status.set_status("on_component", component)
        self.clear_button()
        x,y,w,h = component.bounding_box()
        button1 = DragButton(self, x-5,y-5)
        button2 = DragButton(self, x+w-5,y+h-5)
        self.drag_button.append(button1)
        self.drag_button.append(button2)
        button1.show()
        button2.show()

    def button_move(self, button, old_x, old_y, new_x, new_y):
        if self.status.on_component:
            idx = self.drag_button.index(button)
            dx = new_x - old_x
            dy = new_y - old_y
            self.status.set_status("drag", (dx, dy))
            if idx == 0:
                command = MoveCommand(self.status, self)
                command.execute()
                self.commands.append(command)
                self.redo_commands = []
                x,y,w,h = self.status.on_component.bounding_box()
                self.drag_button[0].move(x-5,y-5)
                self.drag_button[1].move(x+w-5,y+h-5)
            elif idx == 1:
                command = ZoomCommand(self.status, self)
                command.execute()
                self.commands.append(command)
                self.redo_commands = []
                x,y,w,h = self.status.on_component.bounding_box()
                self.drag_button[0].move(x-5,y-5)
                self.drag_button[1].move(x+w-5,y+h-5)

    def set_text(self):
        self.status.set_status("text", None)
    
    def undo(self):
        if self.commands:
            command = self.commands.pop()
            command.undo()
            self.redo_commands.append(command)
            self.update()

    def redo(self):
        if self.redo_commands:
            command = self.redo_commands.pop()
            command.execute()
            self.commands.append(command)
            self.update()

    def get_component(self, x, y):
        #倒叙遍历
        for component in self.components[::-1]:
            if component.inter_box(x, y):
                return component
        return None

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        for component in self.components:
            if component in self.status.selected_component:
                pen = QPen(QColor(Qt.red))  
                pen.setWidth(2)
                painter.setPen(pen)
            else:
                pen = QPen(QColor(Qt.black))  
                pen.setWidth(2)
                painter.setPen(pen)
            component.draw(painter)

    def mousePressEvent(self, event):
        self.status.x = event.x()
        self.status.y = event.y()
        if event.button() == Qt.LeftButton:
            if self.status.current_shape:
                command = AddShapeCommand(self.status, self)
                command.execute()
                self.commands.append(command)
                self.redo_commands = []
            elif self.status.select:
                component = self.get_component(event.x(), event.y())
                if component:
                    if component in self.status.selected_component:
                        self.status.set_status("unselect_component", component)
                        self.update()
                    else:
                        self.status.set_status("select_component", component)
                        self.update()
            elif self.status.text:
                command = AddTextCommand(self.status, self)
                command.execute()
                self.commands.append(command)
                self.redo_commands = []
            else:
                component = self.get_component(event.x(), event.y())
                if component:
                    self.on(component)
                else:
                    self.off()

    def save_drawing(self, file_name):
        # 实现保存绘图的逻辑
        pass

    def load_drawing(self, file_name):
        # 实现加载绘图的逻辑
        pass

    def personalize_settings(self, settings):
        # 实现个性化界面设置的逻辑
        pass

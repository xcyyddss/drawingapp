#实现组合模式，用于图形的组合。
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QPoint, QRect
from ..components.drag_button import DragButton

class Component(QWidget):
    def __init__(self, shape, parent=None):
        super().__init__(parent)
        self.children_shapes = [shape]
        self.drag_buttons = []
        self.setGeometry(shape.bounding_box()[0], shape.bounding_box()[1], shape.bounding_box()[2], shape.bounding_box()[3])

    def add(self, child):
        self.children_shapes.append(child)

    def remove(self, child):
        self.children_shapes.remove(child)

    def draw(self, painter):
        for child in self.children_shapes:
            child.draw(painter)

    def bounding_box(self):
        if not self.children_shapes:
            return (0, 0, 0, 0)
        x,y,width,height = self.children_shapes[0].bounding_box()
        width += x
        height += y
        for child in self.children_shapes[1:]:
            _x, _y, w, h = child.bounding_box()
            width = max(width, _x+w)
            height = max(height, _y+h)
            x = min(x, _x)
            y = min(y, _y)
        return (x, y, width-x, height-y)

    def clone(self):
        clone_component = Component(None, self.parent())
        for child in self.children_shapes:
            clone_component.add(child.clone())
        return clone_component

    def mousePressEvent(self, event):
        x,y,w,h = self.bounding_box()
        if event.button() == Qt.LeftButton:
            if event.x() > x and event.x() < x+w and event.y() > y and event.y() < y+h:
                print("mousePressEvent")
                self.create_drag_buttons()
                self.update()
            else:
                for button in self.drag_buttons:
                    button.hide()
                self.drag_buttons = []
                self.update()

    def create_drag_buttons(self):
        for button in self.drag_buttons:
            button.deleteLater()
        self.drag_buttons = []
        rect = self.bounding_box()
        # 创建四个拖拽按钮
        self.drag_buttons.append(DragButton(self, rect[0] - 15, rect[1] - 15))
        self.drag_buttons.append(DragButton(self, rect[0]+rect[2] - 15, rect[1]+rect[3] - 15))
        for button in self.drag_buttons:
            button.show()

    def update_bounding_box(self, button, delta):
        x,y,w,h = self.bounding_box()
        idx = self.drag_buttons.index(button)
        if idx == 0:
            x += delta.x()
            y += delta.y()
            self.drag_buttons[1].move(self.drag_buttons[1].pos() + delta)
            for child in self.children_shapes:
                child.move(delta.x(), delta.y())
        elif idx == 1:
            for child in self.children_shapes:
                child.zoom((w + delta.x())/w, (h + delta.y())/h)
            w += delta.x()
            h += delta.y()
        self.setGeometry(x,y,w,h)
        self.update()

    def move(self, dx, dy):
        for child in self.children_shapes:
            child.move(dx, dy)
        x,y,w,h = self.bounding_box()
        self.setGeometry(x,y,w,h)
        self.update()

    def zoom(self, factor1, factor2):
        for child in self.children_shapes:
            child.zoom(factor1, factor2)
        x,y,w,h = self.bounding_box()
        self.setGeometry(x,y,w,h)
        self.update()
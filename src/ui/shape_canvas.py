from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QPoint, QRect
from ..shapes.shape_factory import ShapeFactory
from ..patterns.composite import Component

class ShapeCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.components = []
        self.current_shape = None
        self.drawing_line = False
        self.setLayout(QGridLayout())

    def set_shape(self, shape):
        self.current_shape = shape

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        for component in self.components:
            component.draw(painter)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.current_shape:
                if self.current_shape != "line":
                    new_component = Component(ShapeFactory.create_shape(self.current_shape, event.x(), event.y(), 100, 50), self)
                    self.components.append(new_component)
                    new_component.show()
                    self.update()
                    self.current_shape = None
                elif self.current_shape == "line":
                    if not self.drawing_line:
                        self.line_start_point = (event.x(), event.y())
                        self.drawing_line = True
                    else:
                        self.drawing_line = False
                        new_component = Component(ShapeFactory.create_shape(self.current_shape, self.line_start_point[0], self.line_start_point[1], event.x(), event.y()), self)
                        self.components.append(new_component)
                        new_component.show()
                        self.update()
                        self.current_shape = None

    def save_drawing(self, file_name):
        # 实现保存绘图的逻辑
        pass

    def load_drawing(self, file_name):
        # 实现加载绘图的逻辑
        pass

    def personalize_settings(self, settings):
        # 实现个性化界面设置的逻辑
        pass

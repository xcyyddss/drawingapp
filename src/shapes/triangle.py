#定义具体的图形类，继承自shape.py。
from src.shapes.shape import Shape
from PyQt5.QtGui import QPolygon
from PyQt5.QtCore import QPoint 

class Triangle(Shape):
    def __init__(self, x, y, base, height):
        super().__init__(x, y)
        self.base = base
        self.height = height

    def draw(self, painter):
        points = [
            QPoint(self.x + self.base / 2, self.y),
            QPoint(self.x, self.y + self.height),
            QPoint(self.x + self.base, self.y + self.height)
        ]
        polygon = QPolygon(points)
        painter.drawPolygon(polygon)

    def clone(self):
        return Triangle(self.x, self.y, self.base, self.height)

    def bounding_box(self):
        return (self.x, self.y, self.base, self.height)

    def zoom(self, _x, _y, factor1, factor2):
        self.base *= factor1
        self.height *= factor2
        dx = self.x - _x
        dy = self.y - _y
        dx *= factor1
        dy *= factor2
        self.x = _x + dx
        self.y = _y + dy
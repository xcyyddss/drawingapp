#定义具体的图形类，继承自shape.py。
from .shape import Shape

class Line(Shape):
    def __init__(self, x, y, x2, y2):
        super().__init__(x, y)
        self.x2 = x2
        self.y2 = y2

    def draw(self, painter):
        painter.drawLine(self.x, self.y, self.x2, self.y2)

    def clone(self):
        return Line(self.x, self.y, self.x2, self.y2)

    def bounding_box(self):
        return (min(self.x, self.x2), min(self.y, self.y2), abs(self.x - self.x2), abs(self.y - self.y2))

    def zoom(self, factor1, factor2):
        dx = (self.x2 - self.x) * factor1
        dy = (self.y2 - self.y) * factor2
        self.x2 = self.x + dx
        self.y2 = self.y + dy
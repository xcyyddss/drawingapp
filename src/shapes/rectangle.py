#定义具体的图形类，继承自shape.py。
from src.shapes.shape import Shape

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def draw(self, painter):
        painter.drawRect(self.x, self.y, self.width, self.height)

    def clone(self):
        return Rectangle(self.x, self.y, self.width, self.height)

    def bounding_box(self):
        return (self.x, self.y, self.width, self.height)

    def zoom(self, _x, _y, factor1, factor2):
        self.width *= factor1
        self.height *= factor2
        dx = self.x - _x
        dy = self.y - _y
        dx *= factor1
        dy *= factor2
        self.x = _x + dx
        self.y = _y + dy
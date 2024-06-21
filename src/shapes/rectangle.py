#定义具体的图形类，继承自shape.py。
from .shape import Shape

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

    def zoom(self, factor1, factor2):
        self.width *= factor1
        self.height *= factor2
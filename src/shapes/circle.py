#定义具体的图形类，继承自shape.py。
from .shape import Shape

class Circle(Shape):
    def __init__(self, x, y, width):
        super().__init__(x, y)
        self.width = width

    def draw(self, painter):
        painter.drawEllipse(self.x, self.y, self.width, self.width)

    def clone(self):
        return Circle(self.x, self.y, self.width)

    def bounding_box(self):
        return (self.x, self.y, self.width, self.width)
    
    def zoom(self, factor1, factor2):
        self.width *= factor1

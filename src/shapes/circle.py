#定义具体的图形类，继承自shape.py。
from src.shapes.shape import Shape

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
    
    def zoom(self, _x, _y, factor1, factor2):
        self.width *= factor1
        dx = self.x - _x
        dy = self.y - _y
        dx *= factor1
        dy *= factor2
        self.x = _x + dx
        self.y = _y + dy

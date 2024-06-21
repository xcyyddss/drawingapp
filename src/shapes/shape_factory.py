#使用工厂模式，根据需求创建不同的图形对象。
from .triangle import Triangle
from .rectangle import Rectangle
from .ellipse import Ellipse
from .circle import Circle
from .line import Line

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, x, y, *args):
        if shape_type == "triangle":
            return Triangle(x, y, *args)
        elif shape_type == "rectangle":
            return Rectangle(x, y, *args)
        elif shape_type == "ellipse":
            return Ellipse(x, y, *args)
        elif shape_type == "circle":
            return Circle(x, y, args[0])
        elif shape_type == "line":
            return Line(x, y, *args)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

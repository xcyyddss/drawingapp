#使用工厂模式，根据需求创建不同的图形对象。
from src.shapes.triangle import Triangle
from src.shapes.rectangle import Rectangle
from src.shapes.ellipse import Ellipse
from src.shapes.circle import Circle
from src.shapes.line import Line

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

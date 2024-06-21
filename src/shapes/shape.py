#定义图形的抽象基类。
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self, painter):
        pass

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def bounding_box(self):
        pass
    
    @abstractmethod
    def zoom(self, factor1, factor2):
        pass

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

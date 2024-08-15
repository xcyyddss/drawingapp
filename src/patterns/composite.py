#实现组合模式，用于图形的组合。

class Component:
    def __init__(self, shape = None):
        self.type = "component"
        if not shape:
            self.children_shapes = []
        else:
            self.children_shapes = [shape]
        self.drag_buttons = []

    def add(self, child):
        self.children_shapes.append(child)

    def remove(self, child):
        self.children_shapes.remove(child)

    def draw(self, painter):
        for child in self.children_shapes:
            child.draw(painter)

    def bounding_box(self):
        if not self.children_shapes:
            return (0, 0, 0, 0)
        x,y,width,height = self.children_shapes[0].bounding_box()
        width += x
        height += y
        for child in self.children_shapes[1:]:
            _x, _y, w, h = child.bounding_box()
            width = max(width, _x+w)
            height = max(height, _y+h)
            x = min(x, _x)
            y = min(y, _y)
        return (x, y, width-x, height-y)
    
    def inter_box(self, x, y):
        _x,_y,w,h = self.bounding_box()
        if x > _x and x < _x+w and y > _y and y < _y+h:
            return True
        return False

    def clone(self):
        clone_component = Component()
        for child in self.children_shapes:
            clone_component.add(child.clone())
        return clone_component

    def move(self, dx, dy):
        for child in self.children_shapes:
            child.move(dx, dy)

    def zoom(self, _x, _y, factor1, factor2):
        for child in self.children_shapes:
            child.zoom(_x, _y, factor1, factor2)
class Status:
    def __init__(self):
        self.current_shape = None
        self.select = False
        self.selected_component = []
        self.on_component = None
        self.copy_component = None
        self.dx = 0
        self.dy = 0
        self.text = False

    def set_status(self, type, status):
        self.current_shape = None
        self.text = False
        if type == "shape":
            self.current_shape = status
        elif type == "select":
            self.select = not self.select
        elif type == "select_component":
            self.selected_component.append(status)
        elif type == "unselect_component":
            self.selected_component.remove(status)
        elif type == "on_component":
            self.on_component = status
        elif type == "copy":
            self.copy_component = self.on_component
        elif type == "drag":
            self.dx = status[0]
            self.dy = status[1]
        elif type == "text": 
            self.text = True
    
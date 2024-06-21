from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt

class DragButton(QPushButton):
    def __init__(self, parent, x, y):
        super().__init__(parent)
        self.setGeometry(x, y, 10, 10)
        self.setStyleSheet("background-color: red")
        self.setCursor(Qt.SizeAllCursor)
        self.old_pos = self.pos()
        self.dragging = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and not self.dragging:
            self.old_pos = event.pos()
            self.dragging = True

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.dragging:
            self.dragging = False
            delta = event.pos() - self.old_pos
            self.move(self.pos() + delta)
            self.parent().update_bounding_box(self, delta)
            self.parent().update()


    
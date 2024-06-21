from PyQt5.QtWidgets import QToolBar, QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class ToolbarPanel(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setOrientation(Qt.Horizontal)
        
        # 图形按钮
        self.add_shape_action("triangle", "resources/icons/triangle.png")
        self.add_shape_action("rectangle", "resources/icons/rectangle.png")
        self.add_shape_action("circle", "resources/icons/circle.png")
        self.add_shape_action("ellipse", "resources/icons/ellipse.png")
        self.add_shape_action("line", "resources/icons/line.png")

        # 文本框按钮
        text_action = QAction(QIcon("resources/icons/text.png"), "文本框", self)
        text_action.triggered.connect(self.add_text)
        self.addAction(text_action)

        # 组合按钮
        group_action = QAction(QIcon("resources/icons/group.png"), "组合", self)
        group_action.triggered.connect(self.group_shapes)
        self.addAction(group_action)

        # 复制按钮
        copy_action = QAction(QIcon("resources/icons/copy.png"), "复制", self)
        copy_action.triggered.connect(self.copy_shape)
        self.addAction(copy_action)

        # 粘贴按钮
        paste_action = QAction(QIcon("resources/icons/paste.png"), "粘贴", self)
        paste_action.triggered.connect(self.paste_shape)
        self.addAction(paste_action)

        # 撤销按钮
        undo_action = QAction(QIcon("resources/icons/undo.png"), "撤销", self)
        undo_action.triggered.connect(self.undo_action)
        self.addAction(undo_action)

        # 重做按钮
        redo_action = QAction(QIcon("resources/icons/redo.png"), "重做", self)
        redo_action.triggered.connect(self.redo_action)
        self.addAction(redo_action)

    def add_shape_action(self, shape, icon_path):
        action = QAction(QIcon(icon_path), shape, self)
        action.triggered.connect(lambda: self.parent().canvas.set_shape(shape))
        self.addAction(action)

    def add_text(self):
        # 实现添加文本框的逻辑
        QMessageBox.information(self, "文本框", "添加文本框功能未实现。")

    def group_shapes(self):
        # 实现组合图形的逻辑
        QMessageBox.information(self, "组合", "组合图形功能未实现。")

    def copy_shape(self):
        # 实现复制图形的逻辑
        QMessageBox.information(self, "复制", "复制图形功能未实现。")

    def paste_shape(self):
        # 实现粘贴图形的逻辑
        QMessageBox.information(self, "粘贴", "粘贴图形功能未实现。")

    def undo_action(self):
        # 实现撤销操作的逻辑
        QMessageBox.information(self, "撤销", "撤销操作功能未实现。")

    def redo_action(self):
        # 实现重做操作的逻辑
        QMessageBox.information(self, "重做", "重做操作功能未实现。")

    def save_drawing(self):
        # 实现保存绘图的逻辑
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "保存绘图", "", "PNG Files (*.png);;All Files (*)", options=options)
        if file_name:
            self.parent().canvas.save_drawing(file_name)

    def load_drawing(self):
        # 实现加载绘图的逻辑
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "加载绘图", "", "PNG Files (*.png);;All Files (*)", options=options)
        if file_name:
            self.parent().canvas.load_drawing(file_name)

#定义具体的命令类，用于添加、删除图形和撤销、重做操作。
from src.commands.command import Command
from PyQt5.QtWidgets import QTextEdit

class AddTextCommand(Command):
    def __init__(self, status, canvas):
        self.canvas = canvas
        self.status = status
        self.text = None
        self.x = status.x
        self.y = status.y

    def execute(self):
        text_box = QTextEdit(self.canvas)
        text_box.setGeometry(self.x, self.y, 100, 30)  # 设置文本框的初始大小
        text_box.show()
        text_box.setFocus()
        text_box.textChanged.connect(self.canvas.update)
        self.text = text_box
        self.status.text = False
        # 将文本框添加到组件列表中

    def undo(self):
        self.text.hide()
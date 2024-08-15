from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QAction, QFileDialog, QMessageBox
from src.ui.shape_canvas import ShapeCanvas
from src.ui.toolbar_panel import ToolbarPanel
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Drawing Application')
        self.setGeometry(100, 100, 800, 600)

        # 创建中心部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)


        # 创建绘图区域
        self.canvas = ShapeCanvas()
        layout.addWidget(self.canvas)

        # 创建工具栏
        self.toolbar = ToolbarPanel(self)
        self.addToolBar(self.toolbar)

        # 创建菜单栏
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        # 添加菜单项
        save_action = QAction(QIcon("resources/icons/save.png"),'Save', self)
        save_action.triggered.connect(self.save_drawing)
        file_menu.addAction(save_action)

        load_action = QAction(QIcon("resources/icons/load.png"),'Load', self)
        load_action.triggered.connect(self.load_drawing)
        file_menu.addAction(load_action)

        exit_action = QAction(QIcon("resources/icons/exit.png"),'Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # 个性化界面预留
        view_menu = menubar.addMenu('View')
        personalize_action = QAction('Personalize', self)
        personalize_action.triggered.connect(self.personalize_interface)
        view_menu.addAction(personalize_action)

    def save_drawing(self):
        QMessageBox.information(self, "Save", "Not implemented.")

    def load_drawing(self):
        QMessageBox.information(self, "Load", "Not implemented.")

    def personalize_interface(self):
        # 打开个性化界面的设置窗口
        QMessageBox.information(self, "Personalize", "Not implemented.")

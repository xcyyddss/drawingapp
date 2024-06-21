#这个文件是应用程序的入口点，负责启动和初始化应用程序。

from PyQt5.QtWidgets import QApplication
from .ui.main_window import MainWindow

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

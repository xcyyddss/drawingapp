from PyQt5.QtWidgets import QApplication
from src.ui.main_window import MainWindow

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

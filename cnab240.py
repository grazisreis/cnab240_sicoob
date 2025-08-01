import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow
import os

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    style_path = os.path.join(os.path.dirname(__file__), "assets", "style.qss")
    with open(style_path, "r") as f:
        app.setStyleSheet(f.read())


if __name__ == "__main__":
    main()

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from pyqt5_interface import Ui_main_window


class Window(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

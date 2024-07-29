import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow

from pyqt5_interface import Ui_main_window


class Window(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.ui.menu_folder.triggered.connect(self.selected)
        self.ui.action_save.triggered.connect(self.save)


    @QtCore.pyqtSlot(QAction)
    def selected(self, item) -> None:
        print(f"\n{item.text()} was selected")


    @QtCore.pyqtSlot()
    def save(self) -> None:
        print("\nSaving something")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

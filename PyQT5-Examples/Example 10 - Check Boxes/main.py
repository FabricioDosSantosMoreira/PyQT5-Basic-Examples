import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from pyqt5_interface import Ui_main_window


class Window(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        # Set as checked a default radio button
        self.ui.check_box_1.setChecked(True)
        
        # Set a tristate radio button
        self.ui.check_box_2.setTristate(True)

        self.ui.check_box_1.stateChanged.connect(self.change_screen_size)
        self.ui.check_box_2.stateChanged.connect(self.change_screen_title)


    @QtCore.pyqtSlot(int)
    def change_screen_size(self, state: int) -> None:
        print(f"\nActual state: {state}")
        if self.ui.check_box_1.isChecked():
            self.setGeometry(400, 150, 600, 400)
        else:
            self.setGeometry(400, 150, 400, 200)


    @QtCore.pyqtSlot(int)
    def change_screen_title(self, state: int) -> None:
        print(f"\nActual state: {state}")

        if state == QtCore.Qt.CheckState.Checked:
            self.setWindowTitle("State Checked")
        elif state == QtCore.Qt.CheckState.PartiallyChecked:
            self.setWindowTitle("State PartiallyChecked")
        else: #QtCore.Qt.CheckState.Unchecked
            self.setWindowTitle("State Unchecked")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

import sys
from typing import override

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from pyqt5_main_window import Ui_main_window
from pyqt5_secondary_window import Ui_secondary_window


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.secondary_window = SecondaryWindow(self, "Info from Main Window")
        self.ui.push_button_1.clicked.connect(self.change_window)

    
    @QtCore.pyqtSlot()
    def change_window(self) -> None:
        self.secondary_window.show()
        self.hide()


class SecondaryWindow(QMainWindow):

    def __init__(self, main_window: MainWindow, msg: str) -> None:
        super().__init__()

        self.ui = Ui_secondary_window()
        self.ui.setupUi(self)

        self.ui.plain_text_edit_1.setPlainText(msg)
        self.ui.push_button_1.clicked.connect(self.go_back)

        self.main_window = main_window


    @override
    def closeEvent(self, event) -> None:
        # Show the main window when the secondary window is closed
        self.main_window.show()

        event.accept()


    @QtCore.pyqtSlot()
    def go_back(self) -> None:
        self.main_window.show()
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QAbstractButton, QApplication, QMainWindow, QMessageBox, QPushButton

from pyqt5_interface import Ui_main_window


class Window(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.ui.push_button_1.clicked.connect(self.new_message_box)

    
    @QtCore.pyqtSlot(bool)
    def new_message_box(self) -> None:
        msg_box = QMessageBox()

        msg_box.setWindowTitle("This is a message box")
        msg_box.setText("Message box text here")

        # Sets an icon
        msg_box.setIcon(QMessageBox.Information)

        # Sets extra text
        msg_box.setInformativeText("Message box info text here")
        
        # Sets default buttons to the message box
        msg_box.setStandardButtons(
            QMessageBox.StandardButton.Abort | 
            QMessageBox.StandardButton.Yes | 
            QMessageBox.StandardButton.No
        )
        
        # Set a default button
        msg_box.setDefaultButton(QMessageBox.StandardButton.Abort)

        # Sets an escape button
        msg_box.setEscapeButton(QMessageBox.StandardButton.No)

        # Sets an additional info
        msg_box.setDetailedText("Message box extra info")

        msg_box.buttonClicked.connect(self.msg_box_result)
        msg_box_return = msg_box.exec()

    
    @QtCore.pyqtSlot(QAbstractButton)
    def msg_box_result(self, button: QPushButton) -> None:
        print(f"\nMessage box button clicked: {button.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

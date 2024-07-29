import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from pyqt5_interface import Ui_main_window


class Window(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)
 
        # Set a placeholder text in 'plain_text_edit_1'
        self.ui.plain_text_edit_1.setPlaceholderText("Insert here your text")

        # Set a default text in 'plain_text_edit_1'
        self.ui.plain_text_edit_1.setPlainText("Default text")

        # Set read-only property for 'plain_text_edit_1'
        self.ui.plain_text_edit_1.setReadOnly(False)

        # Disable undo/redo options for 'plain_text_edit_1'
        self.ui.plain_text_edit_1.setUndoRedoEnabled(False)

        # Connect button click to insert_text method
        self.ui.push_button_1.clicked.connect(self.insert_text)

        # Connect text change event to plain_text_changed method
        self.ui.plain_text_edit_1.textChanged.connect(self.plain_text_changed)


    @QtCore.pyqtSlot(bool)
    def insert_text(self) -> None:
        self.ui.plain_text_edit_1.clear()
        self.ui.plain_text_edit_1.insertPlainText("Setting a text to plain text edit from a button")


    @QtCore.pyqtSlot()
    def plain_text_changed(self) -> None:
        print("\nPlain text edit was chaged!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

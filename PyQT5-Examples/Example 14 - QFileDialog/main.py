import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

from pyqt5_interface import Ui_main_window


class Window(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.ui.action_text_file.triggered.connect(self.open_text_file)
        self.ui.action_any_file.triggered.connect(self.open_any_file)
        self.ui.action_save.triggered.connect(self.save_text)


    @QtCore.pyqtSlot()
    def open_text_file(self) -> None:
        path: str
        filter: str

        path, filter = QFileDialog.getOpenFileName(
        parent=self, 
        caption="Open text file", 
        directory="C:\\", 
        filter="Text (*.txt)"
        )

        print(f"\nSelected from: {path} with filter: {filter}")

        if path:
            with open(path, 'r', encoding='UTF-8') as file:
                info = file.read()
                self.ui.plain_text_edit_1.setPlainText(info)


    @QtCore.pyqtSlot()
    def open_any_file(self) -> None:
        path: str
        filter: str

        path, filter = QFileDialog.getOpenFileName(
            parent=self, 
            caption="Open any file", 
            directory="C:\\", 
            filter="All files (*.*)"
        )

        print(f"\nSelected from: {path} with filter: {filter}")

        if path:
            try:
                with open(path, 'r', encoding='UTF-8') as file:
                    info = file.read()
                    self.ui.plain_text_edit_1.appendPlainText(f"\nContent of {path}\n{info}")

            except Exception as e:
                print(f"\nError opening file {path}: {e}")
                self.ui.plain_text_edit_1.appendPlainText(f"\nCould not open {path}")


    @QtCore.pyqtSlot()
    def save_text(self) -> None:
        text_content: str = self.ui.plain_text_edit_1.toPlainText()

        path, filter = QFileDialog.getSaveFileName(
            parent=self, 
            caption="Save text", 
            directory="C:\\",
            filter="Text (*.txt)"
        )

        print(f"\nSaving file as {path}")

        if path:
            with open(path, "w", encoding='UTF-8') as file:
                file.write(path)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

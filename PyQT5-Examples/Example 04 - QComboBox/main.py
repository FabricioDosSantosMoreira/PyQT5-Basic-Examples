import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from pyqt5_interface import Ui_main_window


class Window(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        # NOTE: Adds multiple items to 'combo_box_1'
        options = ["Some option 1", "Some option 2"]
        self.ui.combo_box_1.addItems(options)

        # NOTE: Removes "Option 3"
        self.index = self.ui.combo_box_1.findText("Option 3", QtCore.Qt.MatchFlag.MatchCaseSensitive)
        self.ui.combo_box_1.removeItem(self.index)

        # Mapping changes in 'combo_box_1'
        self.ui.combo_box_1.currentIndexChanged.connect(self.combo_box_changed)
        self.ui.combo_box_1.activated[str].connect(self.combo_box_activated)

        # Mapping changes in 'combo_box_2'
        self.ui.combo_box_2.currentTextChanged.connect(self.ui.line_edit_1.setText)


    @QtCore.pyqtSlot(int)
    def combo_box_changed(self, index: int) -> None:
        print(f"\nSelected: {self.ui.combo_box_1.itemText(index)}")


    @QtCore.pyqtSlot(str)
    def combo_box_activated(self, value: str) -> None:
        print(f"\nCombo box was activated!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

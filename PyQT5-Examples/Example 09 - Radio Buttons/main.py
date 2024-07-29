import sys
from pathlib import Path

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

from pyqt5_interface import Ui_main_window

ICON_PATH: Path = Path(__file__).parent / "hd_icon.png"


class Window(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        # Adding an icon to 'radio_button_1'
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(str(ICON_PATH)), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ui.radio_button_1.setIcon(icon)  
        self.ui.radio_button_1.setIconSize(QtCore.QSize(20, 20))

        # Set as checked a default radio button
        self.ui.radio_button_1.setChecked(True)

        self.ui.radio_button_1.toggled.connect(self.state_changed)
        self.ui.radio_button_2.toggled.connect(self.state_changed)
        self.ui.radio_button_3.toggled.connect(self.state_changed)


    @QtCore.pyqtSlot(bool)
    def state_changed(self) -> None:
        radio_button_selected: QtCore.QObject = self.sender()

        print(f"\nChanged to: {radio_button_selected.objectName()}")
        print(f"Is radio button selected? {bool(radio_button_selected.isChecked)}")

        if radio_button_selected.isChecked:
            self.ui.out_label.setText(f"Selected: {radio_button_selected.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

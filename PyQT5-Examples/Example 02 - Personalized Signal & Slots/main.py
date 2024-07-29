import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from pyqt5_interface import Ui_main_window


class PersonalizedSignals(QtCore.QObject):

    # if 'name' isn't set 'pyqtSignal' takes the variable name
    signal_1 = QtCore.pyqtSignal()
    signal_2 = QtCore.pyqtSignal(str, name="String Signal")


class Window(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.signals = PersonalizedSignals()
        
        # NOTE: To conect a signal to a slot do the following:
        # self.object.signal.connect(self.slot)
        self.ui.push_button.clicked.connect(self.personalized_slot)


    # NOTE: Using the 'pyqtSlot' decorator marks the method as a slot
    @QtCore.pyqtSlot()
    def personalized_slot(self) -> None:
        print("\nPush Button clicked!")

        self.signals.signal_1.connect(self.recieve_signal_1)
        self.signals.signal_1.emit()
        self.signals.signal_1.disconnect()

        self.signals.signal_2.connect(self.recieve_signal_2)
        self.signals.signal_2.emit("Signal 2 emmited!")
        self.signals.signal_2.disconnect()


    @QtCore.pyqtSlot()
    def recieve_signal_1(self) -> None:
        print("\nSignal 1 was recieved and emmited with success!")


    @QtCore.pyqtSlot(str)  
    def recieve_signal_2(self, value: str) -> None:
        print(f"\nValue recieved: {value}")
        print("Signal 2 was recieved and emmited with success!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

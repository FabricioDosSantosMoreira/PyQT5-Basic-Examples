# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file ''
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_secondary_window(object):

    def setupUi(self, secondary_window) -> None:

        secondary_window.setObjectName("secondary_window")
        secondary_window.resize(400, 200)

        self.central_widget = QtWidgets.QWidget(secondary_window)
        self.central_widget.setObjectName("central_widget")
        secondary_window.setCentralWidget(self.central_widget)

        self.push_button_1 = QtWidgets.QPushButton(self.central_widget)
        self.push_button_1.setGeometry(QtCore.QRect(70, 119, 250, 31))
        self.push_button_1.setObjectName("push_button_1")

        self.plain_text_edit_1 = QtWidgets.QPlainTextEdit(self.central_widget)
        self.plain_text_edit_1.setGeometry(QtCore.QRect(70, 10, 250, 70))
        self.plain_text_edit_1.setObjectName("plainTextEdit")

        self.menu_bar = QtWidgets.QMenuBar(secondary_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menu_bar.setObjectName("menu_bar")
        secondary_window.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(secondary_window)
        self.status_bar.setObjectName("status_bar")
        secondary_window.setStatusBar(self.status_bar)

        self.retranslateUi(secondary_window)

        QtCore.QMetaObject.connectSlotsByName(secondary_window)


    def retranslateUi(self, secondary_window) -> None:
        _translate = QtCore.QCoreApplication.translate

        secondary_window.setWindowTitle(_translate("secondary_window", "Secondary Window"))

        self.push_button_1.setText(_translate("secondary_window", "Go back"))
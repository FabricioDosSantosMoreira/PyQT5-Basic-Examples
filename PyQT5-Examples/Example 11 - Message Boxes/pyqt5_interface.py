# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file ''
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):

    def setupUi(self, main_window) -> None:

        main_window.setObjectName("main_window")
        main_window.resize(400, 200)
        
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        main_window.setCentralWidget(self.central_widget)

        self.push_button_1 = QtWidgets.QPushButton(self.central_widget)
        self.push_button_1.setGeometry(QtCore.QRect(120, 60, 151, 41))
        self.push_button_1.setObjectName("push_button_1")

        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menu_bar.setObjectName("menu_bar")
        main_window.setMenuBar(self.menu_bar)
        
        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("status_bar")
        main_window.setStatusBar(self.status_bar)

        self.retranslateUi(main_window)

        QtCore.QMetaObject.connectSlotsByName(main_window)


    def retranslateUi(self, main_window) -> None:
        _translate = QtCore.QCoreApplication.translate

        main_window.setWindowTitle(_translate("main_window", "Main Window"))
        self.push_button_1.setText(_translate("main_window", "Push button 1"))

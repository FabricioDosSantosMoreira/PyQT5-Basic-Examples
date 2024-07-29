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
        main_window.resize(600, 400)

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        main_window.setCentralWidget(self.central_widget)

        self.plain_text_edit_1 = QtWidgets.QPlainTextEdit(self.central_widget)
        self.plain_text_edit_1.setGeometry(QtCore.QRect(20, 20, 561, 321))
        self.plain_text_edit_1.setObjectName("plain_text_edit_1")

        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menu_bar.setObjectName("menu_bar")
        main_window.setMenuBar(self.menu_bar)

        self.menu_options = QtWidgets.QMenu(self.menu_bar)
        self.menu_options.setObjectName("menu_options")

        self.menu_open = QtWidgets.QMenu(self.menu_options)
        self.menu_open.setObjectName("menu_open")

        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("status_bar")
        main_window.setStatusBar(self.status_bar)

        self.action_save = QtWidgets.QAction(main_window)
        self.action_save.setObjectName("action_save")

        self.action_text_file = QtWidgets.QAction(main_window)
        self.action_text_file.setObjectName("action_text_file")

        self.action_any_file = QtWidgets.QAction(main_window)
        self.action_any_file.setObjectName("action_any_file")

        self.menu_open.addAction(self.action_text_file)
        self.menu_open.addAction(self.action_any_file)

        self.menu_options.addAction(self.menu_open.menuAction())
        self.menu_options.addAction(self.action_save)

        self.menu_bar.addAction(self.menu_options.menuAction())

        self.retranslateUi(main_window)

        QtCore.QMetaObject.connectSlotsByName(main_window)


    def retranslateUi(self, main_window) -> None:
        _translate = QtCore.QCoreApplication.translate

        main_window.setWindowTitle(_translate("main_window", "Main Window"))

        self.menu_options.setTitle(_translate("main_window", "Options"))
        self.menu_open.setTitle(_translate("main_window", "Open"))

        self.action_save.setText(_translate("main_window", "Save"))
        self.action_save.setShortcut(_translate("main_window", "Ctrl+S"))

        self.action_text_file.setText(_translate("main_window", "Text file"))
        self.action_text_file.setShortcut(_translate("main_window", "Ctrl+T"))

        self.action_any_file.setText(_translate("main_window", "Any file"))
        self.action_any_file.setShortcut(_translate("main_window", "Ctrl+O"))
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

        self.formLayoutWidget = QtWidgets.QWidget(self.central_widget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(90, 130, 411, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        self.form_layout_1 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.form_layout_1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.form_layout_1.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.form_layout_1.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.form_layout_1.setLabelAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.form_layout_1.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.form_layout_1.setContentsMargins(0, 0, 0, 0)
        self.form_layout_1.setObjectName("form_layout_1")

        self.label_1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.form_layout_1.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_1)

        self.line_edit_1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_edit_1.setObjectName("line_edit_1")
        self.form_layout_1.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_edit_1)

        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.form_layout_1.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)

        self.line_edit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_edit_2.setObjectName("line_edit_2")
        self.form_layout_1.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_edit_2)

        self.push_button_1 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_button_1.setObjectName("push_button_1")
        self.form_layout_1.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.push_button_1)

        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 600, 21))
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

        self.label_1.setText(_translate("main_window", "Name"))
        self.label_2.setText(_translate("main_window", "Phone"))

        self.push_button_1.setText(_translate("main_window", "Push button 1"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aviso.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 240)
        self.btnBoxAviso = QtWidgets.QDialogButtonBox(Dialog)
        self.btnBoxAviso.setGeometry(QtCore.QRect(100, 180, 151, 32))
        self.btnBoxAviso.setOrientation(QtCore.Qt.Horizontal)
        self.btnBoxAviso.setStandardButtons(QtWidgets.QDialogButtonBox.No | QtWidgets.QDialogButtonBox.Yes)
        self.btnBoxAviso.setObjectName("btnBoxAviso")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 120, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 30, 47, 13))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.btnBoxAviso.accepted.connect(Dialog.accept)
        self.btnBoxAviso.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Desea Salir?"))

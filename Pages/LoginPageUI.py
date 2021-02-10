# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/LoginPageUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(800, 600)
        Login.setMinimumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        Login.setFont(font)
        self.lbl_title = QtWidgets.QLabel(Login)
        self.lbl_title.setGeometry(QtCore.QRect(210, 10, 401, 80))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: rgb(85, 170, 255);")
        self.lbl_title.setObjectName("lbl_title")
        self.btn_register = QtWidgets.QPushButton(Login)
        self.btn_register.setGeometry(QtCore.QRect(30, 520, 160, 55))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        font.setUnderline(True)
        self.btn_register.setFont(font)
        self.btn_register.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_register.setStyleSheet("border: 1px solid black;\n"
"color: rgb(85, 170, 255);")
        self.btn_register.setObjectName("btn_register")
        self.btn_sigIn = QtWidgets.QPushButton(Login)
        self.btn_sigIn.setGeometry(QtCore.QRect(610, 520, 160, 55))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        font.setUnderline(True)
        self.btn_sigIn.setFont(font)
        self.btn_sigIn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sigIn.setStyleSheet("border: 1px solid black;\n"
"color: rgb(85, 170, 255);")
        self.btn_sigIn.setObjectName("btn_sigIn")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Login)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 230, 491, 117))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_username = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_username.setObjectName("lbl_username")
        self.verticalLayout.addWidget(self.lbl_username)
        self.lbl_password = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_password.setObjectName("lbl_password")
        self.verticalLayout.addWidget(self.lbl_password)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_username = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.txt_username.setObjectName("txt_username")
        self.verticalLayout_2.addWidget(self.txt_username)
        self.txt_password = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.txt_password.setObjectName("txt_password")
        self.verticalLayout_2.addWidget(self.txt_password)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.btn_back = QtWidgets.QPushButton(Login)
        self.btn_back.setGeometry(QtCore.QRect(440, 520, 160, 55))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        font.setUnderline(True)
        self.btn_back.setFont(font)
        self.btn_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_back.setStyleSheet("border: 1px solid black;\n"
"color: rgb(85, 170, 255);")
        self.btn_back.setObjectName("btn_back")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Term Spors Complex"))
        self.lbl_title.setText(_translate("Login", "A or M Login"))
        self.btn_register.setText(_translate("Login", "Register"))
        self.btn_sigIn.setText(_translate("Login", "Sign-In"))
        self.lbl_username.setText(_translate("Login", "Username:"))
        self.lbl_password.setText(_translate("Login", "Password:"))
        self.btn_back.setText(_translate("Login", "Back"))

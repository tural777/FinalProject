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
        Login.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        Login.setFont(font)
        Login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lbl_title = QtWidgets.QLabel(Login)
        self.lbl_title.setGeometry(QtCore.QRect(220, 10, 401, 80))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: #9E9E9E;")
        self.lbl_title.setObjectName("lbl_title")
        self.btn_register = QtWidgets.QPushButton(Login)
        self.btn_register.setGeometry(QtCore.QRect(30, 525, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setUnderline(False)
        self.btn_register.setFont(font)
        self.btn_register.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_register.setStyleSheet("QPushButton{\n"
"    border: 2px solid #9E9E9E;\n"
"    border-radius: 15px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"    color: #FFFFFF;\n"
"}\n"
"QPushButton:hover{\n"
"    color: #9E9E9E;\n"
"    background-color: #5a5a5a;\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #9c2219;\n"
"}\n"
"QPushButton:checked{\n"
"    color: #2c998e;\n"
"}")
        self.btn_register.setObjectName("btn_register")
        self.btn_sigIn = QtWidgets.QPushButton(Login)
        self.btn_sigIn.setGeometry(QtCore.QRect(590, 525, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setUnderline(False)
        self.btn_sigIn.setFont(font)
        self.btn_sigIn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sigIn.setStyleSheet("QPushButton{\n"
"    border: 2px solid #9E9E9E;\n"
"    border-radius: 15px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"    color: #FFFFFF;\n"
"}\n"
"QPushButton:hover{\n"
"    color: #9E9E9E;\n"
"    background-color: #5a5a5a;\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #9c2219;\n"
"}\n"
"QPushButton:checked{\n"
"    color: #2c998e;\n"
"}")
        self.btn_sigIn.setObjectName("btn_sigIn")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Login)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(170, 230, 451, 117))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_username = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_username.setFont(font)
        self.lbl_username.setObjectName("lbl_username")
        self.verticalLayout.addWidget(self.lbl_username)
        self.lbl_password = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_password.setFont(font)
        self.lbl_password.setObjectName("lbl_password")
        self.verticalLayout.addWidget(self.lbl_password)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_username = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        self.txt_username.setFont(font)
        self.txt_username.setStyleSheet("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}")
        self.txt_username.setObjectName("txt_username")
        self.verticalLayout_2.addWidget(self.txt_username)
        self.txt_password = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        self.txt_password.setFont(font)
        self.txt_password.setStyleSheet("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setObjectName("txt_password")
        self.verticalLayout_2.addWidget(self.txt_password)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.btn_back = QtWidgets.QPushButton(Login)
        self.btn_back.setGeometry(QtCore.QRect(400, 525, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setUnderline(False)
        self.btn_back.setFont(font)
        self.btn_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_back.setStyleSheet("QPushButton{\n"
"    border: 2px solid #9E9E9E;\n"
"    border-radius: 15px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"    color: #FFFFFF;\n"
"}\n"
"QPushButton:hover{\n"
"    color: #9E9E9E;\n"
"    background-color: #5a5a5a;\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #9c2219;\n"
"}\n"
"QPushButton:checked{\n"
"    color: #2c998e;\n"
"}")
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

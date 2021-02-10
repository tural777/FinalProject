# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/RegistrationPageUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Registration(object):
    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.resize(800, 600)
        Registration.setMinimumSize(QtCore.QSize(800, 600))
        Registration.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        Registration.setFont(font)
        Registration.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lbl_title = QtWidgets.QLabel(Registration)
        self.lbl_title.setGeometry(QtCore.QRect(230, 10, 331, 80))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: #9E9E9E;")
        self.lbl_title.setObjectName("lbl_title")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Registration)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 110, 601, 389))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_name.setFont(font)
        self.lbl_name.setObjectName("lbl_name")
        self.verticalLayout.addWidget(self.lbl_name)
        self.lbl_surname = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_surname.setFont(font)
        self.lbl_surname.setObjectName("lbl_surname")
        self.verticalLayout.addWidget(self.lbl_surname)
        self.lbl_birthDate = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_birthDate.setFont(font)
        self.lbl_birthDate.setObjectName("lbl_birthDate")
        self.verticalLayout.addWidget(self.lbl_birthDate)
        self.lbl_code = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_code.setFont(font)
        self.lbl_code.setObjectName("lbl_code")
        self.verticalLayout.addWidget(self.lbl_code)
        self.lbl_username = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_username.setFont(font)
        self.lbl_username.setObjectName("lbl_username")
        self.verticalLayout.addWidget(self.lbl_username)
        self.lbl_password = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_password.setFont(font)
        self.lbl_password.setObjectName("lbl_password")
        self.verticalLayout.addWidget(self.lbl_password)
        self.lbl_confirmPass = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_confirmPass.setFont(font)
        self.lbl_confirmPass.setObjectName("lbl_confirmPass")
        self.verticalLayout.addWidget(self.lbl_confirmPass)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_name = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        self.txt_name.setFont(font)
        self.txt_name.setStyleSheet("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}")
        self.txt_name.setObjectName("txt_name")
        self.verticalLayout_2.addWidget(self.txt_name)
        self.txt_surname = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        self.txt_surname.setFont(font)
        self.txt_surname.setStyleSheet("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}")
        self.txt_surname.setObjectName("txt_surname")
        self.verticalLayout_2.addWidget(self.txt_surname)
        self.txt_birthDate = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        self.txt_birthDate.setFont(font)
        self.txt_birthDate.setStyleSheet("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}")
        self.txt_birthDate.setObjectName("txt_birthDate")
        self.verticalLayout_2.addWidget(self.txt_birthDate)
        self.txt_code = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        self.txt_code.setFont(font)
        self.txt_code.setStyleSheet("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}")
        self.txt_code.setObjectName("txt_code")
        self.verticalLayout_2.addWidget(self.txt_code)
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
        self.txt_confirmPass = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        self.txt_confirmPass.setFont(font)
        self.txt_confirmPass.setStyleSheet("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}")
        self.txt_confirmPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_confirmPass.setObjectName("txt_confirmPass")
        self.verticalLayout_2.addWidget(self.txt_confirmPass)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.btn_submit = QtWidgets.QPushButton(Registration)
        self.btn_submit.setGeometry(QtCore.QRect(590, 525, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setUnderline(False)
        self.btn_submit.setFont(font)
        self.btn_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_submit.setStyleSheet("QPushButton{\n"
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
        self.btn_submit.setObjectName("btn_submit")
        self.btn_back = QtWidgets.QPushButton(Registration)
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

        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)

    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Term Spors Complex"))
        self.lbl_title.setText(_translate("Registration", "Registration"))
        self.lbl_name.setText(_translate("Registration", "Name:"))
        self.lbl_surname.setText(_translate("Registration", "Surname:"))
        self.lbl_birthDate.setText(_translate("Registration", "Birth Date:"))
        self.lbl_code.setText(_translate("Registration", "Code:"))
        self.lbl_username.setText(_translate("Registration", "Username:"))
        self.lbl_password.setText(_translate("Registration", "Password:"))
        self.lbl_confirmPass.setText(_translate("Registration", "Confirm Password:"))
        self.btn_submit.setText(_translate("Registration", "Submit"))
        self.btn_back.setText(_translate("Registration", "Back"))

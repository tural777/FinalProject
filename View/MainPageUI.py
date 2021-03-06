# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/MainPageUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.setEnabled(True)
        Main.resize(800, 600)
        Main.setMinimumSize(QtCore.QSize(800, 600))
        Main.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        Main.setFont(font)
        Main.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Main.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_login = QtWidgets.QLabel(self.centralwidget)
        self.lbl_login.setGeometry(QtCore.QRect(500, 140, 181, 91))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_login.setFont(font)
        self.lbl_login.setAutoFillBackground(False)
        self.lbl_login.setStyleSheet("color: #9E9E9E;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lbl_login.setObjectName("lbl_login")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(450, 270, 291, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_admin = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_admin.sizePolicy().hasHeightForWidth())
        self.btn_admin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        font.setUnderline(False)
        self.btn_admin.setFont(font)
        self.btn_admin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_admin.setStyleSheet("QPushButton{\n"
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
        self.btn_admin.setObjectName("btn_admin")
        self.horizontalLayout.addWidget(self.btn_admin)
        self.btn_member = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_member.sizePolicy().hasHeightForWidth())
        self.btn_member.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        font.setUnderline(False)
        self.btn_member.setFont(font)
        self.btn_member.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_member.setStyleSheet("QPushButton{\n"
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
        self.btn_member.setObjectName("btn_member")
        self.horizontalLayout.addWidget(self.btn_member)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.frame.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 230, 191, 131))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("UI\\../Icons/login.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lbl_login_title = QtWidgets.QLabel(self.frame)
        self.lbl_login_title.setGeometry(QtCore.QRect(40, 80, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_login_title.setFont(font)
        self.lbl_login_title.setAutoFillBackground(False)
        self.lbl_login_title.setStyleSheet("color: white;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lbl_login_title.setObjectName("lbl_login_title")
        self.frame.raise_()
        self.lbl_login.raise_()
        self.horizontalLayoutWidget.raise_()
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Term Spors Complex"))
        self.lbl_login.setText(_translate("Main", "Login"))
        self.btn_admin.setText(_translate("Main", "Admin"))
        self.btn_member.setText(_translate("Main", "Member"))
        self.lbl_login_title.setText(_translate("Main", "Term Sport Complex"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/MemberMainPageUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MemberMain(object):
    def setupUi(self, MemberMain):
        MemberMain.setObjectName("MemberMain")
        MemberMain.resize(800, 600)
        MemberMain.setMinimumSize(QtCore.QSize(800, 600))
        MemberMain.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        MemberMain.setFont(font)
        MemberMain.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lbl_title = QtWidgets.QLabel(MemberMain)
        self.lbl_title.setGeometry(QtCore.QRect(210, -10, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: #9E9E9E;")
        self.lbl_title.setObjectName("lbl_title")
        self.label = QtWidgets.QLabel(MemberMain)
        self.label.setGeometry(QtCore.QRect(240, 50, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_notices = QtWidgets.QPushButton(MemberMain)
        self.btn_notices.setGeometry(QtCore.QRect(30, 525, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setUnderline(False)
        self.btn_notices.setFont(font)
        self.btn_notices.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_notices.setStyleSheet("QPushButton{\n"
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
        self.btn_notices.setObjectName("btn_notices")
        self.btn_viewReport = QtWidgets.QPushButton(MemberMain)
        self.btn_viewReport.setGeometry(QtCore.QRect(590, 525, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setUnderline(False)
        self.btn_viewReport.setFont(font)
        self.btn_viewReport.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_viewReport.setStyleSheet("QPushButton{\n"
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
        self.btn_viewReport.setObjectName("btn_viewReport")
        self.tableWidget = QtWidgets.QTableWidget(MemberMain)
        self.tableWidget.setGeometry(QtCore.QRect(30, 170, 741, 351))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.comboBox_Type = QtWidgets.QComboBox(MemberMain)
        self.comboBox_Type.setGeometry(QtCore.QRect(90, 128, 181, 35))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.comboBox_Type.setFont(font)
        self.comboBox_Type.setStyleSheet("QFontComboBox {\n"
"      border: 1px solid gray;\n"
"      border-radius: 13px;\n"
"}")
        self.comboBox_Type.setObjectName("comboBox_Type")
        self.comboBox_Teacher = QtWidgets.QComboBox(MemberMain)
        self.comboBox_Teacher.setGeometry(QtCore.QRect(400, 128, 180, 35))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.comboBox_Teacher.setFont(font)
        self.comboBox_Teacher.setStyleSheet("QFontComboBox::down-arrow {\n"
"      image: url(:/buttons/Icons/down_arrow.png);\n"
"}\n"
" \n"
"QFontComboBox {\n"
"      border: 1px solid gray;\n"
"      border-radius: 3px;\n"
"}")
        self.comboBox_Teacher.setDuplicatesEnabled(True)
        self.comboBox_Teacher.setObjectName("comboBox_Teacher")
        self.comboBox_Price = QtWidgets.QComboBox(MemberMain)
        self.comboBox_Price.setGeometry(QtCore.QRect(680, 128, 91, 35))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.comboBox_Price.setFont(font)
        self.comboBox_Price.setStyleSheet("QFontComboBox::down-arrow {\n"
"      image: url(:/buttons/Icons/down_arrow.png);\n"
"}\n"
" \n"
"QFontComboBox {\n"
"      border: 1px solid gray;\n"
"      border-radius: 3px;\n"
"}")
        self.comboBox_Price.setDuplicatesEnabled(True)
        self.comboBox_Price.setObjectName("comboBox_Price")
        self.label_Price = QtWidgets.QLabel(MemberMain)
        self.label_Price.setGeometry(QtCore.QRect(620, 128, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Price.setFont(font)
        self.label_Price.setStyleSheet("color: rgb(100, 100, 200);")
        self.label_Price.setObjectName("label_Price")
        self.label_Teacher = QtWidgets.QLabel(MemberMain)
        self.label_Teacher.setGeometry(QtCore.QRect(310, 128, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Teacher.setFont(font)
        self.label_Teacher.setStyleSheet("color: rgb(100, 100, 200);")
        self.label_Teacher.setObjectName("label_Teacher")
        self.label_Type = QtWidgets.QLabel(MemberMain)
        self.label_Type.setGeometry(QtCore.QRect(30, 128, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Type.setFont(font)
        self.label_Type.setStyleSheet("color: rgb(100, 100, 200);")
        self.label_Type.setObjectName("label_Type")

        self.retranslateUi(MemberMain)
        QtCore.QMetaObject.connectSlotsByName(MemberMain)

    def retranslateUi(self, MemberMain):
        _translate = QtCore.QCoreApplication.translate
        MemberMain.setWindowTitle(_translate("MemberMain", "Term Spors Complex"))
        self.lbl_title.setText(_translate("MemberMain", "Member Main Page"))
        self.label.setText(_translate("MemberMain", "Upcoming Class Schedules"))
        self.btn_notices.setText(_translate("MemberMain", "Notices"))
        self.btn_viewReport.setText(_translate("MemberMain", "View Report"))
        self.comboBox_Type.setPlaceholderText(_translate("MemberMain", "Place"))
        self.comboBox_Teacher.setPlaceholderText(_translate("MemberMain", "Type"))
        self.comboBox_Price.setPlaceholderText(_translate("MemberMain", "Type"))
        self.label_Price.setText(_translate("MemberMain", "Price"))
        self.label_Teacher.setText(_translate("MemberMain", "Teacher"))
        self.label_Type.setText(_translate("MemberMain", "Type"))

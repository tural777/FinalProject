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
        self.lbl_title = QtWidgets.QLabel(MemberMain)
        self.lbl_title.setGeometry(QtCore.QRect(140, 10, 521, 80))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: rgb(85, 170, 255);")
        self.lbl_title.setObjectName("lbl_title")
        self.label = QtWidgets.QLabel(MemberMain)
        self.label.setGeometry(QtCore.QRect(210, 90, 371, 81))
        self.label.setObjectName("label")
        self.btn_Notices = QtWidgets.QPushButton(MemberMain)
        self.btn_Notices.setGeometry(QtCore.QRect(30, 525, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setUnderline(False)
        self.btn_Notices.setFont(font)
        self.btn_Notices.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Notices.setStyleSheet("QPushButton{\n"
"    border: 2px solid #9E9E9E;\n"
"    border-radius: 15px;\n"
"    background-color: #00000000;\n"
"    color: #9E9E9E;\n"
"}\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
"    background-color: #5a5a5a;\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #9c2219;\n"
"}\n"
"QPushButton:checked{\n"
"    color: #2c998e;\n"
"}")
        self.btn_Notices.setObjectName("btn_Notices")
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
"    background-color: #00000000;\n"
"    color: #9E9E9E;\n"
"}\n"
"QPushButton:hover{\n"
"    color: #FFFFFF;\n"
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
        self.tableWidget.setGeometry(QtCore.QRect(30, 170, 741, 331))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)

        self.retranslateUi(MemberMain)
        QtCore.QMetaObject.connectSlotsByName(MemberMain)

    def retranslateUi(self, MemberMain):
        _translate = QtCore.QCoreApplication.translate
        MemberMain.setWindowTitle(_translate("MemberMain", "Term Spors Complex"))
        self.lbl_title.setText(_translate("MemberMain", "Member Main Page"))
        self.label.setText(_translate("MemberMain", "Upcoming Class Schedules"))
        self.btn_Notices.setText(_translate("MemberMain", "Notices"))
        self.btn_viewReport.setText(_translate("MemberMain", "View Report"))

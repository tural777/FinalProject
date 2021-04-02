# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/AddNoticePageUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddNotice(object):
    def setupUi(self, AddNotice):
        AddNotice.setObjectName("AddNotice")
        AddNotice.resize(800, 600)
        AddNotice.setMinimumSize(QtCore.QSize(800, 600))
        AddNotice.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        AddNotice.setFont(font)
        AddNotice.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalLayoutWidget = QtWidgets.QWidget(AddNotice)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 220, 451, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_date = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_date.setFont(font)
        self.lbl_date.setObjectName("lbl_date")
        self.verticalLayout.addWidget(self.lbl_date)
        self.lbl_notice = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_notice.setFont(font)
        self.lbl_notice.setObjectName("lbl_notice")
        self.verticalLayout.addWidget(self.lbl_notice)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_date = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_date.sizePolicy().hasHeightForWidth())
        self.txt_date.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        self.txt_date.setFont(font)
        self.txt_date.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txt_date.setStyleSheet("QDateEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"width:25px;\n"
"border: 1px solid gray;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"      height: 55px;\n"
"      width: 100px;\n"
"      color: white;\n"
"      font-size: 16px;\n"
"      icon-size: 28px, 28px;\n"
"      background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333);\n"
"  }\n"
"  QCalendarWidget QMenu {\n"
"      width: 100px;\n"
"      left: 20px;\n"
"      color: white;\n"
"      font-size: 16px;\n"
"      background-color: rgb(100, 100, 200);\n"
"  }\n"
"  QCalendarWidget QSpinBox { \n"
"      width: 100px; \n"
"      font-size:16px; \n"
"      color: white; \n"
"      background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); \n"
"      selection-background-color: rgb(136, 136, 136);\n"
"      selection-color: rgb(255, 255, 255);\n"
"  }\n"
"  QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:35px; }\n"
"  QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:35px;}\n"
"  QCalendarWidget QSpinBox::up-arrow { width:46px;  height:46px; }\n"
"  QCalendarWidget QSpinBox::down-arrow { width:46px;  height:46px; }\n"
"   \n"
"  /* header row */\n"
"  QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); }\n"
"   \n"
"  /* normal days */\n"
"  QCalendarWidget QAbstractItemView:enabled \n"
"  {\n"
"      font-size:16px;  \n"
"      color: rgb(180, 180, 180);  \n"
"      background-color: rgb(235, 235, 235);\n"
"      selection-background-color: rgb(100, 100, 200); \n"
"    selection-color: white; \n"
"  \n"
"  }\n"
"   \n"
"  /* days in other months */\n"
"  /* navigation bar */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar\n"
"{ \n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); \n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{ \n"
"color: rgb(64, 64, 64); \n"
"}")
        self.txt_date.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_date.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.txt_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.txt_date.setCalendarPopup(True)
        self.txt_date.setObjectName("txt_date")
        self.verticalLayout_2.addWidget(self.txt_date)
        self.txt_notice = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        self.txt_notice.setFont(font)
        self.txt_notice.setStyleSheet("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}")
        self.txt_notice.setClearButtonEnabled(True)
        self.txt_notice.setObjectName("txt_notice")
        self.verticalLayout_2.addWidget(self.txt_notice)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.lbl_title = QtWidgets.QLabel(AddNotice)
        self.lbl_title.setGeometry(QtCore.QRect(240, 10, 361, 80))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: #9E9E9E;")
        self.lbl_title.setObjectName("lbl_title")
        self.btn_back = QtWidgets.QPushButton(AddNotice)
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
        self.btn_addNotice = QtWidgets.QPushButton(AddNotice)
        self.btn_addNotice.setGeometry(QtCore.QRect(590, 525, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setUnderline(False)
        self.btn_addNotice.setFont(font)
        self.btn_addNotice.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_addNotice.setStyleSheet("QPushButton{\n"
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
        self.btn_addNotice.setObjectName("btn_addNotice")

        self.retranslateUi(AddNotice)
        QtCore.QMetaObject.connectSlotsByName(AddNotice)

    def retranslateUi(self, AddNotice):
        _translate = QtCore.QCoreApplication.translate
        AddNotice.setWindowTitle(_translate("AddNotice", "Term Spors Complex"))
        self.lbl_date.setText(_translate("AddNotice", "Date:"))
        self.lbl_notice.setText(_translate("AddNotice", "Notice:"))
        self.txt_date.setDisplayFormat(_translate("AddNotice", "d/M/yyyy"))
        self.lbl_title.setText(_translate("AddNotice", "Add a Notice"))
        self.btn_back.setText(_translate("AddNotice", "Back"))
        self.btn_addNotice.setText(_translate("AddNotice", "Add Notice"))
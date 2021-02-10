# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/AddLessonPageUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddLesson(object):
    def setupUi(self, AddLesson):
        AddLesson.setObjectName("AddLesson")
        AddLesson.resize(800, 600)
        AddLesson.setMinimumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        AddLesson.setFont(font)
        self.btn_back = QtWidgets.QPushButton(AddLesson)
        self.btn_back.setGeometry(QtCore.QRect(400, 520, 160, 55))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        font.setUnderline(True)
        self.btn_back.setFont(font)
        self.btn_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_back.setStyleSheet("border: 1px solid black;\n"
"color: rgb(85, 170, 255);")
        self.btn_back.setObjectName("btn_back")
        self.btn_addLesson = QtWidgets.QPushButton(AddLesson)
        self.btn_addLesson.setGeometry(QtCore.QRect(580, 520, 191, 55))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        font.setUnderline(True)
        self.btn_addLesson.setFont(font)
        self.btn_addLesson.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_addLesson.setStyleSheet("border: 1px solid black;\n"
"color: rgb(85, 170, 255);")
        self.btn_addLesson.setObjectName("btn_addLesson")
        self.horizontalLayoutWidget = QtWidgets.QWidget(AddLesson)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 120, 581, 357))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_lessonType = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_lessonType.setObjectName("lbl_lessonType")
        self.verticalLayout.addWidget(self.lbl_lessonType)
        self.lbl_teacher = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_teacher.setObjectName("lbl_teacher")
        self.verticalLayout.addWidget(self.lbl_teacher)
        self.lbl_date = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_date.setObjectName("lbl_date")
        self.verticalLayout.addWidget(self.lbl_date)
        self.lbl_time = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_time.setObjectName("lbl_time")
        self.verticalLayout.addWidget(self.lbl_time)
        self.lbl_price = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_price.setObjectName("lbl_price")
        self.verticalLayout.addWidget(self.lbl_price)
        self.lbl_description = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_description.setObjectName("lbl_description")
        self.verticalLayout.addWidget(self.lbl_description)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_lessonType = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.txt_lessonType.setObjectName("txt_lessonType")
        self.verticalLayout_2.addWidget(self.txt_lessonType)
        self.txt_teacher = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.txt_teacher.setObjectName("txt_teacher")
        self.verticalLayout_2.addWidget(self.txt_teacher)
        self.txt_date = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.txt_date.setObjectName("txt_date")
        self.verticalLayout_2.addWidget(self.txt_date)
        self.txt_time = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.txt_time.setObjectName("txt_time")
        self.verticalLayout_2.addWidget(self.txt_time)
        self.txt_price = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.txt_price.setObjectName("txt_price")
        self.verticalLayout_2.addWidget(self.txt_price)
        self.txt_description = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.txt_description.setObjectName("txt_description")
        self.verticalLayout_2.addWidget(self.txt_description)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.lbl_title = QtWidgets.QLabel(AddLesson)
        self.lbl_title.setGeometry(QtCore.QRect(240, 10, 361, 80))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: rgb(85, 170, 255);")
        self.lbl_title.setObjectName("lbl_title")

        self.retranslateUi(AddLesson)
        QtCore.QMetaObject.connectSlotsByName(AddLesson)

    def retranslateUi(self, AddLesson):
        _translate = QtCore.QCoreApplication.translate
        AddLesson.setWindowTitle(_translate("AddLesson", "Term Spors Complex"))
        self.btn_back.setText(_translate("AddLesson", "Back"))
        self.btn_addLesson.setText(_translate("AddLesson", "Add Lesson"))
        self.lbl_lessonType.setText(_translate("AddLesson", "Lesson type:"))
        self.lbl_teacher.setText(_translate("AddLesson", "Teacher:"))
        self.lbl_date.setText(_translate("AddLesson", "Date:"))
        self.lbl_time.setText(_translate("AddLesson", "Time:"))
        self.lbl_price.setText(_translate("AddLesson", "Price:"))
        self.lbl_description.setText(_translate("AddLesson", "Small description: "))
        self.lbl_title.setText(_translate("AddLesson", "Add a Lesson"))

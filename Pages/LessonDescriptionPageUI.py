# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/LessonDescriptionPageUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LessonDescription(object):
    def setupUi(self, LessonDescription):
        LessonDescription.setObjectName("LessonDescription")
        LessonDescription.resize(800, 600)
        LessonDescription.setMinimumSize(QtCore.QSize(800, 600))
        LessonDescription.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        LessonDescription.setFont(font)
        LessonDescription.setStyleSheet("background-color: rgb(254, 254, 254);")
        self.btn_back = QtWidgets.QPushButton(LessonDescription)
        self.btn_back.setGeometry(QtCore.QRect(590, 525, 180, 50))
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(LessonDescription)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 120, 531, 357))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_lessonType = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_lessonType.setFont(font)
        self.lbl_lessonType.setObjectName("lbl_lessonType")
        self.verticalLayout.addWidget(self.lbl_lessonType)
        self.lbl_teacher = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_teacher.setFont(font)
        self.lbl_teacher.setObjectName("lbl_teacher")
        self.verticalLayout.addWidget(self.lbl_teacher)
        self.lbl_date = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_date.setFont(font)
        self.lbl_date.setObjectName("lbl_date")
        self.verticalLayout.addWidget(self.lbl_date)
        self.lbl_time = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_time.setFont(font)
        self.lbl_time.setObjectName("lbl_time")
        self.verticalLayout.addWidget(self.lbl_time)
        self.lbl_price = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_price.setFont(font)
        self.lbl_price.setObjectName("lbl_price")
        self.verticalLayout.addWidget(self.lbl_price)
        self.lbl_description = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_description.setFont(font)
        self.lbl_description.setObjectName("lbl_description")
        self.verticalLayout.addWidget(self.lbl_description)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_edit_lessonType = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_edit_lessonType.sizePolicy().hasHeightForWidth())
        self.lbl_edit_lessonType.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.lbl_edit_lessonType.setFont(font)
        self.lbl_edit_lessonType.setStyleSheet("font: 75 italic 18pt \"Comic Sans MS\";")
        self.lbl_edit_lessonType.setObjectName("lbl_edit_lessonType")
        self.verticalLayout_2.addWidget(self.lbl_edit_lessonType)
        self.lbl_edit_teacher = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_edit_teacher.sizePolicy().hasHeightForWidth())
        self.lbl_edit_teacher.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.lbl_edit_teacher.setFont(font)
        self.lbl_edit_teacher.setStyleSheet("font: 75 italic 18pt \"Comic Sans MS\";")
        self.lbl_edit_teacher.setObjectName("lbl_edit_teacher")
        self.verticalLayout_2.addWidget(self.lbl_edit_teacher)
        self.lbl_edit_date = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_edit_date.sizePolicy().hasHeightForWidth())
        self.lbl_edit_date.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.lbl_edit_date.setFont(font)
        self.lbl_edit_date.setStyleSheet("font: 75 italic 18pt \"Comic Sans MS\";")
        self.lbl_edit_date.setObjectName("lbl_edit_date")
        self.verticalLayout_2.addWidget(self.lbl_edit_date)
        self.lbl_edit_time = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_edit_time.sizePolicy().hasHeightForWidth())
        self.lbl_edit_time.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.lbl_edit_time.setFont(font)
        self.lbl_edit_time.setStyleSheet("font: 75 italic 18pt \"Comic Sans MS\";")
        self.lbl_edit_time.setObjectName("lbl_edit_time")
        self.verticalLayout_2.addWidget(self.lbl_edit_time)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_edit_price = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_edit_price.sizePolicy().hasHeightForWidth())
        self.lbl_edit_price.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.lbl_edit_price.setFont(font)
        self.lbl_edit_price.setStyleSheet("font: 75 italic 18pt \"Comic Sans MS\";")
        self.lbl_edit_price.setObjectName("lbl_edit_price")
        self.horizontalLayout_2.addWidget(self.lbl_edit_price)
        self.lbl_priceAZN = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_priceAZN.setFont(font)
        self.lbl_priceAZN.setStyleSheet("color: rgb(100, 100, 200);")
        self.lbl_priceAZN.setObjectName("lbl_priceAZN")
        self.horizontalLayout_2.addWidget(self.lbl_priceAZN)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.lbl_edit_description = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_edit_description.sizePolicy().hasHeightForWidth())
        self.lbl_edit_description.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.lbl_edit_description.setFont(font)
        self.lbl_edit_description.setStyleSheet("font: 75 italic 18pt \"Comic Sans MS\";")
        self.lbl_edit_description.setObjectName("lbl_edit_description")
        self.verticalLayout_2.addWidget(self.lbl_edit_description)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.btn_signUpForLesson = QtWidgets.QPushButton(LessonDescription)
        self.btn_signUpForLesson.setGeometry(QtCore.QRect(30, 525, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setUnderline(False)
        self.btn_signUpForLesson.setFont(font)
        self.btn_signUpForLesson.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_signUpForLesson.setStyleSheet("QPushButton{\n"
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
        self.btn_signUpForLesson.setObjectName("btn_signUpForLesson")
        self.lbl_title = QtWidgets.QLabel(LessonDescription)
        self.lbl_title.setGeometry(QtCore.QRect(140, 10, 511, 80))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: #9E9E9E;")
        self.lbl_title.setObjectName("lbl_title")

        self.retranslateUi(LessonDescription)
        QtCore.QMetaObject.connectSlotsByName(LessonDescription)

    def retranslateUi(self, LessonDescription):
        _translate = QtCore.QCoreApplication.translate
        LessonDescription.setWindowTitle(_translate("LessonDescription", "Term Spors Complex"))
        self.btn_back.setText(_translate("LessonDescription", "Back"))
        self.lbl_lessonType.setText(_translate("LessonDescription", "Type:"))
        self.lbl_teacher.setText(_translate("LessonDescription", "Teacher:"))
        self.lbl_date.setText(_translate("LessonDescription", "Date:"))
        self.lbl_time.setText(_translate("LessonDescription", "Time:"))
        self.lbl_price.setText(_translate("LessonDescription", "Price:"))
        self.lbl_description.setText(_translate("LessonDescription", "Small description: "))
        self.lbl_edit_lessonType.setText(_translate("LessonDescription", "     ?"))
        self.lbl_edit_teacher.setText(_translate("LessonDescription", "     ?"))
        self.lbl_edit_date.setText(_translate("LessonDescription", "     ?"))
        self.lbl_edit_time.setText(_translate("LessonDescription", "     ?"))
        self.lbl_edit_price.setText(_translate("LessonDescription", "     ?"))
        self.lbl_priceAZN.setText(_translate("LessonDescription", "AZN"))
        self.lbl_edit_description.setText(_translate("LessonDescription", "     ?"))
        self.btn_signUpForLesson.setText(_translate("LessonDescription", "Sign-Up for lesson"))
        self.lbl_title.setText(_translate("LessonDescription", "Lesson Description"))

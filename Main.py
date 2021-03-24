import sys


# PyQt5 modules
from PyQt5 import QtGui
from PyQt5.QtCore import QDate, QRegExp, QTime, Qt
from PyQt5.QtWidgets import QApplication, QHeaderView, QLineEdit, QStyle, QMainWindow, QMessageBox, QPushButton, QTableWidgetItem, QWidget


# My Classes
from Classes import *
from Helper.Convertor import *
from Helper.ToastNotifier import QToaster


# User Interfaces
from Pages.MainPageUI import Ui_Main
from Pages.RegistrationPageUI import Ui_Registration
from Pages.LoginPageUI import Ui_Login
from Pages.MemberMainPageUI import Ui_MemberMain
from Pages.ImportantNoticesPageUI import Ui_ImportantNotices
from Pages.PersonalReportPageUI import Ui_PersonalReport
from Pages.LessonDescriptionPageUI import Ui_LessonDescription
from Pages.AdminMainPageUI import Ui_AdminMain
from Pages.AddLessonPageUI import Ui_AddLesson
from Pages.AddNoticePageUI import Ui_AddNotice






#############################################################
##### Tables (Database Simulator)
lessonObjects = Convertor.readObjectsFromDatabase(Lesson, 'Tables/LessonTable.json')
noticeObjects = Convertor.readObjectsFromDatabase(Notice, 'Tables/NoticeTable.json')
userObjects = Convertor.readObjectsFromDatabase(User, 'Tables/UserTable.json')
currentUserIndex = None






##### Combobox (Filter)
comboboxDefaultText = 'None'
comboBoxTypeCurrentText = 'None'
comboBoxTeacherCurrentText = 'None'
comboBoxPriceCurrentText = 'None'






##### Pages
addNoticePage = None
addLessonPage = None
adminMainPage = None
lessonDescriptionPage = None
personalReportPage = None
importantNoticesPage = None
memberMainPage = None
registrationPage = None
loginPage = None
mainPage = None






#############################################################
##### Functions
def showLessons(self, lessons):
    
    self.ui.tableWidget.setRowCount(len(lessons))

    rowIndex = 0
    for lesson in lessons:
        item1 = QTableWidgetItem(lesson.type)
        item2 = QTableWidgetItem(f'{lesson.date} - {lesson.time}')
        item3 = QTableWidgetItem()


        # for delete lesson, or find lesson
        item1.setData(1, lesson)
        item2.setData(1, lesson)
        item3.setData(1, lesson)


        self.ui.tableWidget.setItem(rowIndex, 0, item1)
        self.ui.tableWidget.setItem(rowIndex, 1, item2)
        self.ui.tableWidget.setItem(rowIndex, 2, item3)


        button = QPushButton("More details", self.ui.tableWidget)
        button.setStyleSheet('color: rgb(85, 170, 255); font: 14pt "Palatino Linotype"; text-decoration: underline; background-color: rgba(255, 255, 255, 0);')
        button.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        button.setProperty('id', lesson.id)

        button.clicked.connect(self.clickedMoreDetail)
        self.ui.tableWidget.setCellWidget(rowIndex, 2, button)


        item1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item3.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        item1.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        item2.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        item3.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

        rowIndex+=1


def selectedIndexChanged(self):
    global comboBoxTypeCurrentText
    global comboBoxTeacherCurrentText
    global comboBoxPriceCurrentText


   
    comboBoxTypeCurrentText = self.ui.comboBox_Type.currentText()
    comboBoxTeacherCurrentText = self.ui.comboBox_Teacher.currentText()
    comboBoxPriceCurrentText = self.ui.comboBox_Price.currentText()


    selectedLessons = []
    if comboBoxTypeCurrentText == comboboxDefaultText and comboBoxTeacherCurrentText == comboboxDefaultText and comboBoxPriceCurrentText == comboboxDefaultText:
        showLessons(self, lessonObjects)
    else:
        for lesson in lessonObjects:
            if  comboBoxTypeCurrentText != comboboxDefaultText and lesson.type == comboBoxTypeCurrentText:
                if lesson not in selectedLessons:
                    selectedLessons.append(lesson)
            if  comboBoxTeacherCurrentText != comboboxDefaultText and lesson.teacher == comboBoxTeacherCurrentText:
                if lesson not in selectedLessons:
                    selectedLessons.append(lesson)
            if  comboBoxPriceCurrentText != comboboxDefaultText and lesson.price == comboBoxPriceCurrentText:
                if lesson not in selectedLessons:
                    selectedLessons.append(lesson)
        showLessons(self, selectedLessons)


def addItemInComboBox(self, changeCobmoboxType = False, changeCobmoboxTeacher = False, changeCobmoboxPrice = False):
    uniqueTypeList = []
    uniqueTeacherList = []
    uniquePriceList = []
    

    if changeCobmoboxType == False and changeCobmoboxTeacher == False and changeCobmoboxPrice == False:
        selectedIndexChanged(self)
    else:
        for lesson in lessonObjects:
            if changeCobmoboxType == True:
                if lesson.type not in uniqueTypeList:
                    uniqueTypeList.append(lesson.type)
                    

            if changeCobmoboxTeacher == True:
                if lesson.teacher not in uniqueTeacherList:
                    uniqueTeacherList.append(lesson.teacher)

            if changeCobmoboxPrice == True:
                if lesson.price not in uniquePriceList:
                    uniquePriceList.append(lesson.price)


    


    if changeCobmoboxType == True:
        global comboBoxTypeCurrentText
        comboBoxTypeCurrentText = comboboxDefaultText

        self.ui.comboBox_Type.clear()
        self.ui.comboBox_Type.addItem(comboboxDefaultText)
        uniqueTypeList.sort()
        self.ui.comboBox_Type.addItems(uniqueTypeList)

        self.ui.comboBox_Type.setCurrentText(comboboxDefaultText)

    
    if changeCobmoboxTeacher == True:
        global comboBoxTeacherCurrentText
        comboBoxTeacherCurrentText = comboboxDefaultText

        self.ui.comboBox_Teacher.clear()
        self.ui.comboBox_Teacher.addItem(comboboxDefaultText)
        uniqueTeacherList.sort()
        self.ui.comboBox_Teacher.addItems(uniqueTeacherList)

        self.ui.comboBox_Teacher.setCurrentText(comboboxDefaultText)


    if changeCobmoboxPrice == True:
        global comboBoxPriceCurrentText
        comboBoxPriceCurrentText = comboboxDefaultText

        self.ui.comboBox_Price.clear()
        self.ui.comboBox_Price.addItem(comboboxDefaultText)
        uniquePriceList.sort()
        self.ui.comboBox_Price.addItems(uniquePriceList)
        
        self.ui.comboBox_Price.setCurrentText(comboboxDefaultText)






#############################################################
##### Widgets


### Add Notice Page ###
class AddNoticePage(QWidget):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_AddNotice()
        self.ui.setupUi(self)

        self.ui.btn_back.clicked.connect(self.clickedBack)
        self.ui.btn_addNotice.clicked.connect(self.clickedAddNotice)

    def clickedBack(self):
        adminMainPage.setGeometry(self.geometry())
        adminMainPage.show()
        self.close()

    def clickedAddNotice(self):
        dateInput = self.ui.txt_date.text()
        noticeInput = self.ui.txt_notice.text()
        
        if dateInput and noticeInput:
            notice = Notice(dateInput, noticeInput)
            noticeObjects.append(notice)
            Convertor.writeObjectsToDatabese(noticeObjects, 'Tables/NoticeTable.json')
            

            #addItemInComboBox(adminMainPage, True, True, True)
            adminMainPage.setGeometry(self.geometry())
            adminMainPage.show()
            self.close()
            message = f'{noticeInput} was successfully added'
            parent = adminMainPage
        else:
            message = 'Notice cannot be empty'
            parent = self

        QToaster.showMessage(parent, message, 
                QStyle.SP_MessageBoxCritical, corner=Qt.Corner(1),
                desktop=False, timeout=2000, closable=False)



### Add Lesson Page ###
class AddLessonPage(QWidget):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_AddLesson()
        self.ui.setupUi(self)


        regVal = QtGui.QRegExpValidator(QRegExp('[1-9][0-9]*\.?[0-9][0-9]'))
        self.ui.txt_price.setValidator(regVal)


        self.ui.btn_back.clicked.connect(self.clickedBack)
        self.ui.btn_addLesson.clicked.connect(self.clickedAddLesson)

    def clickedBack(self):
        adminMainPage.setGeometry(self.geometry())
        adminMainPage.show()
        self.close()

    def clickedAddLesson(self):
        lessonType = self.ui.txt_lessonType.text()
        date = self.ui.txt_date.text()
        time = self.ui.txt_time.text()
        teacher = self.ui.txt_teacher.text()
        price = self.ui.txt_price.text()
        description = self.ui.txt_description.text()

        
        if lessonType and date and time and teacher and price and description:

            id = None
            if lessonObjects:
                id = lessonObjects[-1].id + 1
            else:
                id = 1

            lesson = Lesson(id, lessonType,date,time,teacher,price,description)
            lessonObjects.append(lesson)
            Convertor.writeObjectsToDatabese(lessonObjects, 'Tables/LessonTable.json')
            
            addItemInComboBox(adminMainPage, True, True, True)
            adminMainPage.setGeometry(self.geometry())
            adminMainPage.show()
            self.close()

            message = f'{description} was successfully added'
            parent = adminMainPage
        else:
            message = 'Empty input'
            parent = self

        QToaster.showMessage(parent, message, 
                QStyle.SP_MessageBoxCritical, corner=Qt.Corner(1),
                desktop=False, timeout=2000, closable=False)



### Admin Main Page ###
class AdminMainPage(QWidget):
    def __init__(self, hasComboboxItem = True, configureTable = True):
        super().__init__()
        
        self.ui = Ui_AdminMain()
        self.ui.setupUi(self)


        if not hasComboboxItem:
            addItemInComboBox(self, True, True, True)

        if not configureTable:
            self.configureTable()

        showLessons(self, lessonObjects)
       


        self.ui.btn_addLesson.clicked.connect(self.clickedAddLesson)
        self.ui.btn_addNotice.clicked.connect(self.clickedAddNotice)
        self.ui.btn_deleteLesson.clicked.connect(self.clickedDeleteLesson)
        self.ui.comboBox_Type.currentIndexChanged.connect(self.selectedIndexChanged)
        self.ui.comboBox_Teacher.currentIndexChanged.connect(self.selectedIndexChanged)
        self.ui.comboBox_Price.currentIndexChanged.connect(self.selectedIndexChanged)


    def configureTable(self):
        columnCount = 3
        self.ui.tableWidget.setColumnCount(columnCount)


        self.ui.tableWidget.setHorizontalHeaderLabels(['Name', 'DateTime', 'Details'])
        self.ui.tableWidget.horizontalHeader().setStyleSheet('font: 75 18pt "Comic Sans MS";')

        width = int(self.ui.tableWidget.width() / columnCount / 1.001)

        for col in range(columnCount):
            self.ui.tableWidget.setColumnWidth(col, width)

    def selectedIndexChanged(self, text):
        selectedIndexChanged(self)

    def clickedAddLesson(self):
        global addLessonPage

        if not addLessonPage:
            addLessonPage = AddLessonPage()
        addLessonPage.setGeometry(self.geometry())
        addLessonPage.show()
        self.close()

    def clickedAddNotice(self):
        global addNoticePage

        if not addNoticePage:
            addNoticePage = AddNoticePage()


        addNoticePage.setGeometry(self.geometry())
        addNoticePage.show()
        self.close()

    def clickedDeleteLesson(self):
        message = ''
        
        if self.ui.tableWidget.selectedItems():

            for item in self.ui.tableWidget.selectedItems():
                message += f'{item.text()}\n'
                lessonObjects.remove(item.data(1))
                
            
            changeCobmoboxType = True
            changeCobmoboxTeacher = True
            changeCobmoboxPrice = True


            for lesson in lessonObjects:
                if comboBoxTypeCurrentText == lesson.type:
                    changeCobmoboxType = False
                
                if comboBoxTeacherCurrentText == lesson.teacher:
                    changeCobmoboxTeacher = False
                    
                if comboBoxPriceCurrentText == lesson.price:
                    changeCobmoboxPrice = False

                if not changeCobmoboxType and not changeCobmoboxTeacher and not changeCobmoboxPrice:
                    break


            message += 'deleted'

            addItemInComboBox(self, changeCobmoboxType, changeCobmoboxTeacher, changeCobmoboxPrice)
            
            Convertor.writeObjectsToDatabese(lessonObjects, 'Tables/LessonTable.json')

        else:
            message = 'Please select a lesson to delete'

        QToaster.showMessage(self, message, 
                    QStyle.SP_MessageBoxCritical, corner=Qt.Corner(1),
                    desktop=False, timeout=2000, closable=False)

    def clickedMoreDetail(self):
        global lessonDescriptionPage

        if not lessonDescriptionPage:
            lessonDescriptionPage = LessonDescriptionPage()
        
        lessonDescriptionPage.setGeometry(self.geometry())
        lessonDescriptionPage.show()
        lessonDescriptionPage.showLessonDescription('Admin', self.sender().property("id"))
        self.close()



### Lesson Description Page ###
class LessonDescriptionPage(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_LessonDescription()
        self.ui.setupUi(self)

        regVal = QtGui.QRegExpValidator(QRegExp('[1-9][0-9]*\.?[0-9][0-9]'))
        self.ui.lbl_edit_price.setValidator(regVal)

        self.ui.btn_back.clicked.connect(self.clickedBack)
        self.ui.btn_edit.clicked.connect(self.clickedEdit)
        self.ui.btn_signUpForLesson.clicked.connect(self.clickedSignUpForLesson)


    def clickedBack(self):
        if self.role == 'Admin':
            adminMainPage.setGeometry(self.geometry())
            adminMainPage.show()
            self.close()
        elif self.role == 'Member':
            memberMainPage.setGeometry(self.geometry())
            memberMainPage.show()
            self.close()

        self.ui.btn_edit.setText('Edit')

    def clickedEdit(self):
        senderText = self.sender().text()

        if senderText == 'Edit':
            self.sender().setText('Update')
        elif senderText == 'Update':
            lessonType = self.ui.lbl_edit_lessonType.text()
            date = self.ui.lbl_edit_date.text()
            time = self.ui.lbl_edit_time.text()
            teacher = self.ui.lbl_edit_teacher.text()
            price = self.ui.lbl_edit_price.text()
            description = self.ui.lbl_edit_description.toPlainText()

            
            if lessonType and date and time and teacher and price and description:
                
                self.lesson.type = lessonType
                self.lesson.date = date
                self.lesson.time = time
                self.lesson.teacher = teacher
                self.lesson.price = price
                self.lesson.smallDescription = description

                Convertor.writeObjectsToDatabese(lessonObjects, 'Tables/LessonTable.json')
                
                addItemInComboBox(adminMainPage, True, True, True)
                adminMainPage.setGeometry(self.geometry())
                adminMainPage.show()
                self.close()

                message = f'{description} was successfully updated'
                parent = adminMainPage
            else:
                message = 'Empty input'
                parent = self

            QToaster.showMessage(parent, message, 
                    QStyle.SP_MessageBoxCritical, corner=Qt.Corner(1),
                    desktop=False, timeout=2000, closable=False)
        




        self.ui.lbl_edit_lessonType.setClearButtonEnabled(True)
        self.ui.lbl_edit_teacher.setClearButtonEnabled(True)
        self.ui.lbl_edit_price.setClearButtonEnabled(True)

        self.ui.lbl_edit_lessonType.setReadOnly(False)
        self.ui.lbl_edit_date.setReadOnly(False)
        self.ui.lbl_edit_time.setReadOnly(False)
        self.ui.lbl_edit_teacher.setReadOnly(False)
        self.ui.lbl_edit_price.setReadOnly(False)
        self.ui.lbl_edit_description.setReadOnly(False)


    def clickedSignUpForLesson(self):
        result = QMessageBox.question(self,'Term Sport Complex','Are you sure ?', QMessageBox.Yes | QMessageBox.No)

        if(result == QMessageBox.Yes):
            userObjects[currentUserIndex].personalReport.lastClassAttended = self.lesson.type
            userObjects[currentUserIndex].personalReport.TotNumOfClsAttThisMonth += 1
            userObjects[currentUserIndex].personalReport.totalMonthlyFee += float(self.lesson.price)

            Convertor.writeObjectsToDatabese(userObjects, 'Tables/UserTable.json')

            memberMainPage.setGeometry(self.geometry())
            memberMainPage.show()
            self.close()
            message = 'You have successfully registered for the lesson'
            parent = memberMainPage

            
      
        elif(result == QMessageBox.No):
            message = 'Canceled'
            parent = self

        QToaster.showMessage(parent, message, 
            QStyle.SP_MessageBoxCritical, corner=Qt.Corner(1),
            desktop=False, timeout=2000, closable=False)
            
    def showLessonDescription(self, role, lessonId):
        self.role = role
        self.lesson = [l for l in lessonObjects if l.id == lessonId][0]

        if self.role == 'Admin':
            self.ui.btn_signUpForLesson.setVisible(False)
            self.ui.btn_edit.setVisible(True)
        else:
            self.ui.btn_signUpForLesson.setVisible(True)
            self.ui.btn_edit.setVisible(False)



        self.ui.lbl_edit_lessonType.setClearButtonEnabled(False)
        self.ui.lbl_edit_teacher.setClearButtonEnabled(False)
        self.ui.lbl_edit_price.setClearButtonEnabled(False)

        self.ui.lbl_edit_lessonType.setReadOnly(True)
        self.ui.lbl_edit_date.setReadOnly(True)
        self.ui.lbl_edit_time.setReadOnly(True)
        self.ui.lbl_edit_teacher.setReadOnly(True)
        self.ui.lbl_edit_price.setReadOnly(True)
        self.ui.lbl_edit_description.setReadOnly(True)
            


        date = self.lesson.date.split('/')

        self.ui.lbl_edit_date.setDate(QDate(int(date[2]), int(date[1]), int(date[0])))

        time = QTime().fromString(self.lesson.time, 'h:mm AP')
        self.ui.lbl_edit_time.setTime(time)

        self.ui.lbl_edit_lessonType.setText(self.lesson.type)
        self.ui.lbl_edit_teacher.setText(self.lesson.teacher)
        self.ui.lbl_edit_price.setText(self.lesson.price)
        self.ui.lbl_edit_description.setText(self.lesson.smallDescription)



### Personal Report Page ###
class PersonalReportPage(QWidget):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_PersonalReport()
        self.ui.setupUi(self)


        regVal = QtGui.QRegExpValidator(QRegExp('[1-9][0-9]*\.?[0-9][0-9]'))
        self.ui.txt_inputHeight.setValidator(regVal)
        self.ui.txt_inputWeight.setValidator(regVal)
        self.ui.txt_targetBMI.setValidator(regVal)

        self.currentUser = userObjects[currentUserIndex]

        self.showReports(True)

        self.ui.btn_back.clicked.connect(self.clickedBack)
        self.ui.btn_save.clicked.connect(self.clickedSave)

        self.ui.txt_inputHeight.textChanged[str].connect(self.inputTextChanged)
        self.ui.txt_inputWeight.textChanged[str].connect(self.inputTextChanged)
        self.ui.txt_targetBMI.textChanged[str].connect(self.inputTextChanged)


    def clickedBack(self):
        memberMainPage.setGeometry(self.geometry())
        memberMainPage.show()
        self.showReports(True)
        self.close()  

    def showReports(self, firstTime = False):

        if firstTime:
            self.ui.btn_save.setEnabled(False)
            self.ui.btn_save.setStyleSheet('''
                QPushButton {
                    border: 2px solid #9E9E9E;
                    border-radius: 15px;
                    background-color: #5a5a5a;
                    color: gray; 
                    }
                    
                QPushButton:hover{ 
                    color: #9E9E9E;
                    background-color: #5a5a5a;
                    }
                    
                QPushButton:pressed{
                    color: #9c2219;
                    }
                
                QPushButton:checked{color: #2c998e;}
            ''')
            
            self.ui.lbl_textLastClassAtt.setText(self.currentUser.personalReport.lastClassAttended)
            self.ui.lbl_textTotNumOfClsAttThisMonth.setText(str(self.currentUser.personalReport.TotNumOfClsAttThisMonth))
            self.ui.lbl_textTotalMonthlyFee.setText(str(round(self.currentUser.personalReport.totalMonthlyFee, 2)))

            height = self.currentUser.personalReport.inputHeight
            weight = self.currentUser.personalReport.inputWeight

            self.ui.txt_inputHeight.setText(str(height))
            self.ui.txt_inputWeight.setText(str(weight))
        else:
            if(self.ui.txt_inputHeight.text() != ''):
                height = float(self.ui.txt_inputHeight.text())
            else:
                height = 0

            if(self.ui.txt_inputWeight.text() != ''):
                weight = float(self.ui.txt_inputWeight.text())
            else:
                weight = 0



        
        if(height == 0):
            self.ui.txt_inputHeight.setText('')

        if(weight == 0):
            self.ui.txt_inputWeight.setText('')



        if(self.currentUser.personalReport.targetBMI == 0 and firstTime == True):
            self.ui.txt_targetBMI.setText('')
        elif(firstTime == False):
            pass
        else:
            self.ui.txt_targetBMI.setText(str(self.currentUser.personalReport.targetBMI))


        if(self.currentUser.personalReport.BMI == 0 and firstTime == True):
            self.ui.txt_BMI.setText('0')
        else:
            if height != 0:
                self.ui.txt_BMI.setText(str(round((weight / (height * height)), 2)))
            else:
                self.ui.txt_BMI.setText('0')

    def inputTextChanged(self, text):
        if(text != '0'):

            self.ui.btn_save.setEnabled(True)
            self.ui.btn_save.setStyleSheet('''
                QPushButton {
                    border: 2px solid #9E9E9E;
                    border-radius: 15px;
                    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);
                    color: #FFFFFF; 
                    }
                    
                QPushButton:hover{ 
                    color: #9E9E9E;
                    background-color: #5a5a5a;
                    }
                    
                QPushButton:pressed{
                    color: #9c2219;
                    }
                
                QPushButton:checked{color: #2c998e;}
            ''')

            self.showReports()

    def clickedSave(self):
        if(self.ui.txt_targetBMI.text() != ''):
            userObjects[currentUserIndex].personalReport.targetBMI = float(self.ui.txt_targetBMI.text())
        else:
            userObjects[currentUserIndex].personalReport.targetBMI = 0

        if(self.ui.txt_inputHeight.text() != ''):
            userObjects[currentUserIndex].personalReport.inputHeight = float(self.ui.txt_inputHeight.text())
        else:
            userObjects[currentUserIndex].personalReport.inputHeight = 0

        if(self.ui.txt_inputWeight.text() != ''):
            userObjects[currentUserIndex].personalReport.inputWeight = float(self.ui.txt_inputWeight.text())
        else:
            userObjects[currentUserIndex].personalReport.inputWeight = 0

        if(self.ui.txt_BMI.text() != ''):
            userObjects[currentUserIndex].personalReport.BMI = float(self.ui.txt_BMI.text())
        else:
            userObjects[currentUserIndex].personalReport.BMI = 0


        Convertor.writeObjectsToDatabese(userObjects, 'Tables/UserTable.json')

        self.showReports(True)

        QToaster.showMessage(self, 'Successfully saved', 
                            QStyle.SP_MessageBoxCritical, corner=Qt.Corner(1),
                            desktop=False, timeout=2000, closable=False)




### Important Notices Page ###
class ImportantNoticesPage(QWidget):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_ImportantNotices()
        self.ui.setupUi(self)

        self.ui.btn_back.clicked.connect(self.clickedBack)

        self.showNotices()


    def clickedBack(self):
        memberMainPage.setGeometry(self.geometry())
        memberMainPage.show()
        self.close()


    def showNotices(self):
        columnCount = 2
        self.ui.tableWidget.setColumnCount(columnCount)
        self.ui.tableWidget.setRowCount(len(noticeObjects))
        self.ui.tableWidget.setHorizontalHeaderLabels(('Date', 'Notice'))
        self.ui.tableWidget.horizontalHeader().setStyleSheet('font: 75 18pt "Comic Sans MS";')


        width = int(self.ui.tableWidget.width() / columnCount / 1.002)

        for col in range(columnCount):
            self.ui.tableWidget.setColumnWidth(col, width)

        
        rowIndex = 0
        for notice in noticeObjects:
            item1 = QTableWidgetItem(notice.date)
            item2 = QTableWidgetItem(notice.notice)

            self.ui.tableWidget.setItem(rowIndex, 0, item1)
            self.ui.tableWidget.setItem(rowIndex, 1, item2)

            item1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            
            item1.setFlags(Qt.ItemIsEnabled)
            item2.setFlags(Qt.ItemIsEnabled)

            rowIndex+=1



### Member Main Page ###
class MemberMainPage(QWidget):
    def __init__(self, hasComboboxItem = False, configureTable = False):
        super().__init__()
        
        self.ui = Ui_MemberMain()
        self.ui.setupUi(self)


        if not hasComboboxItem:
            addItemInComboBox(self, True, True, True)

        if not configureTable:
            self.configureTable()

        showLessons(self, lessonObjects)
       

        self.ui.btn_notices.clicked.connect(self.clickedNotices)
        self.ui.btn_viewReport.clicked.connect(self.clickedViewReport)
        self.ui.comboBox_Type.currentIndexChanged.connect(self.selectedIndexChanged)
        self.ui.comboBox_Teacher.currentIndexChanged.connect(self.selectedIndexChanged)
        self.ui.comboBox_Price.currentIndexChanged.connect(self.selectedIndexChanged)

    def configureTable(self):
        columnCount = 3
        self.ui.tableWidget.setColumnCount(columnCount)


        self.ui.tableWidget.setHorizontalHeaderLabels(['Name', 'DateTime', 'Details'])
        self.ui.tableWidget.horizontalHeader().setStyleSheet('font: 75 18pt "Comic Sans MS";')

        width = int(self.ui.tableWidget.width() / columnCount / 1.001)

        for col in range(columnCount):
            self.ui.tableWidget.setColumnWidth(col, width)

    def selectedIndexChanged(self, text):
        selectedIndexChanged(self)

    def clickedNotices(self):
        global importantNoticesPage

        if not importantNoticesPage:
            importantNoticesPage = ImportantNoticesPage()
        importantNoticesPage.setGeometry(self.geometry())
        importantNoticesPage.show()
        self.close()

    def clickedViewReport(self):
        global personalReportPage

        if not personalReportPage:
            personalReportPage = PersonalReportPage()
        else:
            personalReportPage.showReports(True)

        personalReportPage.setGeometry(self.geometry())
        personalReportPage.show()
        self.close()

    def clickedMoreDetail(self):
        global lessonDescriptionPage

        if not lessonDescriptionPage:
            lessonDescriptionPage = LessonDescriptionPage()
        
        lessonDescriptionPage.setGeometry(self.geometry())
        lessonDescriptionPage.show()
        lessonDescriptionPage.showLessonDescription('Member', self.sender().property("id"))
        self.close()



### Registration Page ###
class RegistrationPage(QWidget):
    def __init__(self, role):
        super().__init__()
        
        self.role = role

        self.ui = Ui_Registration()
        self.ui.setupUi(self)

        self.ui.btn_back.clicked.connect(self.clickedBack)
        self.ui.btn_submit.clicked.connect(self.clickedSubmit)

    def clickedBack(self):
        loginPage.ui.txt_username.clear()
        loginPage.ui.txt_password.clear()

        loginPage.changeRole(self.role)
        loginPage.setGeometry(self.geometry())
        loginPage.show()
        self.close()

    
    def clickedSubmit(self):

        name = self.ui.txt_name.text()
        surname = self.ui.txt_surname.text()
        birthDate = self.ui.txt_birthDate.text()
        code = self.ui.txt_code.text()
        username = self.ui.txt_username.text()
        password = self.ui.txt_password.text()
        confirmPass = self.ui.txt_confirmPass.text()

        if name and surname and birthDate and code and username and password and confirmPass:
            if password == confirmPass:
                for userObject in userObjects:
                    if userObject.username == username:
                        QToaster.showMessage(self, 'Already exists', 
                            QStyle.SP_MessageBoxCritical, corner=Qt.Corner(1),
                            desktop=False, timeout=2000, closable=False)
                        return

                user = User(name,surname,birthDate,code,username,password,self.role, PersonalReport('Empty', 0,0,0,0,0,0))
                userObjects.append(user)
                Convertor.writeObjectsToDatabese(userObjects, 'Tables/UserTable.json')

                
                loginPage.ui.txt_username.clear()
                loginPage.ui.txt_password.clear()
                loginPage.changeRole(self.role)
                loginPage.setGeometry(self.geometry())
                loginPage.show()
                self.close()

                QToaster.showMessage(loginPage, 'Successfully', 
                    QStyle.SP_MessageBoxCritical, corner=Qt.Corner(1),
                    desktop=False, timeout=2000, closable=False)

            else:
                QToaster.showMessage(self, 'Wrong: Confirm Password', 
                    QStyle.SP_MessageBoxCritical, corner=Qt.Corner(1),
                    desktop=False, timeout=2000, closable=False)
        else:
            QToaster.showMessage(self, 'Empty input', 
                    QStyle.SP_MessageBoxCritical, corner=Qt.Corner(1),
                    desktop=False, timeout=2000, closable=False)



### Login Page ###
class LoginPage(QWidget):
    def __init__(self, role):
        super().__init__()
        
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        
        self.role = role
        self.changeRole(self.role)

        self.ui.btn_back.clicked.connect(self.clickedBack)
        self.ui.btn_register.clicked.connect(self.clickedRegistration)
        self.ui.btn_sigIn.clicked.connect(self.clickedSigIn)
    
    def changeRole(self, role):
        self.role = role
        self.ui.lbl_title.setText(f"{self.role} Login")

    def clickedBack(self):
        mainPage.setGeometry(self.geometry())
        mainPage.show()
        self.close()

    def clickedRegistration(self):
        global registrationPage

        if not registrationPage:
            registrationPage = RegistrationPage(self.role)


        registrationPage.ui.txt_birthDate.setDate(QDate(2000,1,1))
        for lineEdit in registrationPage.findChildren(QLineEdit):
            lineEdit.clear()

        registrationPage.setGeometry(self.geometry())
        registrationPage.show()
        self.close()

    def clickedSigIn(self):
        global currentUserIndex
        global memberMainPage
        global adminMainPage

        currentUserIndex = 0
        for user in userObjects:
            if self.role == 'Member':
                if user.role == 'Member' and self.ui.txt_username.text() == user.username and self.ui.txt_password.text() == user.password:
                    if not memberMainPage:
                        memberMainPage = MemberMainPage()
                    memberMainPage.setGeometry(self.geometry())
                    memberMainPage.show()
                    self.close()
                    break
            elif self.role == 'Admin':
                if user.role == 'Admin' and self.ui.txt_username.text() == user.username and self.ui.txt_password.text() == user.password:
                    if not memberMainPage:
                        adminMainPage = AdminMainPage(False, False)
                    adminMainPage.setGeometry(self.geometry())
                    adminMainPage.show()
                    self.close()
                    break
            currentUserIndex += 1
            
        else:
            QToaster.showMessage(self, 'The email or password is incorrect', 
                    QStyle.SP_MessageBoxCritical, corner=Qt.Corner(1),
                    desktop=False, timeout=2000, closable=False)



### Main Page (App) ###
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        self.ui.btn_member.clicked.connect(self.clickedLogin)
        self.ui.btn_admin.clicked.connect(self.clickedLogin)


    def clickedLogin(self):
        global loginPage
        sender = self.sender().text()

        if not loginPage:
            loginPage = LoginPage(sender)


        loginPage.ui.txt_username.clear()
        loginPage.ui.txt_password.clear()
            
        loginPage.changeRole(sender)
        loginPage.setGeometry(self.geometry())
        loginPage.show()
        self.close()



def window():
    global mainPage

    app = QApplication(sys.argv)

    if not mainPage:
        mainPage = MyApp()
    mainPage.show()
    sys.exit(app.exec_())


window()
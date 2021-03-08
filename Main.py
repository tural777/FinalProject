import sys

# PyQt5 modules
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QHeaderView, QStyle, QMainWindow, QMessageBox, QPushButton, QTableWidgetItem, QWidget

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



lessonObjects = Convertor.readObjectsFromDatabase(Lesson, 'Tables/LessonTable.json')
noticeObjects = Convertor.readObjectsFromDatabase(Notice, 'Tables/NoticeTable.json')
userObjects = Convertor.readObjectsFromDatabase(User, 'Tables/UserTable.json')
currentUserIndex = None


### Add Notice Page ###
class AddNoticePage(QWidget):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_AddNotice()
        self.ui.setupUi(self)

        self.ui.btn_back.clicked.connect(self.clickedBack)
        self.ui.btn_addNotice.clicked.connect(self.clickedAddNotice)

    def clickedBack(self):
        self.adminMainPage = AdminMainPage()
        self.adminMainPage.show()
        self.close()

    def clickedAddNotice(self):
        dateInput = self.ui.txt_date.text()
        noticeInput = self.ui.txt_notice.text()
        
        if dateInput and noticeInput:
            notice = Notice(dateInput, noticeInput)
            noticeObjects.append(notice)
            Convertor.writeObjectsToDatabese(noticeObjects, 'Tables/NoticeTable.json')
            self.adminMainPage = AdminMainPage()
            self.adminMainPage.show()
            self.close()
            message = f'{noticeInput} was successfully added'
            parent = self.adminMainPage
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

        self.ui.btn_back.clicked.connect(self.clickedBack)
        self.ui.btn_addLesson.clicked.connect(self.clickedAddLesson)


    def clickedBack(self):
        self.adminMainPage = AdminMainPage()
        self.adminMainPage.show()
        self.close()


    def clickedAddLesson(self):
        lessonType = self.ui.txt_lessonType.text()
        date = self.ui.txt_date.text()
        time = self.ui.txt_time.text()
        teacher = self.ui.txt_teacher.text()
        price = self.ui.txt_price.text()
        description = self.ui.txt_description.text()
        
        if lessonType and date and time and teacher and price and description:
            lesson = Lesson(lessonType,date,time,teacher,price,description)
            lessonObjects.append(lesson)
            Convertor.writeObjectsToDatabese(lessonObjects, 'Tables/LessonTable.json')
            self.adminMainPage = AdminMainPage()
            self.adminMainPage.show()
            self.close()
            message = f'{description} was successfully added'
            parent = self.adminMainPage
        else:
            message = 'Empty input'
            parent = self

        QToaster.showMessage(parent, message, 
                QStyle.SP_MessageBoxCritical, corner=Qt.Corner(1),
                desktop=False, timeout=2000, closable=False)



### Admin Main Page ###
class AdminMainPage(QWidget):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_AdminMain()
        self.ui.setupUi(self)

        self.showLessons()

        self.ui.btn_addLesson.clicked.connect(self.clickedAddLesson)
        self.ui.btn_addNotice.clicked.connect(self.clickedAddNotice)
        self.ui.btn_deleteLesson.clicked.connect(self.clickedDeleteLesson)


    def clickedAddLesson(self):
        self.addLessonPage = AddLessonPage()
        self.addLessonPage.show()
        self.close()


    def clickedAddNotice(self):
        self.addNoticePage = AddNoticePage()
        self.addNoticePage.show()
        self.close()


    def clickedDeleteLesson(self):
        message = ''
        
        if self.ui.tableWidget.selectedItems():
            indexesSort = []
            for item in self.ui.tableWidget.selectedItems():
                indexesSort.append(item.row())
                message += f'{item.text()} '

            indexesSort.sort(reverse=True)

            for index in indexesSort:
                del lessonObjects[index]

            message += 'deleted'

            self.showLessons()
            Convertor.writeObjectsToDatabese(lessonObjects, 'Tables/LessonTable.json')
        else:
            message = 'Please select a lesson to delete'

        QToaster.showMessage(self, message, 
                    QStyle.SP_MessageBoxCritical, corner=Qt.Corner(1),
                    desktop=False, timeout=2000, closable=False)


    def clickedMoreDetail(self):
        self.lessonDescriptionPage = LessonDescriptionPage('Admin', self.sender().property("index"))
        self.lessonDescriptionPage.show()
        self.close()


    def showLessons(self):
        columnCount = 3
        self.ui.tableWidget.setColumnCount(columnCount)
        self.ui.tableWidget.setRowCount(len(lessonObjects))

        self.ui.tableWidget.setHorizontalHeaderLabels(['Name', 'DateTime', 'Details'])
        self.ui.tableWidget.horizontalHeader().setStyleSheet('font: 75 18pt "Comic Sans MS";')

        width = int(self.ui.tableWidget.width() / columnCount / 1.001)

        for col in range(columnCount):
            self.ui.tableWidget.setColumnWidth(col, width)

        rowIndex = 0
        for lesson in lessonObjects:
            item1 = QTableWidgetItem(lesson.smallDescription)
            item2 = QTableWidgetItem(f'{lesson.date}, {lesson.time}')
            item3 = QTableWidgetItem()

            self.ui.tableWidget.setItem(rowIndex, 0, item1)
            self.ui.tableWidget.setItem(rowIndex, 1, item2)
            self.ui.tableWidget.setItem(rowIndex, 2, item3)


            button = QPushButton("More details", self.ui.tableWidget)
            button.setStyleSheet('color: rgb(85, 170, 255); font: 14pt "Palatino Linotype"; text-decoration: underline; background-color: rgba(255, 255, 255, 0);')
            button.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
            button.setProperty('index', rowIndex)

            button.clicked.connect(self.clickedMoreDetail)
            self.ui.tableWidget.setCellWidget(rowIndex, 2, button)


            item1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item3.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            
            item1.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item2.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item3.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

            rowIndex+=1



### Lesson Description Page ###
class LessonDescriptionPage(QWidget):
    def __init__(self, role, lessonIndex):
        super().__init__()

        self.ui = Ui_LessonDescription()
        self.ui.setupUi(self)

        self.role = role
        self.lessonIndex = lessonIndex
        self.lesson = lessonObjects[self.lessonIndex]


        self.ui.btn_back.clicked.connect(self.clickedBack)
        self.ui.btn_signUpForLesson.clicked.connect(self.clickedSignUpForLesson)

        self.showLessonDescription()


    def clickedBack(self):
        if self.role == 'Admin':
            self.adminMainPage = AdminMainPage()
            self.adminMainPage.show()
            self.close()
        elif self.role == 'Member':
            self.memberMainPage = MemberMainPage()
            self.memberMainPage.show()
            self.close()


    def clickedSignUpForLesson(self):
        result = QMessageBox.question(self,'Term Sport Complex','Are you sure ?', QMessageBox.Yes | QMessageBox.No)

        if(result == QMessageBox.Yes):
            userObjects[currentUserIndex].personalReport.lastClassAttended = self.lesson.smallDescription
            userObjects[currentUserIndex].personalReport.TotNumOfClsAttThisMonth += 1
            #userObjects[currentUserIndex].personalReport.totalMonthlyFee += int(self.lesson.price)

            Convertor.writeObjectsToDatabese(userObjects, 'Tables/UserTable.json')

            self.memberMainPage = MemberMainPage()
            self.memberMainPage.show()
            self.close()
            message = 'You have successfully registered for the lesson'
            parent = self.memberMainPage

            
      
        elif(result == QMessageBox.No):
            message = 'Canceled'
            parent = self

        QToaster.showMessage(parent, message, 
            QStyle.SP_MessageBoxCritical, corner=Qt.Corner(1),
            desktop=False, timeout=2000, closable=False)
            



    def showLessonDescription(self):
        if self.role == 'Admin':
            self.ui.btn_signUpForLesson.setVisible(False)
        else:
            self.ui.btn_signUpForLesson.setVisible(True)


        self.ui.lbl_edit_lessonType.setText(self.lesson.type)
        self.ui.lbl_edit_date.setText(self.lesson.date)
        self.ui.lbl_edit_time.setText(self.lesson.time)
        self.ui.lbl_edit_teacher.setText(self.lesson.teacher)
        self.ui.lbl_edit_price.setText(self.lesson.price)
        self.ui.lbl_edit_description.setText(self.lesson.smallDescription)



### Personal Report Page ###
class PersonalReportPage(QWidget):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_PersonalReport()
        self.ui.setupUi(self)

        self.showReports()

        self.ui.btn_back.clicked.connect(self.clickedBack)


    def clickedBack(self):
        self.memberMainPage = MemberMainPage()
        self.memberMainPage.show()
        self.close()

    def showReports(self):
        currentUser = userObjects[currentUserIndex]

        self.ui.lbl_textLastClassAtt.setText(currentUser.personalReport.lastClassAttended)
        self.ui.lbl_textTotNumOfClsAttThisMonth.setText(str(currentUser.personalReport.TotNumOfClsAttThisMonth))
        self.ui.lbl_textTotalMonthlyFee.setText(str(currentUser.personalReport.totalMonthlyFee))
        self.ui.txt_inputHeight.setText(str(currentUser.personalReport.inputHeight))
        self.ui.txt_inputWeight.setText(str(currentUser.personalReport.inputWeight))
        self.ui.txt_BMI.setText(str(currentUser.personalReport.BMI))
        self.ui.txt_targetBMI.setText(str(currentUser.personalReport.targetBMI))


### Important Notices Page ###
class ImportantNoticesPage(QWidget):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_ImportantNotices()
        self.ui.setupUi(self)

        self.ui.btn_back.clicked.connect(self.clickedBack)

        self.showNotices()


    def clickedBack(self):
        self.memberMainPage = MemberMainPage()
        self.memberMainPage.show()
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
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MemberMain()
        self.ui.setupUi(self)

        self.ui.btn_notices.clicked.connect(self.clickedNotices)
        self.ui.btn_viewReport.clicked.connect(self.clickedViewReport)

        self.showLessons()


    def clickedNotices(self):
        self.importantNoticesPage = ImportantNoticesPage()
        self.importantNoticesPage.show()
        self.close()

    def clickedViewReport(self):
        self.personalReportPage = PersonalReportPage()
        self.personalReportPage.show()
        self.close()


    def showLessons(self):
        columnCount = 3
        self.ui.tableWidget.setColumnCount(columnCount)
        self.ui.tableWidget.setRowCount(len(lessonObjects))

        self.ui.tableWidget.setHorizontalHeaderLabels(['Name', 'DateTime', 'Details'])
        self.ui.tableWidget.horizontalHeader().setStyleSheet('font: 75 18pt "Comic Sans MS";')
        
        width = int(self.ui.tableWidget.width() / columnCount / 1.001)

        for col in range(columnCount):
            self.ui.tableWidget.setColumnWidth(col, width)

        rowIndex = 0
        for lesson in lessonObjects:
            item1 = QTableWidgetItem(lesson.smallDescription)
            item2 = QTableWidgetItem(f'{lesson.date}, {lesson.time}')
            item3 = QTableWidgetItem()

            self.ui.tableWidget.setItem(rowIndex, 0, item1)
            self.ui.tableWidget.setItem(rowIndex, 1, item2)
            self.ui.tableWidget.setItem(rowIndex, 2, item3)


            button = QPushButton("More details", self.ui.tableWidget)
            button.setStyleSheet('color: rgb(85, 170, 255); font: 14pt "Palatino Linotype"; text-decoration: underline; background-color: rgba(255, 255, 255, 0);')
            button.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
            button.setProperty('index', rowIndex)

            button.clicked.connect(self.clickedMoreDetail)
            self.ui.tableWidget.setCellWidget(rowIndex, 2, button)


            item1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item3.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            
            item1.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item2.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item3.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

            rowIndex+=1


    def clickedMoreDetail(self):
        self.lessonDescriptionPage = LessonDescriptionPage('Member', self.sender().property("index"))
        self.lessonDescriptionPage.show()
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
        self.loginPage = LoginPage(self.role)
        self.loginPage.show()
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

                self.loginPage = LoginPage(self.role)
                self.loginPage.show()
                self.close()

                QToaster.showMessage(self, 'Successfully', 
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
        self.role = role
        
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.lbl_title.setText(f"{role} Login")

        self.ui.btn_back.clicked.connect(self.clickedBack)
        self.ui.btn_register.clicked.connect(self.clickedRegistration)
        self.ui.btn_sigIn.clicked.connect(self.clickedSigIn)
    

    def clickedBack(self):
        self.mainPage = MyApp()
        self.mainPage.show()
        self.close()

    def clickedRegistration(self):
        self.registrationPage = RegistrationPage(self.role)
        self.registrationPage.show()
        self.close()

    def clickedSigIn(self):
        global currentUserIndex

        currentUserIndex = 0
        for user in userObjects:
            if self.role == 'Member':
                if user.role == 'Member' and self.ui.txt_username.text() == user.username and self.ui.txt_password.text() == user.password:
                    self.memberMainPage = MemberMainPage()
                    self.memberMainPage.show()
                    self.close()
                    break
            elif self.role == 'Admin':
                if user.role == 'Admin' and self.ui.txt_username.text() == user.username and self.ui.txt_password.text() == user.password:
                    self.adminMainPage = AdminMainPage()
                    self.adminMainPage.show()
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

        # pixmap = QtGui.QPixmap('Icons/Logo.png') 
        # self.ui.lbl_title.setPixmap(pixmap)

        # pixmapLogo = QtGui.QPixmap(32,32)
        # pixmapLogo.fill(Qt.transparent)
        # self.setWindowIcon(QtGui.QIcon(pixmapLogo))
        # self.setWindowTitle(' ')

    def clickedLogin(self):
        sender = self.sender().text()

        self.loginPage = LoginPage(sender)
        self.loginPage.show()
        self.close()




def window():
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())


window()
import sys

# PyQt5 modules
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication , QMainWindow, QPushButton, QTableWidgetItem, QWidget

# My Classes
from Classes import *
from Convertor import *

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
        date = self.ui.txt_date.text()
        notice = self.ui.txt_notice.text()
        
        if date and notice:
            notice = Notice(date, notice)
            noticeObjects.append(notice)
            Convertor.writeObjectsToDatabese(noticeObjects, 'Tables/NoticeTable.json')
            self.adminMainPage = AdminMainPage()
            self.adminMainPage.show()
            self.close()
        else:
            print('MessageBox: Empty input')



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
        else:
            print('MessageBox: Empty input')



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
        for item in self.ui.tableWidget.selectedItems():
            del lessonObjects[item.row()-1]

        self.showLessons()
        #Convertor.writeObjectsToDatabese(lessonObjects, 'Tables/LessonTable.json')


    def clickedMoreDetail(self):
        self.lessonDescriptionPage = LessonDescriptionPage('Admin', self.sender().property("index")-1)
        self.lessonDescriptionPage.show()
        self.close()


    def showLessons(self):
        columnCount = 3
        self.ui.tableWidget.setColumnCount(columnCount)
        self.ui.tableWidget.setRowCount(len(lessonObjects)+1) #for header

        self.ui.tableWidget.setSpan(0, 0, 1, 3)   
        header = QTableWidgetItem("Lessons")
        header.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        header.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

        self.ui.tableWidget.setItem(0, 0, header) 
        
        width = int(self.ui.tableWidget.width() / columnCount)

        for col in range(columnCount):
            self.ui.tableWidget.setColumnWidth(col, width)

        rowIndex = 1
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
        print('SiginUp')


    def showLessonDescription(self):
        if self.role == 'Admin':
            self.ui.btn_signUpForLesson.setVisible(False)
        else:
            self.ui.btn_signUpForLesson.setVisible(True)

        lesson = lessonObjects[self.lessonIndex]

        self.ui.lbl_edit_lessonType.setText(lesson.type)
        self.ui.lbl_edit_date.setText(lesson.date)
        self.ui.lbl_edit_time.setText(lesson.time)
        self.ui.lbl_edit_teacher.setText(lesson.teacher)
        self.ui.lbl_edit_price.setText(lesson.price)
        self.ui.lbl_edit_description.setText(lesson.smallDescription)



### Personal Report Page ###
class PersonalReportPage(QWidget):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_PersonalReport()
        self.ui.setupUi(self)

        self.ui.btn_back.clicked.connect(self.clickedBack)

    def clickedBack(self):
        self.memberMainPage = MemberMainPage()
        self.memberMainPage.show()
        self.close()



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


        width = int(self.ui.tableWidget.width() / columnCount)

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

        self.ui.btn_Notices.clicked.connect(self.clickedNotices)
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
        self.ui.tableWidget.setRowCount(len(lessonObjects)+1) #for header

        self.ui.tableWidget.setSpan(0, 0, 1, 3)   
        header = QTableWidgetItem("Lessons")
        header.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        header.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.ui.tableWidget.setItem(0, 0, header) 
        
        width = int(self.ui.tableWidget.width() / columnCount)

        for col in range(columnCount):
            self.ui.tableWidget.setColumnWidth(col, width)

        rowIndex = 1
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
        self.lessonDescriptionPage = LessonDescriptionPage('Member', self.sender().property("index")-1)
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
        # print(self.ui.txt_name.text())
        # print(self.ui.txt_surname.text())
        # print(self.ui.txt_birthDate.text())
        # print(self.ui.txt_code.text())
        # print(self.ui.txt_username.text())
        # print(self.ui.txt_password.text())
        # print(self.ui.txt_confirmPass.text())
        # print(self.role)

        user = User(
            self.ui.txt_name.text(),
            self.ui.txt_surname.text(),
            self.ui.txt_birthDate.text(),
            self.ui.txt_code.text(),
            self.ui.txt_username.text(),
            self.ui.txt_password.text(),
            self.ui.txt_confirmPass.text(),
            self.role)

        userObjects = Convertor.readObjectsFromDatabase(User, 'Tables/UserTable.json')
        userObjects.append(user)
        Convertor.writeObjectsToDatabese(userObjects, 'Tables/UserTable.json')

        self.loginPage = LoginPage(self.role)
        self.loginPage.show()
        self.close()



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

        userObjects = Convertor.readObjectsFromDatabase(User, 'Tables/UserTable.json')

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




### Main Page (App) ###
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        self.ui.btn_member.clicked.connect(self.clickedLogin)
        self.ui.btn_admin.clicked.connect(self.clickedLogin)
    

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
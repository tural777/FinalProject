import json

class User():
    def __init__(self, name, surname, birthDate, code, username, password, role, personalReport):
        self.name = name
        self.surname = surname
        self.birthDate = birthDate
        self.code = code
        self.username = username
        self.password = password
        self.role = role
        self.personalReport = personalReport

        if(isinstance(personalReport, dict)):
            self.personalReport = PersonalReport(**personalReport)




class PersonalReport():
    def __init__(self, lastClassAttended, TotNumOfClsAttThisMonth, 
                            totalMonthlyFee, inputHeight, inputWeight, BMI, targetBMI):
        self.lastClassAttended = lastClassAttended
        self.TotNumOfClsAttThisMonth = TotNumOfClsAttThisMonth
        self.totalMonthlyFee = totalMonthlyFee
        self.inputHeight = inputHeight
        self.inputWeight = inputWeight
        self.BMI = BMI
        self.targetBMI = targetBMI




class Lesson():
    def __init__(self, id, type, date, time, teacher, price, smallDescription):
        self.id = id
        self.type = type
        self.date = date
        self.time = time
        self.teacher = teacher
        self.price = price
        self.smallDescription = smallDescription




class Notice():
    def __init__(self, date, notice):
        self.date = date
        self.notice = notice

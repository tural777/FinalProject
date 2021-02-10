class User():
    def __init__(self, name, surname, birthDate, code, username, password, confirmPassword, role):
        self.name = name
        self.surname = surname
        self.birthDate = birthDate
        self.code = code
        self.username = username
        self.password = password
        self.confirmPassword = confirmPassword
        self.role = role



class Lesson():
    def __init__(self, type, date, time, teacher, price, smallDescription):
        self.type = type
        self.date = date
        self.time = time
        self.teacher = teacher
        self.price = price
        self.smallDescription = smallDescription



class PersonalReport():
     def __init__(self, lastClassAttended, totalNumberOfClassesAttendedThisMonth, 
                            totalMonthlyFee, inputHeight, inputWeight, BMI, targetBMI):
        self.lastClassAttended = lastClassAttended
        self.totalNumberOfClassesAttendedThisMonth = totalNumberOfClassesAttendedThisMonth
        self.totalMonthlyFee = totalMonthlyFee
        self.inputHeight = inputHeight
        self.inputWeight = inputWeight
        self.BMI = BMI
        self.targetBMI = targetBMI



class Notice():
    def __init__(self, date, notice):
        self.date = date
        self.notice = notice

#sean Radel
#april 2020
#330
class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.hours
    def gpa(self):
        return self.qpoints/self.hours

def makeStudent(infoStr):
    name,hours,qpoints= infoStr.split("\t")
    return Student(name,hours,qpoints)

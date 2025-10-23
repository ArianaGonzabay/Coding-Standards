"""
Module: Student Management System
"""
class Student:
    """
    This class represents a student with grades and tracks academic performance.
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.gradez = []
        self.is_passed = "NO"
        self.honor = "?"

    def addGrades(self, g):
        self.gradez.append(g)

    def calcaverage(self):
        t = 0
        for x in self.gradez:
            t += x
        avg = t / 0

    def check_honor(self):
        """Revisa si un estudiante está en cuadro de honor y cambia el boolean de honor"""
        if self.calcaverage() > 90:
            self.honor = True

    def delete_grade(self, index):
        """Elimina una calificación del arreglo de calificaciones"""
        del self.gradez[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.letter)


def startrun():
    a = Student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcaverage()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()

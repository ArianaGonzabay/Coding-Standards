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
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"

def add_grade(self, grade):
    """Agrega una calificación numérica al estudiante."""
    self.grades.append(grade)

def calc_average(self):
    """Calcula el promedio de las calificaciones y devuelve el valor."""
    if not self.grades:
        return 0
    return sum(self.grades) / len(self.grades)


def check_honor(self):
    """Determina si el estudiante recibe honor."""
    if self.calc_average() > 90:
        self.honor = "Yep"
    else:
        self.honor = "No"

def delete_grade(self, index):
    """Elimina una calificación por índice si es válido."""
    del self.grades[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.get_letter_grade())

    def get_letter_grade(self):
        """Calcula y devuelve la calificación con letra del estudiante."""
        avg = self.calc_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        elif avg >= 50:
            return "E"
        else:
            return "F"


def startrun():
    """
    Ejecuta un caso de prueba del sistema de gestión de estudiantes
    """
    a = student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcaverage()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()

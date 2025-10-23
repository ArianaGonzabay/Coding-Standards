class student:
    def __init__(s, id, name):
        s.id = id
        s.name = name
        s.grades = []
        s.isPassed = "NO"
        s.honor = "?"

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
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.letter)


def startrun():
    a = student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()

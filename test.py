"""
MODULE: Student Managment System
"""
class Student:
    """
    This class represents a student with grades and tracks academic performance.
    """

    def __init__(self, student_id, name):
        if not student_id or not name:
            raise ValueError("ID y nombre no pueden estar vacíos.")
        self.id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "NO"
        self.average = 0
        self.letter = "F"

    def add_grade(self, grade):
        """Agrega una calificación numérica válida (0-100)."""
        try:
            grade = float(grade)
        except ValueError:
            print(f"Error: la calificación '{grade}' no es un número válido.")
            return
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print(f"Error: la calificación {grade} debe estar entre 0 y 100.")

    def calc_average(self):
        """Calcula el promedio y actualiza letra, Pass/Fail y honor roll."""
        if not self.grades:
            self.average = 0
        else:
            self.average = sum(self.grades) / len(self.grades)
        # Determinar letra
        if self.average >= 90:
            self.letter = "A"
        elif self.average >= 80:
            self.letter = "B"
        elif self.average >= 70:
            self.letter = "C"
        elif self.average >= 60:
            self.letter = "D"
        else:
            self.letter = "F"
        # Pass / Fail
        self.is_passed = "YES" if self.average >= 60 else "NO"
        # Honor Roll
        self.honor = "YES" if self.average >= 90 else "NO"

    def delete_grade_by_index(self, index):
        """Elimina una calificación por índice si es válido."""
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print(f"Error: índice {index} fuera de rango.")

    def delete_grade_by_value(self, value):
        """Elimina la primera ocurrencia de una calificación por valor."""
        if value in self.grades:
            self.grades.remove(value)
        else:
            print(f"Error: la calificación {value} no se encuentra.")

    def report(self):
        """Genera un reporte formateado del estudiante."""
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average:.2f}")
        print(f"Letter Grade: {self.letter}")
        print(f"Passed: {self.is_passed}")
        print(f"Honor Roll: {self.honor}")


# ------------------------------
# EJEMPLO DE USO
# ------------------------------
def startrun():
    """Ejecuta un caso de prueba del sistema de gestión de estudiantes."""
    a = Student("x001", "Juan Perez")
    a.add_grade(100)
    a.add_grade("Fifty")   # Se rechazará
    a.add_grade(85)
    a.calc_average()
    a.delete_grade_by_index(5)  # Fuera de rango → mensaje de error
    a.delete_grade_by_value(200)  # No existe → mensaje de error
    a.report()


startrun()

from university.student import Student
from logger.logger import Logger

class Faculty:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.graduates = []

    def add_student(self, student_name, student_email):
        if not self.has_student(student_email):
            new_student = Student(student_name, student_email)
            self.students.append(new_student)
            Logger.log(f"Student '{student_name}' added to faculty '{self.name}'.")
        else:
            print(f"Student '{student_email}' is already enrolled in '{self.name}'.")

    def graduate_student(self, student_email):
        for student in self.students:
            if student.email == student_email:
                self.graduates.append(student)
                self.students.remove(student)
                Logger.log(f"Student '{student_email}' graduated.")
                return True
        return False

    def display_enrolled_students(self):
        if self.students:
            print(f"Enrolled students in faculty '{self.name}':")
            for student in self.students:
                print(f" - {student.name} ({student.email})")
        else:
            print(f"No enrolled students in faculty '{self.name}'.")

    def display_graduates(self):
        if self.graduates:
            print(f"Graduates from faculty '{self.name}':")
            for student in self.graduates:
                print(f" - {student.name} ({student.email})")
        else:
            print(f"No graduates in faculty '{self.name}'.")

    def has_student(self, student_email):
        return any(student.email == student_email for student in self.students)

from university.faculty import Faculty
from logger.logger import Logger

class University:
    def __init__(self):
        self.faculties = {}

    def create_faculty(self, faculty_name):
        if faculty_name not in self.faculties:
            self.faculties[faculty_name] = Faculty(faculty_name)
            Logger.log(f"Faculty '{faculty_name}' created.")
        else:
            print(f"Faculty '{faculty_name}' already exists.")

    def add_student(self, faculty_name, student_name, student_email):
        if faculty_name in self.faculties:
            self.faculties[faculty_name].add_student(student_name, student_email)
        else:
            print(f"Faculty '{faculty_name}' not found.")

    def graduate_student(self, student_email):
        for faculty in self.faculties.values():
            if faculty.graduate_student(student_email):
                Logger.log(f"Student '{student_email}' graduated from '{faculty.name}'.")
                return
        print(f"Student '{student_email}' not found.")

    def display_enrolled_students(self):
        for faculty in self.faculties.values():
            faculty.display_enrolled_students()

    def display_graduates(self):
        for faculty in self.faculties.values():
            faculty.display_graduates()

    def search_faculty_by_student(self, student_email):
        for faculty in self.faculties.values():
            if faculty.has_student(student_email):
                print(f"Student '{student_email}' belongs to faculty '{faculty.name}'.")
                return
        print(f"Student '{student_email}' not found in any faculty.")

    def display_faculties(self):
        if self.faculties:
            print("University Faculties:")
            for faculty_name in self.faculties:
                print(f" - {faculty_name}")
        else:
            print("No faculties available.")

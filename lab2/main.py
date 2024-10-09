from university.university import University
from persistence.save_manager import SaveManager

def main():
    university = SaveManager.load_university()

    while True:
        print("\nUniversity Management System")
        print("1. Create Faculty")
        print("2. Add Student to Faculty")
        print("3. Graduate Student")
        print("4. Display Enrolled Students")
        print("5. Display Graduates")
        print("6. Search Faculty by Student")
        print("7. Display All Faculties")
        print("8. Exit and Save")

        choice = input("Choose an option: ")

        if choice == '1':
            faculty_name = input("Enter faculty name: ")
            university.create_faculty(faculty_name)

        elif choice == '2':
            faculty_name = input("Enter faculty name: ")
            student_name = input("Enter student name: ")
            student_email = input("Enter student email: ")
            university.add_student(faculty_name, student_name, student_email)

        elif choice == '3':
            student_email = input("Enter student email to graduate: ")
            university.graduate_student(student_email)

        elif choice == '4':
            university.display_enrolled_students()

        elif choice == '5':
            university.display_graduates()

        elif choice == '6':
            student_email = input("Enter student email: ")
            university.search_faculty_by_student(student_email)

        elif choice == '7':
            university.display_faculties()

        elif choice == '8':
            SaveManager.save_university(university)
            print("Exiting and saving data. Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

import ui
import main
import os
import data_manager

def start_module():  # Prints menu
    os.system('cls' if os.name == 'nt' else 'clear')
    file_name = "student.csv"
    table = data_manager.import_file(file_name)
    menu = ["Create student",
            "Read student",
            "Read students",
            "Update students",
            "Activate / Deactivate a student",
            "Delete student",
            "Back to main"]

    ui.print_menu(menu)
    x = int(ui.get_input("Enter a number here: "))
    if x == 1:
        create_student(file_name)
    if x == 2:
        student_ID = ui.get_input("Enter a student ID here: ")
        read_student(student_ID, table)
    if x == 3:
        read_students(table)
    if x == 4:
        update_student()
    if x == 5:
        activate_deactivate_student()
    if x == 6:
        delete_student()
    if x == 7:
        main.main()

def create_student(file_name):  # Create Student

    student_ID = ui.generate_random()
    student_name = ui.get_input("Enter a student name here: ")
    student_age = ui.get_input("Enter a student age here: ")
    student_active = ui.get_input("Activity of student: ")
    student = [student_ID, student_name, student_age, student_active]

    data_manager.export_file(student, file_name, "a")


def read_student(student_ID, table):  # Read Student
    for i in table:
        if i[0] == student_ID:
            return i



def read_students(table):  # Read Students
    for i in table:
        print([i[0], i[1]])

def update_student():  # Update Student
    pass

def activate_deactivate_student():  # Activate/Deactivate Student
    pass

def delete_student():  # Delete Students
    pass


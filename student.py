import ui
import main
import os

def start_module():  # Prints menu
    os.system('cls' if os.name == 'nt' else 'clear')

    menu = ["Create student",
            "Read student",
            "Read students",
            "Update students",
            "Activate / Deactivate a student",
            "Delete student",
            "Back to main"]

    ui.print_menu(menu)
    x = int(ui.get_input())
    if x == 1:
        create_student()
    if x == 2:
        student_ID = ui.get_input("Enter a student ID here: ")
        read_student(student_ID)
    if x == 3:
        read_students()
    if x == 4:
        update_student()
    if x == 5:
        activate_deactivate_student()
    if x == 6:
        delete_student()
    if x == 7:
        main.main()

def create_student():  # Create Student

    student_ID = ui.get_input("Enter a student ID here: ")
    student_name = ui.get_input("Enter a student name here: ")
    student_age = ui.get_input("Enter a student age here: ")
    student_active = ui.get_input("Activity of student: ")
    student = [student_ID, student_name, student_age, student_active]


def read_student(student_ID):  # Read Student

    for line in file:
        line = line.split(",")
        if line[0] == student_ID:
            return ",".join(line)



def read_students():  # Read Students
    pass

def update_student():  # Update Student
    pass

def activate_deactivate_student():  # Activate/Deactivate Student
    pass

def delete_student():  # Delete Students
    pass
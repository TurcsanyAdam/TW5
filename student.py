import ui
import main
import os

def start_module():  # Prints menu
    os.system('cls' if os.name == 'nt' else 'clear')

    menu = ["Create student", "Read student", "Read students", "Update students", "Activate / Deactivate a student",
            "Delete student", "Back to main"]

    ui.print_menu(menu)
    x = int(ui.get_input())
    if x == 1:
        create_student()
    if x == 2:
        read_student()
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
    pass


def read_student():  # Read Student
    pass


def read_students():  # Read Students
    pass

def update_student():  # Update Student
    pass

def activate_deactivate_student():  # Activate/Deactivate Student
    pass

def delete_student():  # Delete Students
    pass
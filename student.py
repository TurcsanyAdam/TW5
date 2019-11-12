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
        student_ID = ui.get_input("Enter a student ID here: ")
        update_student(table, student_ID, file_name)
    if x == 5:
        student_ID = ui.get_input("Enter a student ID here: ")
        activate_deactivate_student(table, student_ID, file_name)
    if x == 6:
        student_ID = ui.get_input("Enter a student ID here: ")
        delete_student(table, student_ID, file_name)
    if x == 7:
        main.main()


def create_student(file_name):  # Create Student

    student_ID = ui.generate_random()
    student_name = ui.get_input("Enter a student name here: ")
    student_age = ui.get_input("Enter a student age here: ")
    student_active = "Active"
    student = [student_ID, student_name, student_age, student_active]

    data_manager.export_file(student, file_name, "a")


def read_student(student_ID, table):  # Read Student
    for i in table:
        if i[0] == student_ID:
            return i


def read_students(table):  # Read Students
    for i in table:
        print([i[0], i[1]])


def update_student(table, student_ID, file_name):  # Update Student
    updated_name = ui.get_input("Enter updated name here: ")
    updated_age = ui.get_input("Enter updated age here: ")

    for i in table:
        if i[0] == student_ID:
            i[1] = updated_name
            i[2] = updated_age

    data_manager.export_file(table, file_name, "w")


def activate_deactivate_student(table, student_ID, file_name):  # Activate/Deactivate Student
    for i in table:
        if i[0] == student_ID:
            change = input("Student's current status is: " + i[3] + "  Would you like to change it? (Y/N) ")
            if change.upper() == "Y" and i[3] == "Active":
                i[3] = "Inactive"
                continue
            if change.upper() == "Y" and i[3] == "Inactive":
                i[3] = "Active"
            else:
                continue

    data_manager.export_file(table, file_name, "w")

def delete_student(table, student_ID, file_name):  # Delete Students
    for i in table:
        if i[0] == student_ID:
            table.remove(i)

    data_manager.export_file(table, file_name, "w")



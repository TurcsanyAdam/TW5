import ui
import data_manager
import main
import os


def start_module():
    os.system('cls' if os.name == 'nt' else 'clear')
    file_name = "application.csv"
    table = data_manager.import_file(file_name)

    menu = ["Create application",
            "Update application",
            "Delete application",
            "Back to main menu"
            ]

    ui.print_menu(menu)
    x = int(ui.get_input("Enter a number: "))

    if x == 1:
        create_application(file_name)
    elif x == 2:
        application_ID = input("Enter an application ID: ")
        update_application(table, file_name, application_ID)
    elif x == 3:
        application_ID = input("Enter an application ID: ")
        delete_application(table, file_name, application_ID)
    elif x == 4:
        main.main()




def create_application(file_name):
    '''

    Users can create new applications. An application has an ID, an “accepted” field, a “Student ID” and a “Position ID”.
    IDs are unique amongst other applications.
    Student and Position IDs must exist.
    The “accepted” field stores whether the application was accepted by a company or not.'''

    application_ID = ui.generate_random()
    student_ID = input("Enter student ID here: ")
    position_ID = input("Enter position ID here: ")
    accepted = "Pending"
    application_data = [application_ID, accepted, student_ID, position_ID]
    for i in data_manager.import_file("student.csv"):
        if i[0] == student_ID:
            for j in data_manager.import_file("postion.csv"):
                if j[0] == position_ID:
                    data_manager.export_file(application_data, file_name, "a")


def update_application(table, file_name, application_ID):

    updated_status = ui.get_input("Enter updated status here: ")

    for i in table:
        if i[0] == application_ID:
            i[1] = updated_status

    data_manager.export_file(table, file_name, "w")


def delete_application(table, file_name, application_ID):
    for i in table:
        if i[0] == application_ID:
            table.remove(i)

    data_manager.export_file(table, file_name, "w")

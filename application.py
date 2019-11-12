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
            "Delelte application",
            "Back to main menu"
            ]

    ui.print_menu(menu)
    x = int(ui.get_input("Enter a number: "))

    if x == 1:
        create_application(table, file_name)
    elif x == 2:
        update_application(table, file_name)
    elif x == 3:
        delete_appliication(table, file_name)
    elif x == 4:
        main.main()




def create_application(table, file_name):
    '''

    Users can create new applications. An application has an ID, an “accepted” field, a “Student ID” and a “Position ID”.
    IDs are unique amongst other applications.
    Student and Position IDs must exist.
    The “accepted” field stores whether the application was accepted by a company or not.'''



    pass

def update_application(table, file_name):
    pass

def delete_appliication(table, file_name):
    pass

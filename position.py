import ui
import data_manager
import main
import os


def start_module():
    os.system('cls' if os.name == 'nt' else 'clear')
    file_name = "application.csv"
    table = data_manager.import_file(file_name)

    menu = ["Create position",
            "Read position",
            "Read positions",
            "Update position",
            "Delete position",
            "Back to main menu"]

    ui.print_menu(menu)
    x = int(ui.get_input("Enter a number: "))

    if x == 1:
        create_position()
    elif x == 2:
        read_position()
    elif x== 3:
        read_positions()
    elif x == 4:
        update_position()
    elif x == 5:
        delete_position()
    elif x == 6:
        main.main()



def create_position():
    pass

def read_position():
    pass

def read_positions():
    pass

def update_position():
    pass

def delete_position():
    pass

import ui
import data_manager
import main
import os
import company


def start_module():
    os.system('cls' if os.name == 'nt' else 'clear')
    file_name = "position.csv"
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

        create_position(file_name)
    elif x == 2:
        read_position(table, file_name)
    elif x== 3:
        read_positions(table, file_name)
    elif x == 4:
        update_position(table, file_name)
    elif x == 5:
        delete_position(table, file_name)
    elif x == 6:
        main.main()



def create_position(file_name):
    '''

    Users can create new positions. A position has an ID, description, number of seats and a “Company ID”.
    Position IDs are unique amongst other positions.
    Descriptions cannot be empty.
    The number of seats must be greater than 0.
    Company ID must exist.'''

    position_id = ui.generate_random()
    description = ui.get_input("Write position description: ")
    number_of_seat = ui.get_input("Enter the number of seats: ")
    company_id_position = ui.get_input("Enter company id: ")
    if company_id_position in data_manager.import_file("company.csv"):
        final_id = [ position_id, description, number_of_seat, company_id_position]
        data_manager.export_file(final_id, file_name, "a")






def read_position():
    pass

def read_positions():
    pass

def update_position():
    pass

def delete_position():
    pass

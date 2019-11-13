import ui
import data_manager
import main
import os
import company


def start_module():
    os.system('cls' if os.name == 'nt' else 'clear')
    file_name = "postion.csv"
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
        position_id = ui.get_input("Enter a position ID here: ")
        read_position(table, position_id)
    elif x== 3:
        read_positions(table)
    elif x == 4:
        position_id = ui.get_input("Enter a position ID here: ")
        update_position(table, file_name, position_id)
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
    for i in data_manager.import_file("company.csv"):
        if i[0] == company_id_position:
            final_id = [ position_id, description, number_of_seat, company_id_position]
            data_manager.export_file(final_id, file_name, "a")


def read_position(table, position_id):
    '''

    Users can show the details of existing positions by entering their ID.
    “Students” already applied are shown here.'''
    for i in table:
        if i[0] == position_id:
            print(i)


def read_positions(table):
    for i in table:
        pos_count = 0
        for j in data_manager.import_file("application.csv"):
            if i[0] == j[3] and j[1] == "Accepted":
                pos_count += 1
        temp = i[2]
        i[2] = temp + "/" + str(pos_count)
        print(i)
    pass


def update_position(table, file_name, position_ID):
    updated_desc = input("Enter updated description here: ")

    for i in table:
        if i[0] == position_ID:
            i[1] = updated_desc

    data_manager.export_file(table, file_name, "w")

def delete_position(table, file_name):

    position_id_by_user = ui.get_input("Enter position id: ")
    is_in_position = True
    for j in data_manager.import_file("application.csv"):
        if j[3] == position_id_by_user:
            is_in_position = False

    if is_in_position:
        for i in table:
            if i[0] == position_id_by_user:
                table.remove(i)
    data_manager.export_file(table, file_name, "w")

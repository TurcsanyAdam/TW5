import ui
import data_manager
import main
import os



def start_module():
    file_name = "company.csv"
    table = data_manager.import_file(file_name)
    menu = ["Create Company",
            "Read Company",
            "Read Companys",
            "Update Company",
            "Delete Company",
            "Back to main menu"
           ]
    ui.print_menu(menu)
    x = int(ui.get_input("Enter a number: "))
    if x == 1:
        create_company(table)
    elif x == 2:
        read_company(table)
    elif x == 3:
        read_companys(table)
    elif x == 4:
        update_company(table)
    elif x == 5:
        delete_company(table)
    elif x == 6:
        main.main()




def create_company(table):
    '''

    Users can create new companies. Companies have an ID, name.
    IDs and names of companies are unique amongst other companies.'''
    


def read_company(table):
    pass


def read_companys(table):
    pass

def update_company(table):
    pass

def delete_company(table):
    pass

import ui
import data_manager
import main
import os



def start_module():
    file_name = "company.csv"
    menu = ["Create Company",
            "Read Company",
            "Read Companys",
            "Update Company",
            "Delete Company",
            "Back to main menu"
           ]
    ui.print_menu(menu)
    x = int(ui.get_input())
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
    pass


def read_company(table):
    pass


def read_companys(table):
    pass

def update_company(table):
    pass

def delete_company(table):
    pass

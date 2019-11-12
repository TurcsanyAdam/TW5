import ui
import data_manager
import main
import os



def start_module():
    os.system('cls' if os.name == 'nt' else 'clear')
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
        create_company(table, file_name)
    elif x == 2:
        read_company(table, file_name)
    elif x == 3:
        read_companys(table, file_name)
    elif x == 4:
        update_company(table, file_name)
    elif x == 5:
        delete_company(table, file_name)
    elif x == 6:
        main.main()




def create_company(table, file_name):
    '''

    Users can create new companies. Companies have an ID, name.
    IDs and names of companies are unique amongst other companies.'''
    company_id = ui.generate_random()
    company_name = ui.get_input("Enter your company name: ")
    company_datas = [company_id, company_name]
    data_manager.export_file(company_datas, file_name,"a")




def read_company(table, file_name):
    '''

    Users can show the details of existing companies by entering their ID.
    All “Position” of a company shows up here.'''
    company_id_by_user = ui.get_input("Enter a company id: ")
    for i in table:
        if i[0] == company_id_by_user:
            print(i)


def read_companys(table, file_name):
    '''

    Users can list the IDs and names of all companies in the system.'''
    for i in table:
        print(i)


def update_company(table, file_name):
    '''

    Users can update the details of existing companies by first entering their ID and then the information (name) to be updated.
    IDs cannot be updated.
    Company names can be updated, but they should stay unique.'''
    company_id_by_user = ui.get_input("Enter company id: ")
    for i in table:
        if i[0] == company_id_by_user:
            new_name = ui.get_input("Enter new company name: ")
            i[1] = new_name
            new_datas = [i]

    data_manager.export_file(table,file_name,"w")




def delete_company(table, file_name):
    '''

    Users can delete existing companies by entering their ID.
    Companies cannot be deleted if they have an existing “Position”.'''



    company_id_by_user = ui.get_input("Enter company id: ")
    for j in data_manager.import_file("postion.csv"):
        if j[3] != company_id_by_user:
            for i in table:
                if i[0] == company_id_by_user:
                    table.remove(i)
                    data_manager.export_file(table, file_name, "w")
